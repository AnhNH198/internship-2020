# Cấu hình / cài đặt TSL certificates cho cluster:
trước khi cấu hình các dịch vụ trên các nodes, chúng ta cần tạo chứng chỉ SSL/TLS, cái mà sẽ được sử dụng bởi kubernetes components.

Ví dụ này sẽ setup một certificates đơn lẻ, nhưng trong triển khai thực tế chúng ta nên tạo chứng chỉ riêng biệt cho mỗi component/service.

* Chúng ta cần bảo mật những components:
  - admin user (used to interact with cluster)
  - kubelet (run on each worker node)
  - kube-controller-manager
  - kube-proxy
  - kube-scheduler
  - Kubernetes API Server
  - service account

Ta sẽ sử dụng CFSSL để tạo những chứng chỉ này:

```
Linux:
wget https://pkg.cfssl.org/R1.2/cfssl_linux-amd64
chmod +x cfssl_linux-amd64
sudo mv cfssl_linux-amd64 /usr/local/bin/cfssl

wget https://pkg.cfssl.org/R1.2/cfssljson_linux-amd64
chmod +x cfssljson_linux-amd64
sudo mv cfssljson_linux-amd64 /usr/local/bin/cfssljson

```
### Tạo CA CSR config file:

```
echo '{
  "signing": {
    "default":{
      "expiry": "8998h"
    },
    "profiles":{
      "kubernetes": {
        "usages": ["signing", "key encipherment", "server auth", "client auth"],
        "expiry": "8998h"
      }
    }
  }
  }' > ca-config.json
```

### Tạo CA certificates và CA private key:
```
echo '{
  "CN": "kubernetes",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "VN",
      "L": "HaNoi",
      "O": "VCCorp",
      "OU": "Kubernetes The Hard Way",
      "ST": "Vietnam"
    }
  ]
  }' > ca-csr.json
```
```
cfssl gencert -initca ca-csr.json | cfssljson -bare ca
```

Sau khi tạo chứng chỉ ta sẽ có 3 file:
* ca.pem
* ca.csr
* ca-key.pem

ca.pem là CA certificate <br>
ca-key.pem là CA-certificate’s private key<br>
ca.csr là chứng chỉ ký cho certificate

Ta có thể xác thực rằng ta có certificate bằng cách sử dụng command
```
openssl x509 -in ca.pem -text -noout
```

### Tạo admin client certificate và private key
```
{

cat > admin-csr.json <<EOF
{
  "CN": "admin",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "VN",
      "L": "HaNoi",
      "O": "VCCorp",
      "OU": "Kubernetes The Hard Way",
      "ST": "Vietnam"
    }
  ]
}
EOF

cfssl gencert \
  -ca=ca.pem \
  -ca-key=ca-key.pem \
  -config=ca-config.json \
  -profile=kubernetes \
  admin-csr.json | cfssljson -bare admin

}
```

#### Tạo chứng chỉ cho kubelet client
```
for instance in worker worker1 worker2; do
cat > ${instance}-csr.json <<EOF
{
  "CN": "system:node:${instance}",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "VN",
      "L": "HaNoi",
      "O": "VCCorp",
      "OU": "Kubernetes The Hard Way",
      "ST": "Vietnam"
    }
  ]
}
EOF

EXTERNAL_IP=$(nslookup {$instance} | grep Address | tail -1 | awk '{print $2}'
)

cfssl gencert \
  -ca=ca.pem \
  -ca-key=ca-key.pem \
  -config=ca-config.json \
  -hostname=${instance},${EXTERNAL_IP} \
  -profile=kubernetes \
  ${instance}-csr.json | cfssljson -bare ${instance}
done
```

#### Tạo chứng chỉ cho kube-control-manager client và private key
```
{

cat > kube-controller-manager-csr.json <<EOF
{
  "CN": "system:kube-controller-manager",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "VN",
      "L": "HaNoi",
      "O": "VCCorp",
      "OU": "Kubernetes The Hard Way",
      "ST": "Vietnam"
    }
  ]
}
EOF

cfssl gencert \
  -ca=ca.pem \
  -ca-key=ca-key.pem \
  -config=ca-config.json \
  -profile=kubernetes \
  kube-controller-manager-csr.json | cfssljson -bare kube-controller-manager

}
```
#### Tạo chứng chỉ kube-proxy client và private key
```
{

cat > kube-proxy-csr.json <<EOF
{
  "CN": "system:kube-proxy",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "VN",
      "L": "HaNoi",
      "O": "VCCorp",
      "OU": "Kubernetes The Hard Way",
      "ST": "Vietnam"
    }
  ]
}
EOF

cfssl gencert \
  -ca=ca.pem \
  -ca-key=ca-key.pem \
  -config=ca-config.json \
  -profile=kubernetes \
  kube-proxy-csr.json | cfssljson -bare kube-proxy

}

```
#### Tạo chứng chỉ cho kube-scheduler client và private key:
```
{

cat > kube-scheduler-csr.json <<EOF
{
  "CN": "system:kube-scheduler",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "VN",
      "L": "HaNoi",
      "O": "VCCorp",
      "OU": "Kubernetes The Hard Way",
      "ST": "Vietnam"
    }
  ]
}
EOF

cfssl gencert \
  -ca=ca.pem \
  -ca-key=ca-key.pem \
  -config=ca-config.json \
  -profile=kubernetes \
  kube-scheduler-csr.json | cfssljson -bare kube-scheduler

}
```
#### Tạo chứng chỉ Kubernetes API Server và private key
```
{

KUBERNETES_PUBLIC_ADDRESS=10.168.0.200

KUBERNETES_HOSTNAMES=kubernetes,kubernetes.default,kubernetes.default.svc,kubernetes.default.svc.cluster,kubernetes.svc.cluster.local

cat > kubernetes-csr.json <<EOF
{
  "CN": "kubernetes",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "VN",
      "L": "HaNoi",
      "O": "VCCorp",
      "OU": "Kubernetes The Hard Way",
      "ST": "Vietnam"
    }
  ]
}
EOF

cfssl gencert \
  -ca=ca.pem \
  -ca-key=ca-key.pem \
  -config=ca-config.json \
  -hostname=10.168.0.20,10.168.0.21,10.168.0.22,${KUBERNETES_PUBLIC_ADDRESS},127.0.0.1,${KUBERNETES_HOSTNAMES} \
  -profile=kubernetes \
  kubernetes-csr.json | cfssljson -bare kubernetes

}
```
#### Service Account Key Pair
Kubernetes Controller Manager sử dụng cặp key pair để tạo và ký service account token, xem chi tiết thêm tại [managing service accounts](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/)
```
{

cat > service-account-csr.json <<EOF
{
  "CN": "service-accounts",
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "VN",
      "L": "HaNoi",
      "O": "VCCorp",
      "OU": "Kubernetes The Hard Way",
      "ST": "Vietnam"
    }
  ]
}
EOF

cfssl gencert \
  -ca=ca.pem \
  -ca-key=ca-key.pem \
  -config=ca-config.json \
  -profile=kubernetes \
  service-account-csr.json | cfssljson -bare service-account

}
```
#### Phân phối Client và Server Certificates
Cho Workers:
```
for instance in worker worker1 worker2; do
  scp ca.pem ${instance}-key.pem ${instance}.pem root@${instance}:~/
done
```
Cho controllers:
```
for instance in controller controller1 controller2; do
  scp ca.pem ca-key.pem kubernetes-key.pem kubernetes.pem \
    service-account-key.pem service-account.pem root@${instance}:~/
done
```
