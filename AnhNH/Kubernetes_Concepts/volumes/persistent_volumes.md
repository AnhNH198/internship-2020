# Persistent Volume

![](images/ps.png)

Now when we have a large environment with a lot of users deploying a lot of pods the users would have to configure storage every time for each pod. 

Whatever storage solution is used the users who deploys the pods would have to configure that on all pod definition files in his own environment every time it changes to be made the user would have to make them on all of his pods.



![](images/ps1.png)

-> Instead you would like to manage storage more centrally. You would like it to be configured in a way that an administrator can create a large pool of storage and then have users carve out pieces from it has required. 

-> That is where persistent volumes can help us.

![](images/ps2.png)

A persistent volume is a cluster wide pool of storage volumes configured by an administrator to be used by users deploying applications on the Cluster.
The users can now select storage from this pool using ** persistent volume claims** let us now create a persistent volume.

### Example config persistent volume
![](images/ps3.png)
                      

### [Access Modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes)
```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: host-pv
spec:
  capacity:
    storage: 1Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
    - ReadOnlyMany
    - ReadWriteMany
  hostPath:
    path: /data
    type: DirectoryOrCreate
```

Ta có thể thấy có 3 access modes
* ReadWriteOnce
  * volume có thể được mounted như là một read-write volume bởi chỉ 1 sigle Node
  * Có thể mount trên multiple pod nhưng chỉ được claim trên cùng 1 Node
* ReadOnlyMany
  * Read Only
  * Có thể được claim trên multiple Node
  * multiple pod trên các Nodes khác nhau có thể  claim loại volume này
* ReadWriteMany
  * Read-Write access
  * còn lại giống với ReadOnlyMany

![](images/ps5.png)

### volumeMode
Kubernetes supports two volumeModes of PersistentVolumes: Filesystem and Block.

volumeMode is an optional API parameter. Filesystem is the default mode used when volumeMode parameter is omitted.

A volume with volumeMode: Filesystem is mounted into Pods into a directory. If the volume is backed by a block device and the device is empty, Kuberneretes creates a filesystem on the device before mounting it for the first time.

You can set the value of volumeMode to Block to use a volume as a raw block device. Such volume is presented into a Pod as a block device, without any filesystem on it. This mode is useful to provide a Pod the fastest possible way to access a volume, without any filesystem layer between the Pod and the volume. On the other hand, the application running in the Pod must know how to handle a raw block device. See Raw Block Volume Support for an example on how to use a volume with volumeMode: Block in a Pod