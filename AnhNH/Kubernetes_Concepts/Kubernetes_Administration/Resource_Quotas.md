# Resources Quotas

* When a Kubernetes cluster is used by multiple people or teams, resource management becomes more important
  
  * You want to be able to manage the resources you give to a person or
a team
 
  * You don’t want one person or team taking up all the resources (e.g.
CPU/Memory) of the cluster
 
* You can divide your cluster in namespaces (explained in next lecture) and
enable resource quotas on it

  * You can do this using the ResourceQuota and ObjectQuota objects



* Each container can specify request capacity and capacity limits
    
    * Request capacity is an explicit request for resources
    
    * The scheduler can use the request capacity to make decisions on where to put the pod on
    
    * You can see it as a minimum amount of resources the pod needs

* Resource limit is a limit imposed to the container
  
  * The container will not be able to utilize more resources than
specified


### Example of resource quotas:

*   You run a deployment with a pod with a CPU resource request of 200m

*   200m = 200 millicpu (or also 200 millicores)

* 200m = 0.2, which is 20% of a CPU core of the running node
  * If the node has 2 cores, it’s still 20% of a single core

* You can also put a limit, e.g. on 400m

* Memory quotas are defined by MiB or GiB

* If a capacity quota (e.g. mem / cpu) has been specified by the
administrator, then each pod needs to specify capacity quota during
creation
  * The administrator can specify default request values for pods that don’t
specify any values for capacity
  * The same is valid for limit quotas
* If a resource is requested more than the allowed capacity, the server API
will give an error 403 FORBIDDEN - and kubectl will show an error

