# virt-install
### Ví dụ sử dụng câu lệnh để cài đặt một máy ảo:
```
virt-install –n test –description "this is a test vm" --os-type=Linux –os-variant=centos7.0 --ram=512 –vcpus=2 –disk path=/create/new/disk/test.qcow2,bus=virtio,size=5 –cdrom /iso/to/install.iso --network network=NAT
```
### Chi tiết các parameter được sử dụng trong câu lệnh
n: đặt tên máy ảo của bạn

description: mô tả máy ảo của bạn, ví dụ: application server, database server, web server, …

os-type: OS type có thể là Linux, Solaris, Unix, Windows.

Os-variant: Loại distribution (có thể dùng câu lệnh để tra) osinfo-query os
vcpus: số cpu cho máy ảo

disk path=/var/lib/libvirt/images/myRHELVM1.qcow2,bus=virtio,size=10 Path where the VM image files is stored. Size in GB. In this example, this VM image file is 10GB. 

Cdrom: chỉ ra đường dẫn của image cài đặt. Ta cũng có thể chỉ ra NFS hoặc http installation location thay vì -cdrom. Ví dụ, –location=http://.com/pub/rhel6/x86_64/ 

networks: chọn networks cho máy ảo
