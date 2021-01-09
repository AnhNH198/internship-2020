# Autoscaling (Horizontal Pod Autoscaling)

* Kubernetes has the possibility to automatically scale pods based on metrics
* Kubernetes can automatically scale a Deployment, Replication Controller or ReplicaSet
* In Kubernetes 1.3 scaling based on CPU usage is possible out of the box

  * With alpha support, application based metrics are also available (like queries per second or average request latency)
  * To enable this, the cluster has to be started with the env var ENABLE_CUSTOM_METRICS to true


* Autoscaling will periodically query the utilization for the targeted pods
  * By default 30 sec, can be changed using the “—horizontal-pod-autoscaler-sync-period” when launching the controller-manager
* Autoscaling will use metric-server, the monitoring tool, to gather its metrics and make scaling decisions
  * metric-server must be installed and running before autoscaling will work

##### Example
* You run a deployment with a pod with a CPU resource request of 200m
* 200m = 200 millicpu (or also 200 millicores)
* 200m = 0.2, which is 20% of a CPU core of the running node
* If the node has 2 cores, it’s still 20% of a single core
* You introduce auto-scaling at 50% of the CPU usage (which is 100m)
* Horizontal Pod Autoscaling will increase/descrease pods to maintain a
target CPU utilization of 50% (or 100m / 10% of a core within this pod)