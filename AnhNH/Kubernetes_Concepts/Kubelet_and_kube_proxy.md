The kubelet is the Kubernetes node agent that runs on each node. It has many roles.
* It communicates with the API server to see if pods have been assigned to the nodes.
* It executes the pod containers via the container engine.
* It mounts and runs pod volumes and secrets.
* It executes health checks and is aware of pod and node status and reports that back to the API server.

The kubelet works in terms of Podspec, which is just a YAML file that describes the pod.

The kubelet takes a set of Podspecs that are provided by the kube-apiserver and ensures that the containers described in those Podscpecs are running and healthy. It's important to note that the kubelet only manages containers that were created by the API server, and not any other containers that might be running on the node. We can also manage the kubelet without an API server by using HTP endpoint or a file.

The network proxy is called the kube-proxy.

This is another process that runs on all the worker nodes.
The kube-proxy reflects services that are defined in the API on each node and can do simple network stream or round-robin forwarding across a set of backends. Service cluster IPs and ports are currently found through Docker-link compatible environment variables specifying ports opened by the service proxy.

* The kube-proxy has three modes:
  - the user space mode,
  - Iptables mode,
  - ipvs mode, which is an alpha feature in Kuberetes 1.8.

* The user space is the most common mode.

* Why these mode are important
  - These modes are important when it comes to using services.
  - Services are defined against the API server. The kube-proxy watches the API server for addition and removal of services.
  - For each new service, kube-proxy opens a randomly chosen port on the local node. Any connections made to that port are proxied to one of the corresponding back-end pods.
