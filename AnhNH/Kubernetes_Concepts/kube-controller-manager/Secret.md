# Secrets

* Secrets cung cấp cho Kubernetes một cách để phân phối credentials, keys, passwords hoặc "secret" data tới các pods
  - Kubernetes sử dụng Secrets để cung cấp credentials access tới internal API
  - Ta cũng có thể dùng cơ chế trên để cung cấp secret tới các applications
  - Secrets là một cách để cung cấp secrets, mặc định của Kubernetes
  - Vẫn có thể dùng cách khác để container có thể lấy secrets của nó(ví dụ sử dụng một external services khác)


* Secrets có thể được sử dụng theo cách:
  - Dùng secrets như environment variables
  - Dùng volumes mount secrets vào container
    - trong volumes này có file secret
  - có thể được sử dụng cho dotenv files hoặc app chỉ có thể đọc dotenv files


### tạo secrets sử dụng files
```
echo -n "root" > ./username.txt

echo -n "password" > ./password.txt

kubectl create secret generic db-user-pass --from-file=./username.txt —from-file=./password.txt

```
Output:
```
secret "db-user-pass" created
```

### Một secret cung có thể là một SSH key hoặc một SSL certificate
```
 kubectl create secret generic ssl-certificate --from-file=ssh-privatekey=~/.ssh/id_rsa --ssl-cert-=ssl-cert=mysslcert.crt
```

### Tạo secrets sử dụng yaml definitions
secrets-db-secret.yml
```
$ echo -n "root" | base64
cm9vdA==
$ echo -n "password" | base64
cGFzc3dvcmQ=
```
```
apiVersion: v1
kind: Secret
metadata:
 name: db-secret
type: Opaque
data:
 password: cm9vdA==
 username: cGFzc3dvcmQ=
```
password và username được mã hóa ở dạng base64
* Sau khi tạo yml file, dùng câu lệnh kubectl create:
```
kubectl create -f secrets-db-secret.yml
```

### Sử dụng secret
Ta có thể tạo một pod, dùng secret như một environment variables
```
apiVersion: v1
kind: Pod
metadata:
 name: nodehelloworld.example.com
 labels:
 app: helloworld
spec:
 containers:
 - name: k8s-demo
 image: wardviaene/k8s-demo
 ports:
 - containerPort: 3000
 **env:
 - name: SECRET_USERNAME
 valueFrom:
 secretKeyRef:
 name: db-secret
 key: username
 - name: SECRET_PASSWORD
 […]**
```

Một cách khác, ta có thể cung cấp secret bên trong 1 file:
```
apiVersion: v1
kind: Pod
metadata:
 name: nodehelloworld.example.com
 labels:
 app: helloworld
spec:
 containers:
 - name: k8s-demo
 image: wardviaene/k8s-demo
 ports:
 - containerPort: 3000
 **volumeMounts:
 - name: credvolume
 mountPath: /etc/creds
 readOnly: true
 volumes:
 - name: credvolume
 secret:
 secretName: db-secrets**
```
* secrets sẽ được lưu lại tại:
 - /etc/creds/db-secrets/username
 - /etc/creds/db-secrets/password
