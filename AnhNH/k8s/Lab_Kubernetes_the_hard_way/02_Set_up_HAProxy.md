# Setup ha-proxy
yum install -y haproxy net-tools

netstat -nltp: kiểm tra  dịch vụ đang sử  dung

### Cấu hình HA proxy
nano /etc/haproxy/haproxy.cfg

```
frontend k8s
  bind 10.168.0.200:6443
  node tcp
  default_backend k8s

backend k8s
  balance roundrobin
  node tcp
  option tcplog
  option tcp-check
  server controller 10.168.0.20:6443 check
  server controller1 10.168.0.21:6443 check
  server controller2 10.168.0.22:6443 check

```

* bind 10.168.0.200:6443, 6443 là port API Server sử dụng, vậy nên khi kết nối tới port 6443 load balancer sẽ tự chuyển đến port các API Server
* default_backend: backend mặc định là k8s
* balance roundrobin: balancer phát gói tin luân phiên từ controller 0 – 1 – 2 rồi lặp lại 0 - 1 – 2

Trong trường hợp haproxy không thể bind address
```
setsebool -P haproxy_connect_any=1
```
