# Bootstrapping Kubernetes Control Plane
Tạo thư mục Kubernetes configuration
```
sudo mkdir -p /etc/kubernetes/config

```
Tải và cài đặt Kubernetes Controller Binaries
```
wget -q --show-progress --https-only --timestamping \
  "https://storage.googleapis.com/kubernetes-release/release/v1.18.6/bin/linux/amd64/kube-apiserver" \
  "https://storage.googleapis.com/kubernetes-release/release/v1.18.6/bin/linux/amd64/kube-controller-manager" \
  "https://storage.googleapis.com/kubernetes-release/release/v1.18.6/bin/linux/amd64/kube-scheduler" \
  "https://storage.googleapis.com/kubernetes-release/release/v1.18.6/bin/linux/amd64/kubectl"
```
Cài đặt Kubernetes Binaries
```
{
  chmod +x kube-apiserver kube-controller-manager kube-scheduler kubectl
  sudo mv kube-apiserver kube-controller-manager kube-scheduler kubectl /usr/local/bin/
}
```
Cấu hình Kubernetes API server
```
{
  sudo mkdir -p /var/lib/kubernetes/

  sudo mv ca.pem ca-key.pem kubernetes-key.pem kubernetes.pem \
    service-account-key.pem service-account.pem \
    encryption-config.yaml /var/lib/kubernetes/
}
```
Internal IP address sẽ được sử dụng để quảng bá API Server tới member của cluster.
```
```
tạo kube-apiserver.services
```

```
Cấu hình Kubernetes Controller manager
move kube-controller-manager kubconfig vào place:
```
```

Tạo kube-controller-manager.service systemd unit file:
```
```
Cấu hình Kubernetes scheduler
move kube-scheduler kubeconfig vào place
```
```
Tạo kube-scheduler.yaml configuration file
```
```

tạo kube-scheduler.service systemd unit file
```

```
khởi động controller service

### RBAC cho kubelet authorization
```
```
