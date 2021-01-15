# Docker Pipeline plugin
* docker pipeline plugin, cho phép ta khởi tạo bất kỳ container bên trong pipeline

* Không chỉ giúp ta khởi tạo hay build new containers, mà nó còn giúp ta run existing containers
  * -> Nó hữu ích khi ta không muốn gộp development tools với production container, nhưng ta vẫn muốn chạy all stages trong một isolated environtment 
    * -> ta có thể  build/test application trước trên existing container với tất cả development tools
    * -> tiếp theo ta có thể build new container, much tinier, with only the runtime environtment that you only need to run application

##### Example
*   Spinning up new docker containers let you bring in any new tool, easily
    *   you can specify exactly what dependencies you want, at any stage in the job
    *   You can start a database during the test stage to run tests on
    *   after the database tests have been concluded, the container can be removed, together with all the data
    *   Next time you run a new database contaienr during test, you will have a brand new container again
    *   This also works for multiple builds at the same time(example we have multiple git branches), every build has its own database container.