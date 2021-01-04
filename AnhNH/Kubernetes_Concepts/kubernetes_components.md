# Kubernetes Components
 Khi ta triển khai Kubernetes, ta có một cluster.

 Một Kubernetes cluster bao gồm 1 set worker machine được gọi là nodes.

 Worker nodes host các Pods là Components của application workload. Control plane quản lý worker nodes và pods trong cluster. Trong môi trường production, Control Plane thường chạy trên multiple computer và một cluster thương chạy multiple nodes, cung cấp fault-tolerance và high availability(HA)

Biểu đồ bên dưới thể hiện một Kubernetes cluster với tất cả các Components kết nối với nhau:

![](images/kubernetes_c.png)

![](images/components.png)

### Control Plane Components
Control Plane Components đưa ra global decisions về cluster(ví dụ, scheduling) cũng như là phát hiện và phản hồi tới cluster events(ví dụ, khởi động pod mới khi một deployment's replicas field không đáp ứng được)

Control Plane Components có thể chạy trên bấy kỳ machine nào trong cluster. Tuy nhiên, để đơn giản hóa, khi setup scripts thường khở động tất cả control plane Components trên cùng một machine, và không được chạy user containers trên máy này.

Ví dụ về một [High-Availablity Clusters](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/) multi-master-VM setup

##### kube-apiserver
API server là một component của Kubernetes control plane(container orchestration layer that expose API and interfaces to define, deploy and manage lifecycle of containers)

Việc chính của Kubernetes API serverr là kube-apiserver. kube-apiserver được thiết kế để có thể scale horizontally, nó scale bằng cách kiển khai thêm các instance. Ta có thể chạy nhiều instances của kube-apiserver và cân bằng traffic giữa chúng
##### etcd
etcd là nơi để đảm bảo và tính sẵn sàng cao cho key-value store, được sử dụng như là Kubernetes' backing store cho tất cả cluster data.

Nếu Kubernetes cluster của bạn sử dụng etcd như là backing store, đảm bảo rằng ta có backup plan cho những data này

Tìm hiểu sâu hơn về [etcd](https://etcd.io/docs/)
##### kube-scheduler
![](images/sch.png)

La 1 control Plane componet đảm nhiệm việc phát hiện Pods mới được tạo với no assigned node, và chọn node cho chúng chạy trên đó.

Những yếu tố quyết định cho việc chọn scheduling:
* individual và collective resources requirements
* hardware/sofware/policy constraints
* affinity và anti-affinity specifications
* data locality
* inter-workload interrference và deadlines

##### kube-controller-manager
Control Plane Component đảm nhiệm việc chạy controller processes

Mỗi controller(In Kubernetes, controllers are control loops that watch the state of your cluster, then make or request changes where needed. Each controller tries to move the current cluster state closer to the desired state.) là một separate process, nhưng để giảm độ phức tạp, chúng được compiled thành một single binary và chạy trong một sigle process

Những controllers này bao gồm:
* Node controller: chịu trách nhiệm cho việc noticing và responding khi một node go down
* Replication controller: Chịu trách nhiệm cho việc maintaining correct number of pods cho mọi replication object trong hệ thống
* Endpoints controller: Populates the Endpoints object(joins Services and Pods)
* Service Account và Token controller: Tạo default accounts và API access tokens cho namespaces mới

##### cloud-controller-manager
Một Kubernetes control plane component cái mà được nhúng trong cloud-specific control logic. Cloud
### Node Components
Node Components chạy trên tất cả các node, duy trì việc chạy pods và cung cấp môi trường Kubernetes runtime
##### kubelet
Một agent chạy trên mỗi node trong cluster. nó đảm bảo rằng một container đang được chạy trong Pod.

kubelet lấy một set của PodSpecs cái mà được cung cấp thông qua nhiều cơ chế và đảm bảo thằng container được mo tả trong PodSpec running and healthy.

kubelet không quản lý containers mà không được tạo bởi Kubernetes.
##### kube-proxy
kube-proxy là một network proxy chạy trên mỗi node trong cluster, thực hiện một phần của Kubernetes Service.

[kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/) duy trì network rule trên nodes. Những network rules cho phép network communication tới Pods tư network sessions bên trong hoặc bên ngoài cluster.

kube-proxy sử dụng operating system packet-filtering layer nếu có và nó available. Nếu không có, kube-proxy sẽ tự nó forward traffic

##### Container runtime
Container runtime là phần mềm chịu trách nhiệm cho việc chạy các containers

Kubernetes hỗ trợ các container runtime như là : Docker, containerd, CRI-O, ...
### Addons
Addons sử dung Kubernetes resources(DaemonSet, Deployment, etc)
### DNS
Trong khi các addon không bắt buộc phải có, thế cả các cluster nên có [cluster-DNS](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/).

cluster DNS là một DNS server, server DNS records cho Kubernetes services.

Container khởi động bới Kubernetes tự động bao gồm DNS server trong DNS searches của chúng
### Container Resource Monitoring
[Container Resource Monitoring](https://kubernetes.io/docs/tasks/debug-application-cluster/resource-usage-monitoring/) records generic time-series metrics about containers in a central database, and provides a UI for browsing that data.
### Cluster-level Logging
A [cluster-level logging](https://kubernetes.io/docs/concepts/cluster-administration/logging/) mechanism is responsible for saving container logs to a central log store with search/browsing interface.
