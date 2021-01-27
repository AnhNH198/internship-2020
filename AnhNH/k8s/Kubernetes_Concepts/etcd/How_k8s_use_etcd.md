# How k8s use etcd
All the objects you’ve created throughout this book—Pods, ReplicationControllers, Services, Secrets, and so on—need to be stored somewhere in a persistent manner so their manifests survive API server restarts and failures. For this, Kubernetes uses etcd,which is a fast, distributed, and consistent key-value store. Because it’s distributed, you can run more than one etcd instance to provide both high availability and bet-ter performance. 

The only component that talks to etcd directly is the Kubernetes API server. All other components read and write data to etcd indirectly through the API server. This brings a few benefits, among them a more robust optimistic locking system as well as
validation; and, by abstracting away the actual storage mechanism from all the other components, it’s much simpler to replace it in the future. It’s worth emphasizing that etcd is the only place Kubernetes stores cluster state and metadata.

```
**About optimistic concurrency control**
Optimistic concurrency control (sometimes referred to as optimistic locking) is a method where instead of locking a piece of data and preventing it from being read or updated while the lock is in place, the piece of data includes a version number. 

Every time the data is updated, the version number increases. When updating the data, the version number is checked to see if it has increased between the time the client read the data and the time it submits the update. If this happens, the update is rejected and the client must re-read the new data and try to update it again. The result is that when two clients try to update the same data entry, only the first one succeeds. 

All Kubernetes resources include a metadata.resourceVersion field, which clientsneed to pass back to the API server when updating an object. If the version doesn’t match the one stored in etcd, the API server rejects the update.
```