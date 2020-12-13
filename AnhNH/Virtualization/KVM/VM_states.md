# Các trạng thái thông báo của VMs
1. running – máy ảo đang chạy
2. idle – máy ảo đang rảnh, không chạy và cũng không thể  chạy. Có thể bởi vì máy ảo đang đợi IO hoặc đã vào trạng thái ngủ vì không hoạt động
3. paused - máu ảo đã bị pause, thường là do admin chạy lệnh virsh suspend. Khi ở trạng thái pause, máy ảo vẫn tiêu thụ tài nguyên bộ nhớ nhưng sẽ không được schedule bới hypervisor
4. in shutdown - máy ảo đang trong tiến trình tắt
5. shut off - máy ảo không chạy, thường là do máy ảo bị tắt.
6. crashed - máy ảo bị crash, có khả năng bị tắt cứng. Trạng thái này thường xảy ra khi máy ảo được cấu hình không khởi động lại khi bị crash.
7. pmsuspended - máy ảo bị suspend bởi power management của máy host ví dụ vào s3 State
