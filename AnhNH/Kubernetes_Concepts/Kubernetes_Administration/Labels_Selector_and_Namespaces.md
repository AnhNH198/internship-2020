# Labels, selectors và namespaces.

Label, selector và namespace giúp ta tổ chức và sắp xếp applications -> khi ta quản lý nhiều applications, ta vẫn có thể hiểu rõ tổng quan hệ thống.

##### Label:
Label là key-value pair được gắn với object(pod, service và deployments). Label giúp ta định danh được tính chất của object. Thông thường, labels được sử dụng để tổ chức các cluster in some meaningful way. Chúng có thể được thêm vào at deployment time, hoặc thêm vào sau đó và có thể được thay đổi bất kỳ lúc nào
 - Label keys là unique per object.
 - Ví dụ về label:
   - "release": "stable", "release": "canvary", ...
   - "environment": "dev", "environment": "qa", ...
   - "tier": "frontend", "tier": "backend", ...
![](images/l.png)

labels are very specific to your use case, and they are built for users, so think about what your environment looks like, and how you want to organize your applications, and then get your label maker out.

##### Selector:
Selector kết hợp với label tạo thành 1 tính năng toàn tăng. Với label kết hợp vơis selector ta có thể định danh 1 specific set of objects.
* Có 2 loại selectors:
 - equality-based:
  ![](images/equal_based_s.png)
 - set-based
  ![](images/set_based_selector.png)

##### namespaces:
namespace là một feature của kubernetes cho phép ta có multiple virtual clusters trên cùng một physical cluster.

Namespaces rất tốt cho việc sử dụng cho hệ thống lớn có rất nhiều user và team khác nhau. Ví dụ khi mà ta muốn give access to different team nhưng ta vẫn muốn kiểm soát xem ai được quyền access vào cái gì trong môi trường kubernetes
- ![](images/namespaces.png)
- Ví dụ:
  - Ta có triển khai cho 1 big e-commerce company sẽ có namespace cho catalog team, card team và order status team để họ có thể chạy app khác nhau trên cùng một hệ thống.
- Ta có thể phân chia tài nguyên cluster sử dụng resource quotas.