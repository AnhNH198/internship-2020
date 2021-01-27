# Replication Set
Repication Set là thế hệ tiếp theo của Replication Controller
* Nó hỗ trợ selector mới, có thể tạo các selection dựa trên filtering theo một set of values
  * Ví dụ: ta có thể chọn nhiều selector "environment" vừa là 'dev' hoặc vừa là 'qa'
  * Không chỉ dùng mỗi based on equality như Replication Controller ("environment" == "dev"), Replication Set có thể làm được các selector phức tạp hơn
* Replicaset được sử dụng bởi Deployment object

# Deployments

* Deployment trong Kubernets cho phép ta thực hiện app deployments và updates
* Khi sử dụng deployment object, ta có thể define state của application
  * Kubernets sẽ đảm bảo rằng cluster match đúng trạng thái mà ta define

-> Nếu chỉ sử dụng Repication Controller hoặc Replication set rất là phức tạp khi deploy apps (không có khả năng tự động hóa các task)
  * Deployments Object giúp ta deploy dễ dàng và cung cấp nhiều khả năng hơn

### Deployment cung cấp
* Tạo một deployment (ví dụ deploying một app)
* update một deployment (ví dụ deploy một version mới)
* rolling updates (zero down time deployment, ta sẽ không update toàn bộ app mà ta sẽ update từng bước 1, không làm down hệ thống)
* roll back to a previous version
* Pause / Resume (roll-out to only a certain percentage)

### Ví dụ về một deployments

```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
 name: helloworld-deployment
spec:
 replicas: 3
 template:
 metadata:
 labels:
 app: helloworld
 spec:
 containers:
 - name: k8s-test
 image: wardviaene/k8s-demo
 ports:
 - containerPort: 3090
```
Command  | Mô tả
--|--
kubectl get deployments  | Lấy thông tin về các Deployments hiện tại
kubectl get rs  |  lấy thông tin về replica sets
kubectl get pods --show-labels  |  get pod, show label của pod đó
kubectl rollout status deployment/helloworld-deployment  | Lấy status của deployment helloworld-deployment
kubectl set image deployment/helloworld-deployment k8s-demo=k8s-demo:2  | Chạy k8s-demo với image label version 2
kubectl edit deployment/helloworld  |  Sửa Deployment
kubectl rollout history deployment/helloworld-deployment  |  Lịch sử rollout
kubectl rollout undo deployment/helloworld-deployment | rollback về version trước
kubectl rollout undo deployment/helloworld-deployment --to-revision=n |  rollback về version cụ thể mà ta set
