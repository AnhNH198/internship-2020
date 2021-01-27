# Authorization

* After authentication, authorization controls what the user can do, where does the user have access to

* The access controls are implemented on an API level (kube-apiserver)

* When an API request comes in (e.g. when you enter kubectl get nodes), it will be checked to see whether you have access to execute this command

##### There are multiple authorization module available:
* Node: a special purpose authorization mode that authorizes API requests made by kubelets

* ABAC: attribute-based access control
  
  * Access rights are controlled by policies that combine attributes
  
  * e.g. user “alice" can do anything in namespace “marketing”
  
  * ABAC does not allow very granular permission control

* RBAC: role based access control
  
  * Regulates access using roles
  
  * Allows admins to dynamically configure permission policies
  
  * This is what I’ll use in the demo

* Webhook: sends authorization request to an external REST interface
  
  * Interesting option if you want to write your own authorization server
  
  * You can parse the incoming payload (which is JSON) and reply with access granted or access denied


##### RBAC

To enable an authorization mode, you need to pass --authorization-mode= to the API server at startup

For example, to enable RBAC, you pass —authorization-mode=RBAC

Most tools now provision a cluster with RBAC enabled by default (like kops and kubeadm)

For minikube, it’ll become default at some point (see https://github.com/kubernetes/minikube/issues/1722)

### RBAC

* You can **add RBAC resources** with kubectl to grant permissions

  * You first describe them in **yaml** format, then apply them to the cluster
* First you define a **role**, then you can **assign users/groups** to that role
* You can create roles **limited to a namespace** or you can create roles where the **access applies to all namespaces**
  * Role (single namespace) and ClusterRole (cluster-wide)
  * RoleBinding (single namespace) and ClusterRoleBinding (cluster-wide)

##### RBAC Role
* RBAC Role granting read access to pods and secrets within default namespace
```
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
namespace: default
name: pod-reader
rules:
- apiGroups: [""]
resources: [“pods”, “secrets”]
verbs: ["get", "watch", "list"]
```

* Next step is to assign users to the newly created role

```
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
name: read-pods
namespace: default
subjects:
- kind: User
name: bob
apiGroup: rbac.authorization.k8s.io
roleRef:
kind: Role
name: pod-reader
apiGroup: rbac.authorization.k8s.io
```

* If you rather want to create a role that spans all namespaces, you can use ClusterRole
```
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
name: pod-reader-clusterwide
rules:
- apiGroups: [""]
resources: [“pods”, “secrets”]
verbs: ["get", "watch", "list"]
```

* If you need to assign a user to a cluster-wide role, you need to use ClusterRoleBinding
```
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
name: read-pods
subjects:
- kind: User
name: alice
apiGroup: rbac.authorization.k8s.io
roleRef:
kind: Role
name: pod-reader-clusterwide
apiGroup: rbac.authorization.k8s.io
```