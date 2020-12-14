One important thing to note is that this Node can be a physical computer or a virtual machine. The Node has the following requirements. Each Node must have a Kubelet running, container tooling, like Docker, a kube-proxy process running, and a process like Supervisord, so it can restart components. I'll go over more details of the specifics of these components in a later section. One thing to note is that if you're using Kubernetes in a production like setting, it's recommended that you have at least a three Node cluster.

For this course, we will use Minikube, which is a tool run Kubernetes locally. It's a lightweight Kubernetes implementation that creates a virtual machine, on your local box, and deploys a simple cluster containing of one single Node. Your applications run on Nodes, so let's take a look at the most basic construct needed to build a Kubernetes app. This is called a Pod. In the Kubernetes model, a Pod is the simplest unit that you can interact with. You can create, deploy, and delete Pods, and it represents one running process in your cluster.

A Pod contains the following things. Your Docker application container, storage resources, a unique network IP, and options that govern how the container should run. In some scenarios, you can have multiple docker containers running in a Pod, but a Pod represents one single unit of deployment, a single instance of an application in Kubernetes that's tightly coupled and shares resources. Pods are designed to be ephemeral, disposable entities. I never create Pods just by themselves in a production application.

I only do that when I need to test whether the underlying containers actually work. Pods also don't self-heal. If a Pod dies, for some reason, it will not be rescheduled. Also, if a Pod is exited from a Node because of lack of resources, it will not be restarted on different healthier Nodes. There are higher level constructs to manage and add stability to Pods, called controllers. So pro-tip, don't use a Pod directly. Use a controller instead, like a deployment. Through its life-cycle, a Pod has the following states.

Pending, which means that the Pod has been accepted by the Kubernete system, but a container has not been created yet. Running, where a Pod has been scheduled on a Node, and all of its containers are created, and at least one container is in a running state. Succeeded, which means that all the containers in the Pod have exited with an exit stat of zero, which indicates successful execution, and will not be restarted. A failed state, which means all the containers in the Pod have exited and at least one container has failed and returned a non-zero exit status.

Or, my favorite, which is the CrashLoopBackOff. This is where a container fails to start, for some reason, and then Kubernetes tries over and over and over again to restart the Pod. Now that we've discussed two basic concepts, Nodes and Pods, in the next video, we'll build on these concepts and talk about deployments, replicacets, and services.
### Nodes
Node có thể là physical computer hoặc một máy ảo.
* Một Node có nhưng yêu cầu:
 - Mỗi node phải có một kubelet running
 - Phải có container tooling(Docker, ...)
 - kube-proxy running
 - process like supervisord, nó có thể restart components

 ### Pods

 Pods đại diện 1 running process bên trong cluster

* Một pod bao gồm những thứ sau:
   - Docker application container
   - Storage resources
   - unique network IP
   - option chỉ ra container nên chạy như thế nào (options that govern how the container should run)

 Ta có thể có nhiều containers chạy trong 1 pods, nhưng một Pods đại diện cho chỉ một unit of deployment.

* các đặc tính của pods:
 - không thể tự self heal, nếu một Pods die, nó sẽ không được rescheduled
 - không thể tự scale khi thiếu tài nguyên

 -> không nên trực tiếp sử dụng Pods,thay vào đó Sử dụng controller(deployment) để sử dụng pod.


* Pod có những trạng thái:
  - Pending: Pod đã được chấp nhận bởi Kubernetes system, nhưng container vẫn chưa được tạo.
  - Running: Pod đã được scheduled trên một node và tất cả container trong nó đã được tạo và ít nhất 1 container đang ở trạng thái running
  - Scceeded: Tất cả các Pod đã thoát với một zero exit status, nghĩa là successful execution và không bị restart.
  - failed : Tất cả container trong Pod đã thoát và ít nhất một container failed và trả về non-zero exit status
  - CrashLoopBackOff: Container fail to start, vì lý do nào đó, khiến kubernetes lặp lại liên tục việc restart Pod.
