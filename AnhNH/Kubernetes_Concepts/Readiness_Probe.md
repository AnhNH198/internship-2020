# Readiness Probe
Bên cạnh livenessProbes, ta cũng có thể sử dụng readinessProbes trên container bên trong một Pod

* livenessProbes: xác định xem liệu một container đang running hay không
  - Nếu check fail, container sẽ bị restart


* readinessProbes: xác định xem liệu một container có ready to serve requests hay không
  - Nếu check fail, container sẽ không bị restarted, nhưng Pod's IP address sẽ bị removed khỏi Service, nó sẽ không phục vụ bất kỳ requests nào nữa

* readinessProbes test sẽ đảm bảo at startup, pod chỉ nhận traffic khi test succeed.
* Ta có thể kết hợp dùng cả 2 test, cấu hình cả livenessProbe và readinessProbe
* Nếu container luôn luôn tự thoát khi gặp lỗi, ta không cần cấu hình livenessProbes
