<p>
Nhiều ứng dụng yêu cầu môi trường mạng xác định cho các mục tiêu về bảo mật hoặc đảm bảo chức năng. Chức năng mạng native của Docker có phần bị hạn chế trong các tình huống này. Vì lý do đó, có nhiều chương trình đã được tạo ra để mở rộng hệ sinh thái mạng Docker.</p>

# Overlay Network
Tạo các overlay network để phân tách (abstract) cấu trúc liên kết cơ bản.
Thiết lập các overlay network giúp cải tiến phần hạn chế.

Overlay network là mạng ảo được xây dựng trên các kết nối mạng hiện có. Thiết lập overlay network cho phép tạo một môi trường mạng dễ dự đoán và thống nhất hơn trên các máy chủ. Điều này giúp đơn giản hóa việc kết nối giữa các container, mà không cần quan tâm đến vị trí đang chạy các container.

Một mạng đơn ảo có thể nối nhiều máy chủ hoặc các subnet xác định, có thể được chỉ định cho mỗi máy chủ trong một mạng hợp nhất.

Một ứng dụng khác của overlay network là xây dựng cấu trúc các cụm máy tính (computing cluster). Trong cấu trúc tính toán (fabric computing), nhiều máy chủ được tách ra và quản lý như một thực thể duy nhất và mạnh mẽ hơn.

Việc triển khai một lớp cấu trúc tính toán cho phép người dùng cuối quản lý cluster như một tổng thể thay vì các máy chủ riêng lẻ. Kết nối đóng vai trò lớn trong mô hình cụm này.
