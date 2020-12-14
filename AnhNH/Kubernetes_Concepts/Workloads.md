# Workloads
Một workload là một application chạy trên Kubernetes. Workload là một single component hay một vài component làm việc cùng nhau, trên Kubernetes ta chạy nó bên trong 1 set của Pods. Trong Kubernetes, một Pod tái hiện 1 set of running container trên cluster.

Một Pod có một defined lifecycle. Ví dụ, một khi một Pod đang chạy trong cluster thì bị critical failure trên node nơi mà Pod đó đang chạy thì tất cả Pods trên node đó fail. Kubernetes coi cấp độ đó như là final: bạn cần phải tạo Pod mới ngay cả khi nếu node cũ có thể recover lại.

Tuy nhiên, để cho life considerably easier, bạn không cần phải quản lý mỗi Pod trực tiếp. Thay vào đó, ban có thể sử dụng workload resource có thể quản lý một set của Pods thay bạn. Những tài nguyên này cấu hình controllers đảm bảo right number of the right kind of Pod are running, để match state ta specified.
Those workload resources include:
* [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) and [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) (thay thế legacy resource ReplicationController)
* [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
* [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)
* [job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) và [Cronjob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)
* [Garbage collection](https://kubernetes.io/docs/concepts/workloads/controllers/garbage-collection/)
* [time-to-live after finished controller](https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished/) removes Jobs once a defined time has passed since they completed.
