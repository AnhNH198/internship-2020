# DaemonSet trong Kubernetes là gì ?
![](images/DaemonSets2.png)

DaemonSet là một dạng dịch vụ quản lý các Pod hoạt động với chức năng khá là riêng biệt bằng cách đảm bảo Pod dịch vụ sẽ được chạy trên toàn bộ các Node trong một Kubernetes Cluster (hoặc trên một số Node cụ thể trong Kubernetes Cluster).

DaemonSet sử dụng Pod template, để định nghĩa các thông số cho pod dịch vụ mà bạn sẽ chạy như : sử dụng image gì, volume gì được mount, label, selectors,…

Khi mà bạn thêm một node mới vào Kubernetes Cluster, thì DaemonSet pod sẽ được tự động add vào node mới đó. Cũng tương tự ở chiều ngược lại, khi bạn xoá một node khỏi Kubernetes Cluster thì pod đó sẽ được xoá khỏi hệ thống Kubernetes.

![DaemonSets](images/DaemonSets.png)

Khi bạn xoá một DaemonSet đang chạy, thì đồng nghĩa bạn xoá tất cả các DaemonSet Pod đang tồn tại.

# Sử dụng DaemonSet trong trường hợp nào ?
Các trường hợp ứng dụng thực tế phổ biến mà ta sẽ chạy dịch vụ ở dạng DaemonSet. :
 - Chạy dịch vụ để kết nối cluster storage ở mỗi Kubernetes Node như : glusterd, glusterfs, ceph,..
 -    Chạy dịch vụ để thu thập log (log container hoặc log os node) ở mỗi Kubernetes Node như : fluentd, logstash, datadog agent,..
 -       Chạy dịch vụ để giám sát hệ thống node ở mỗi Kubernetes Node như : prometheus node exporter, collectd, datadog agent, newrelic agent..

Nhìn chung thì ba trường hợp trên là ứng dụng thực tế phổ biến nhất đối với DaemonSet trong Kubernetes. Trong những hạ tầng công ty khác nhau, sẽ luôn có những nhu cầu đặc biệt ứng dụng mục đích khác nhau khi triển khai dịch vụ DaemonSet Kubernetes.

Bạn có thể chạy nhiều dịch vụ DaemonSet trong cùng một Node đấy, mỗi DaemonSet có thể đảm nhận chức năng khác nhau dù cùng một source ứng dụng.

# Giao tiếp với DaemonSet như thế nào ?
* DaemonSet cũng chỉ là dịch vụ Pod chạy trên mỗi Node nên cách thức nói chuyện cũng sẽ quen thuộc như sau :
 - Push: ở cơ chế Push, thì các DaemonSet Pod thường được cấu hình để tự động thu thập dữ liệu và đẩy về 1 dịch vụ cố định. Nên cũng không có nhu cầu client nào giao tiếp hết.

  - NodeIP và known port: giống như khi deploy Prometheus Node Exporter, bạn sẽ cho DaemonSet Pods sử dụng hostPort và port IP cụ thể trên mỗi Node. Như vậy khi các service discovery sẽ lấy danh sách Kubernetes Node và giao tiếp với DaemonSet qua port mà bạn cấu hình.
  - DNS: bạn cũng có thể giao tiếp với DaemonSet qua DNS endpoint.
    Service: bạn cũng có thể cấu Service cho DaemonSet, từ đó client khi truy cập DaemonSet qua Service sẽ truy cập ngẫu nhiên một DaemonSet Pod trên ngẫu nhiên Node.

-> Với DaemonSet, người ta hay cấu hình dịch vụ thu thập log tự động hoặc sử dụng NodeIP & Port như Prometheus Node Exporter hoac monitor.
