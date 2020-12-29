# Ta nên chọn CA như thế nào?
Nó khá quan trọng khi chọn Certification Authority phù hợp. Ta nên chọn CA có danh tiếng và độ uy tín cao.

# CSR là gì
CSR hay Certificate Signing Request là một khối dữ liệu được mã hóa, cái mà được tạo ra trên server và được sử dụng. Nó chứa đựng thông tin cần thiết cho việc khởi tạo chứng chỉ như tên tổ chức Organization name, common name(domain name), locality, và country. Nó cũng chứa public key cái mà sẽ được bao gồm trong certificate của bạn. Một private key thường được tạo ra cùng với thời điểm bạn tạo CSR

# Tại sao chúng ta cần một CSR
Một Certificate Authority có thể sử dụng một CSR để tạo chứng chỉ SSL nhưng ho không cần private key của bạn. Ban cần phải giữ private key bí mật. Chứng chỉ được tạo váo CSR cụ thể sẽ chỉ làm việc với private key được tạo ra cùng với nó. Nếu bạn làm mất private key, chứng chỉ của bạn không còn tác  dụng
# Chi tiết nội dung bên trong 1 CSR
Common Name (CN): The fully qualified domain name (FQDN) of your server

Organization (O): Tên hợp pháp của tổ chức của bạn

Organizational Unit (OU): The division of your organization handling the
certificate.

City/Locality (L): Thành phố mà tổ chức của bạn đang hoạt động

State(S): Bang mà tổ chức của bạn đang hoạt động.

Country (C): Mã code đất nước của bạn.

Email address: Địa chỉ email làm việc với công ty của bạn.

Public Key: The public key that will go into the certificate.

# Format của một CSR
phần lớn CSRs được tạo ở định dạng Base64 encoded PEM format. Format này bao gồm

“——–BEGIN CERTIFICATE REQUEST——–” và

 “——–END CERTIFICATE REQUEST——–”

ở đầu và cuối CSR.

# Những vấn đề nên tập trung:


    • Bảo vệ Private Key
      Su dung chung chi tu nha cung cap dang tin cay
    • Đảm bảo chứng chỉ không bị hết hạn
    • Ensure Domain Name Coverage
    • Ensure Certificate Chain – some CAs provide such a utility
    • Make sure you are using the most current version of your server distribution and the most current SSL library.
    • Disable SSL v2
    • xem xét disabling SSL v.3.1
    • Don’t serve mixed HTTP and HTTPS content
    • Disable Insecure Renegetotiation
    • Use persistent connections
    • Mã hóa 100% traffic của bạn
    • Đảm bảo secure cookies được sử dụng
    • Sử dụng do-not-cache http header cho dữ liệu nhạy cảm
    • Sử dụng Secure Protocols và Cipher-Suites
    • Enable Session Resumption
    • Implement HSTS

# Một số ví dụ
Apache SSLProtocol -ALL +SSLv3 +TLSv1 SSLCipherSuite ECDHE-RSA-AES128-SHA256:AES128-GCM-SHA256:RC4:HIGH:!MD5:!aNULL:!EDH SSLHonorCipherOrder on

Nginx ssl_protocols SSLv3 TLSv1 TLSv1.1 TLSv1.2; ssl_ciphers ECDHE-RSA-AES128-SHA256:AES128-GCM-SHA256:RC4:HIGH:!MD5:!aNULL:!EDH; ssl_prefer_server_ciphers on;
