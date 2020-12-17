# Khởi tạo Data Encryption Config và Key
Kubernetes lưu trữ nhiều loaị data bao gồm cluster state, application configuration va secret. Kubernetes hỗ trợ [encrypt](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) cluster data at rest.

# Encryption Key
Khởi tạo encrytion key
```
ENCRYPTION_KEY=$(head -c 32 /dev/urandom | base64)

```
# Encryption Config File
tạo encryption-config.yaml configuration file:
```
cat > encryption-config.yaml <<EOF
kind: EncryptionConfig
apiVersion: v1
resources:
  - resources:
      - secrets
    providers:
      - aescbc:
          keys:
            - name: key1
              secret: ${ENCRYPTION_KEY}
      - identity: {}
EOF

```
 copy encrytion-config.yaml encryption config file tới mỗi controller instance:
```
for instance in controller controller1 controller2; do
  scp encryption-config.yaml root@${instance}:~/
done
```
* Những key này là cần thiết cho các etcd cluster(trong lab nay etcd nam trong controller)
* phải cài đặt trên các controller/etcd khác
