# Secrets

* Secrets cung cấp cho Kubernetes một cách để phân phối credentials, keys, passwords hoặc "secret" data tới các pods
  - Kubernetes sử dụng Secrets để cung cấp credentials access tới internal API
  - Ta cũng có thể dùng cơ chế trên để cung cấp secret tới các applications
  - Secrets là một cách để cung cấp secrets, mặc định của Kubernetes
  - Vẫn có thể dùng cách khác để container có thể lấy secrets của nó(ví dụ sử dụng một external services khác)


* Secrets có thể được sử dụng để:
  - Dùng secrets như environment variables
  - Dùng secrets như một file trong một pod
    - setup
