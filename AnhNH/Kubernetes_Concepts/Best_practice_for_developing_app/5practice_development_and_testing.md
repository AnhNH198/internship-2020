# Best practices for development and testing
We’ve talked about what to be mindful of when developing apps, but we haven’t
talked about the development and testing workflows that will help you streamline
those processes. I don’t want to go into too much detail here, because everyone needs
to find what works best for them, but here are a few starting points.

## 1. Running apps outside of Kubernetes during development
When you’re developing an app that will run in a production Kubernetes cluster, does
that mean you also need to run it in Kubernetes during development? Not really. Hav-
ing to build the app after each minor change, then build the container image, push it
to a registry, and then re-deploy the pods would make development slow and painful.
Luckily, you don’t need to go through all that trouble.
You can always develop and run apps on your local machine, the way you’re used
to. After all, an app running in Kubernetes is a regular (although isolated) process
running on one of the cluster nodes. If the app depends on certain features the
Kubernetes environment provides, you can easily replicate that environment on your
development machine.
I’m not even talking about running the app in a container. Most of the time, you
don’t need that—you can usually run the app directly from your IDE.
### 1.1 CONNECTING TO BACKEND SERVICES
In production, if the app connects to a backend Service and uses the BACKEND_SERVICE
_HOST and BACKEND_SERVICE_PORT environment variables to find the Service’s coordi-
nates, you can obviously set those environment variables on your local machine manu-
ally and point them to the backend Service, regardless of if it’s running outside or
inside a Kubernetes cluster. If it’s running inside Kubernetes, you can always (at least
temporarily) make the Service accessible externally by changing it to a NodePort or a
LoadBalancer -type Service.
### 1.2 CONNECTING TO THE API SERVER
Similarly, if your app requires access to the Kubernetes API server when running
inside a Kubernetes cluster, it can easily talk to the API server from outside the cluster
during development. If it uses the ServiceAccount’s token to authenticate itself, you
can always copy the ServiceAccount’s Secret’s files to your local machine with kubectl
cp . The API server doesn’t care if the client accessing it is inside or outside the cluster.
If the app uses an ambassador container like the one described in chapter 8, you
don’t even need those Secret files. Run kubectl proxy on your local machine, run
your app locally, and it should be ready to talk to your local kubectl proxy (as long as
it and the ambassador container bind the proxy to the same port).
In this case, you’ll need to make sure the user account your local kubectl is using
has the same privileges as the ServiceAccount the app will run under.
### 1.3 RUNNING INSIDE A CONTAINER EVEN DURING DEVELOPMENT
When during development you absolutely have to run the app in a container for what-
ever reason, there is a way of avoiding having to build the container image every time.
Instead of baking the binaries into the image, you can always mount your local filesys-
tem into the container through Docker volumes, for example. This way, after you
build a new version of the app’s binaries, all you need to do is restart the container (or
not even that, if hot-redeploy is supported). No need to rebuild the image.
## 2. Employing Continuous Integration and Continuous Delivery (CI/CD)
We’ve touched on automating the deployment of Kubernetes resources two sections back, but you may want to set up a complete CI/CD pipeline for building your application binaries, container images, and resource manifests and then deploying them in
one or more Kubernetes clusters.
You’ll find many online resources talking about this subject. Here, I’d like to point you specifically to the Fabric8 project (http://fabric8.io), which is an integrated
development platform for Kubernetes. It includes Jenkins, the well-known, open-
source automation system, and various other tools to deliver a full CI/CD pipeline
for DevOps-style development, deployment, and management of microservices on
Kubernetes.
If you’d like to build your own solution, I also suggest looking at one of the Google
Cloud Platform’s online labs that talks about this subject. It’s available at https://
github.com/GoogleCloudPlatform/continuous-deployment-on-kubernetes.