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

* Các đặc tính của pods:
   - Không thể tự self heal, nếu một Pods die, nó sẽ không được rescheduled
   - Không thể tự scale khi thiếu tài nguyên

 -> không nên trực tiếp sử dụng Pods,thay vào đó Sử dụng controller(deployment) để sử dụng pod.


* Pod có những trạng thái:
  - Pending: Pod đã được chấp nhận bởi Kubernetes system, nhưng container vẫn chưa được tạo.
  - Running: Pod đã được scheduled trên một node và tất cả container trong nó đã được tạo và ít nhất 1 container đang ở trạng thái running
  - Succeeded: Tất cả các Pod đã tra ve với một zero exit status, nghĩa là successful execution và không bị restart.
  - failed : Tất cả container trong Pod đã thoát và ít nhất một container failed và trả về non-zero exit status
  - CrashLoopBackOff: Container fail to start, vì lý do nào đó, khiến kubernetes lặp lại liên tục việc restart Pod.
  - Unknown: Không thể xác định state của pod
    - Thường do một network error có thể đã xảy ra(ví dụ node của pod đó đang chạy bị down)


* PodConditions:
  - PodScheduled: pod đã được scheduled tới một Node
  - Ready: pod đã có thể serve requests và sẽ được add tới matching Service
  - Initialized: quá trình initialization containers đã được started thành công
  - Unschedulable: Pod không thể được scheduled (Ví dụ vì lý do ràng buộc về tài nguyên (resources constraints))
  - ContainersReady: tất cả containers trong pod đó đều ở trạng thái ready
