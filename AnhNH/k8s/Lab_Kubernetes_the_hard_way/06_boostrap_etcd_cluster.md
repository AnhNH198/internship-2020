
Kubernetes component là stateless và lưu trữ  cluster state trong [etcd](https://github.com/etcd-io/etcd). Ta sẽ tạo 3 node etcd cluster và cấu hình nó HA và sercure remote access.

# Yêu cầu
câu lệnh sẽ chạy trên mỗi instance: controller, controller1 và controller2.

# Thực hiện trên các etc cluster member

Tải và cấu hình etcd từ etcd github project:
```
wget -q --show-progress --https-only --timestamping \
  "https://github.com/etcd-io/etcd/releases/download/v3.4.10/etcd-v3.4.10-linux-amd64.tar.gz"
```

giải nén và cài đặt etcd server và etcdctl
```
{
  tar -xvf etcd-v3.4.10-linux-amd64.tar.gz
  sudo mv etcd-v3.4.10-linux-amd64/etcd* /usr/local/bin/
}
```
Cấu hình etcd Server:
```
{
  sudo mkdir -p /etc/etcd /var/lib/etcd
  sudo chmod 700 /var/lib/etcd
  sudo cp ca.pem kubernetes-key.pem kubernetes.pem /etc/etcd/
}
```

địa chỉ internal sẽ được dùng để phục vụ request từ client và giao tiếp với etcd cluster peer.
```
INTERNAL_IP= dia chi ip cua con controller/etcd
```

Mỗi etcd member phải có tên riêng biết bên trong etcd cluster. Đặt etcd name trùng với tên host
```
ETCD_NAME=$(hostname -s)
```
mo port 2380:
```
firewall-cmd --zone=public --add-port=2380/tcp --permanent
```
Tạo etcd.service systemd unit file:
```
cat <<EOF | sudo tee /etc/systemd/system/etcd.service
[Unit]
Description=etcd
Documentation=https://github.com/coreos

[Service]
Type=notify
ExecStart=/usr/local/bin/etcd \\
  --name ${ETCD_NAME} \\
  --cert-file=/etc/etcd/kubernetes.pem \\
  --key-file=/etc/etcd/kubernetes-key.pem \\
  --peer-cert-file=/etc/etcd/kubernetes.pem \\
  --peer-key-file=/etc/etcd/kubernetes-key.pem \\
  --trusted-ca-file=/etc/etcd/ca.pem \\
  --peer-trusted-ca-file=/etc/etcd/ca.pem \\
  --peer-client-cert-auth \\
  --client-cert-auth \\
  --initial-advertise-peer-urls https://${INTERNAL_IP}:2380 \\
  --listen-peer-urls https://${INTERNAL_IP}:2380 \\
  --listen-client-urls https://${INTERNAL_IP}:2379,https://127.0.0.1:2379 \\
  --advertise-client-urls https://${INTERNAL_IP}:2379 \\
  --initial-cluster-token etcd-cluster-0 \\
  --initial-cluster controller=https://10.168.0.20:2380,controller1=https://10.168.0.21:2380,controller2=https://10.168.0.22:2380 \\
  --initial-cluster-state new \\
  --data-dir=/var/lib/etcd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF
```
* Phải cài đặt trên các controller/etcd khác:
# Verification
```
ETCDCTL_API=3 etcdctl member list \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/etcd/ca.pem \
  --cert=/etc/etcd/kubernetes.pem \
  --key=/etc/etcd/kubernetes-key.pem
```
output sample:
```
bdff55678130e0d, started, controller2, https://10.168.0.22:2380, https://10.168.0.22:2379, false
d271bd8745b282c6, started, controller, https://10.168.0.20:2380, https://10.168.0.20:2379, false
f0e68644655adc00, started, controller1, https://10.168.0.21:2380, https://10.168.0.21:2379, false
```
