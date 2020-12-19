# Kubernetes API
Core của Kubernetes's control plane là API server.

API server mở một HTTP API cho phép end uers, different part of your cluster và external components giao tiếp với one another.

Kubernetes API cho phép bạn  query and manipulate trạng thái của objects trong Kubernetes API(ví dụ Pods, namespaces, ConfigMaps và Events)

Phần lơn operations có thê được thực hiện qua kubectl command-line interface hoặc command line tool khác nhưu là kubeadm. Tuy nhiên, ta cũng có thể access API trực tiếp sử dụng REST calls.

Xem xet sử dụng một trong [client-libraries](https://kubernetes.io/docs/reference/using-api/client-libraries/) nếu đang viết một app sử dụng Kubernetes API
