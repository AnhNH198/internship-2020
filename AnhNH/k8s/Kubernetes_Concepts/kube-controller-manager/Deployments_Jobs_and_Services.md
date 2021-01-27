Không nên sử dụng trực tiếp Pod mà thay vào đó ta dùng controller.

### Lợi ích của controller:
 - Application reliability: Nhiều instance của một app được chạy -> phòng tránh việc lỗi khi một hoặc nhiều instace fail
 - Scaling: Khi Pod gặp lượng lớn request, Kubernetes cho phép ta scale up pods, tăng khả năng chịu tải của pods
 - load balancing: nhiều pod chạy cho phep traffic được flow tới các pods khác nhau và không bị quá tải single pod hay single node.

 ### Các loại controller
 ##### ReplicaSets
  - replicaset đảm bảo số lượng cụ thể của pod được running
  - Nếu số lượng pod ít hơn ReplicaSet được cấu hình(VÍ dụ 1 pod bị crashed) ReplicaSet sẽ tự động khởi động Pod mới lên
  - Ta không thể tự khai bao Replicaset mà phải thông qua cấu hình trong Deployment

 ##### Deployment
  - A Deployment Controller provides declarative updates for pods and ReplicaSets.
     - This means that you can describe the desired state of a deployment in a YAML file and the Deployment Controller will align the actual state to match.
  - Deployments can be defined to create new ReplicaSets or replace existing ones with new ones.
  - Most applications are packages deployments, so chances are, you'll end up creating Deployments more than anything else.

  - Essentially, a deployment manages a ReplicaSet which, in turn, manages a pod.
    - The benefit of this architecture is that deployments can automatically support a role-back mechanism.
    -     A new ReplicaSet is created each time a new Deployment config is deployed, but it also keeps the old ReplicaSet.
       -         This allows you to easily roll back to the old state if something isn't quite working correctly.

* Deployment Controller usecase:
 Deployment Controllers and objects are higher-level constructs that were introduced to solve specific issues.
 - Pod management: Where running a ReplicaSet allows us to deploy a number of pods and check their status as a single unit.

 - Scaling a ReplicaSet: which scales out the pods and allows for the deployment to handle more traffic.
 -    Pod updates and role-backs: where the Deployment Controller allows updates to the PodTemplateSpec. This creates a new ReplicaSet and deploys a newer version of the pod. Also, if you don't like what you see in the newer version of the pod, just roll-back to the old ReplicaSet.
 - Pause and resume:
 Sometimes we have larger changesets or multiple updates that need to happen to a deployment.
   - In these scenarios, we can pause a deployment, make all the necessary updates, and then resume the deployment.
   -    Once the deployment is resumed, the new ReplicaSet will be started up and the deployment will update as expected.
   -         Please note that while a deployment is paused, it means that only updates are paused, but traffic will still get passed to the existing ReplicaSet as expected.
  - Status: Getting the deployment status is an easy way to check for the health of your pods and identify issues during a roll-out.
 * Replication Controller
   - You might have come across Replication Controllers if you search for Kubernetes controllers.This was an early implementation of ReplicaSets, but it has since been replaced by deployments and ReplicaSets, so in short, use deployments and ReplicaSets instead.

##### [DaemonSets](./DaemonSets.md)

##### Jobs
  - Job is basically a supervisor process for pods carrying out batch processes to completion. As the pod completes successfully, the job tracks information about the completion state of the pod. Jobs are used to run individual processes that need to run once and complete successfully. Typically, jobs are run as a cron job to run a specific process at a specific time and repeat at another time. You might use a cron job to run a nightly report or database backups, for example.

##### Services

A service provides network connectivity to one or more pods in your cluster.

When you create a service, it's designed a unique IP address that never changes through the lifetime of the service.

Pods are then configured to talk to the service and can rely on the service IP on any requests that might be sent to the pod.

Services are a really important concept because they allow one set of pods to communicate with another set of pods in an easy way.

It's a best practice to use a service when you're trying to get two deployments to talk to each other. That way, the pod in the first deployment always has an IP that they can communicate with regardless of whether the pod IPs in the second deployment changes.

![](images/services.png)

For example, when your front-end deployment needs to call a back-end deployment, you want to address the back-end with a service IP. Using the Backend Pod IP is a bad choice here because it can change over time and would wreak havoc for your application. A service provides an unchanging address so that the Frontend Pods can effectively talk to them at all times.

- There's a few kind of services that you can use.
  - Internal services: where an IP is only reachable from within the cluster, this is the cluster IP in Kubernetes speak
  - External services: where services running web servers, or publicly accessible pods, are exposed through an external endpoint. These endpoints are available on each node through a specific port. This is called a NodePort in Kubernetes speak.
  - Load balancer: This is for use cases when you want to expose your application to the public internet. It's only used when you are using Kubernetes in a cloud environment backed by a cloud provider such as AWS.
