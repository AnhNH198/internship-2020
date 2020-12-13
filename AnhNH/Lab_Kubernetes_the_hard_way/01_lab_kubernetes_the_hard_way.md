# Lab bao gồm:
1. 1 x Load Balancer (HA Proxy)
2. 3 x Kubernetes controller nodes + etcd
3. 3 x Kubernetes worker nodes
4. SSL dựa trên truyền thông giữa các thành phần của Kubernetes
5. Internal Cluster DNS (SkyDNS)
6. Default Services account và Secrets

# Các VMs được sử dụng
1. controller + etcd 1024 MB RAM 10 GB disk 10.168.0.20/24
2. controller1 + etcd 1024 MB RAM 10 GB disk 10.168.0.21/24
3. controller2 + etcd 1024 MB RAM 10 GB disk 10.168.0.22/24
4. worker1 1024 MB RAM 20 GB disk 10.168.0.31/24
5. worker2 1024 MB RAM 20 GB disk 10.168.0.32/24
6. worker3 1024 MB RAM 20 GB disk 10.168.0.33/24
7. ha(Load Balancer) 10.168.0.200/24
