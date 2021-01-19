# Bringing everything together

![](images/summarize.png)
Resources in a typical application

A typical application manifest contains one or more Deployment and/or StatefulSet
objects. Those include a pod template containing one or more containers, **with a live-
ness probe for each of them** and a **readiness probe for the service(s)** the container
provides (if any). Pods that provide services to others are exposed through one or
more Services. When they need to be reachable from outside the cluster, the Services
are either configured to be LoadBalancer or NodePort -type Services, or exposed
through an Ingress resource.
The pod templates (and the pods created from them) usually reference two types
of Secrets—those for pulling container images from private image registries and those
used directly by the process running inside the pods. The Secrets themselves are
usually not part of the application manifest, because they aren’t configured by the
application developers but by the operations team. Secrets are usually assigned to
ServiceAccounts, which are assigned to individual pods.

The **application** also **contains one or more ConfigMaps**, which are either **used to
initialize environment variables** or **mounted as a configMap volume in the pod**. Cer-
tain pods use additional volumes, such as an emptyDir or a gitRepo volume, whereas
**pods requiring persistent storage use persistentVolumeClaim volumes**. The Persistent-
VolumeClaims are also part of the application manifest, whereas StorageClasses refer-
enced by them are created by system administrators upfront.
In certain cases, an application also requires the use of Jobs or CronJobs. **Daemon-
Sets aren’t normally part of application deployments, but are usually created by sysad-
mins to run system services on all or a subset of nodes.** 

**HorizontalPodAutoscalers** are either included in the manifest by the developers or added to the system later **by the ops team**. 

The **cluster administrator** also **creates LimitRange and ResourceQuota
objects** to **keep compute resource usage of individual pods and all the pods (as a whole) under control.**

**After the application is deployed**, **additional objects are created automatically** by the various Kubernetes **controllers**. 
These include service Endpoints objects created by the **Endpoints controller**, **ReplicaSets** created by the **Deployment controller**, and the actual pods created by the ReplicaSet (or Job, CronJob, StatefulSet, or DaemonSet) controllers.

**Resources** **are often labeled with one or more labels to keep them organized**. This doesn’t **apply** only to pods but **to all other resources** as well. In addition to **labels**, **most resources also contain annotations that describe each resource**, **list the contact infor-mation of the person or team responsible for it**, or **provide additional metadata for
management and other tools**.

At the center of all this is the Pod, which arguably is the most important Kuberne-
tes resource. After all, each of your applications runs inside it. To make sure you know
how to develop apps that make the most out of their environment let’s take one last
close look at pods—this time from the application’s perspective.

