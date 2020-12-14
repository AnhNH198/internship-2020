# Networking
#### Kubernetes sử dụng 3 loại networks:
<ol>
  <li>Infrastructure Network: </li>
  <p>Network mà máy vật lý của bạn kết nối tới, thường là production network của bạn hoặc 1 phần của nó</p>
  <li>Service Network: </li>
  <p>Hoàn toàn) Network ảo hóa, cái mà được sử dụng để gán IP addresses tới các dịch vụ Kubernetes. (Một dịch vụ là một frontend tới 1 RC hoặc 1 Deployment). một điều cần phải chú trọng răng IP từ network này không bao giờ được gán tới bất kỳ nodes/VMs nào. Những Services IPs được sử dụng behind the scenes bới kube-proxy dể tạo (weird) iptables rules trên worker nodes</p>
  <li>Pod Network: </li>
  <p>Network này được sử dụng bởi pods. Dựa trên kiểu kubernetes network solution nào bạn đang sử dụng. Nếu bạn đang sử dụng chương trình flannel, thì đó sẽ là một mạng luới phần mềm lớn với overlay network, và mỗi worker node sẽ có một subnet của mạng đó và được cấu hình cho docker0 interface của nó. <p>
  <p>Nếu bạn đang triển khai CIDR network, sử dụng CNI, thì nó sẽ là mạng lưới lớn sử dụng cluster-cidr, với những subnet nhỏ phù hợp với những worker nodes. Bảng đinh tuyến của router quản lý phần của infrastructure networks sẽ cần được cập nhật với route tới những subnet nhỏ.</p>
</ol>

{>>flannel, overlay network, CIDR network, cluster-cidr<<}
