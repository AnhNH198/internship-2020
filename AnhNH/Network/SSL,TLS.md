# SSL/TLS là gì?
Secure Sockets Layer (Lớp socket bảo mật). Một loại bảo mật giúp mã hóa liên lạc giữa website và trình duyệt.

Công nghệ này đang được thay thế hoàn toàn bởi TLS.
Transport Layer Security (TSL), nó cũng giúp bảo mật thông tin truyền giống như SSL.

Https là phần mở rộng bảo mật của http sử dụng ssl.
* TLS:
  - Bảo mật thông tin khi chuyển qua internet
  - Mã hóa thông tin khi truyền
  - Các website lớn đều sử dụng

* Cơ chế hoạt động của SSL/TLS:
  - Sử dụng 1 cặp khóa public và private key
  - Cặp khóa được sử dụng để tạo session key
  - session key được tạo và sử dụng trong 1 khoảng tgian nhất định và chỉ được dùng trong phiên giao dịch đó

* Tại sao cần dùng SSL/TLS:
  - Cần chứng thực
  - Tăng độ tin cậy với khách hàng
  - Tuân thủ tiêu chuẩn của ngành
