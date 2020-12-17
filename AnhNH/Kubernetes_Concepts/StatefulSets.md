# StatefulSets
StatefulSet là một workload API object được sử dụng để quản lý các stateful application(web application, database, ...)

StatefulSets quản lý deployment và scaling set of Pods, đảm bảo về ordering và uniqueness của Pods

Giống như Deployment, một StatefulSet quản lý Pods dự trên một identical container spec.

Không giống như Deployment, một StatefulSet duy trì một sticky identity cho mỗi Pods của nó. Nhưng pods này được tạo dùng chung spec, nhưng không thể thay thế cho nhau: Mỗi cái có một persistent identifier duy trì across any rescheduling

Nếu ta muốn sử dụng storage volumes để cung cấp persistence cho workload, ta có thể sử dụng StatefulSets như là một phần của giải pháp. Mặc dù individual Pods trong một StatefulSet là dễ bị lỗi, the persistent Pods identifiers make it easier to match existing volumes to the new Pods that replace any that have failed

### Sử dụng StatefulSets
StatefulSets thích hợp cho những application yêu cầu 1 hoặc nhiều requirements dưới:
 ##### Stable, unique network identifier
 ##### Stable, persistent storage
 Ngay cả khi pod bị lỗi hoặc bị xóa đi, khi pod mới vào thay thế nó vẫn sẽ nhận lại storage, network address, ... mà con cũ sử dụng
 ##### Ordered, graceful deployment and scaling
 * Ví dụ: Ta triển khai StatefulSets từ web0 - web2
   - Nó sẽ tạo lần lượt từ web0 - web1 - web2
   - Nếu web 1 ready nhưng web0 tự dưng lỗi -> chờ web0 lên lại mới tiếp tục web2 (ordered provisioning)
   - Ngược lại với delete, nó sẽ delete web2 trước đến web1 rồi web0, nếu web2 không thể bị xóa thì web1 web0 sẽ không bị xóa

##### Ordered, automated rolling updates
 * Ví dụ: Ta update web từ web0 đến web2
  - web2 sẽ được update đầu tiền rồi moi đến web1 -> web0


### Những giới hạn
* Xóa hoặc scaling down một StatefulSet sẽ không xóa volume associated với StatefulSet đó. Điều này đảm bảo Data được an toàn
* StatefulSet hiện tại yêu cầu một [Headless Service]() chịu trách nhiệm cho việc network identity of the Pods. Ta  có trách nhiệm phải tự tạo Service này
