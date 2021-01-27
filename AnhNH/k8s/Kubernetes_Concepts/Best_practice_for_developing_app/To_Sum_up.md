# Sum up
In this chapter has given you an even deeper insight into how Kubernetes works and will help you build apps that feel right at home when deployed to a Kubernetes cluster. The aim of this chapter was to:

*   Show you how all the resources covered in this book come together to represent a typical application running in Kubernetes.
*   Make you think about the difference between apps that are rarely moved between machines and apps running as pods, which are relocated much more frequently.

*   Help you understand that your multi-component apps (or microservices, if you will) shouldn’t rely on a specific start-up order.
*   Introduce init containers, which can be used to initialize a pod or delay the start of the pod’s main containers until a precondition is met.
*   Teach you about container lifecycle hooks and when to use them.
*   Gain a deeper insight into the consequences of the distributed nature of Kubernetes components and its eventual consistency model.
*   Learn how to make your apps shut down properly without breaking client connections.
*   Give you a few small tips on how to make your apps easier to manage by keeping image sizes small, adding annotations and multi-dimensional labels to all your resources, and making it easier to see why an application terminated.
*   Teach you how to develop Kubernetes apps and run them locally or in Minikube before deploying them on a proper multi-node cluster.