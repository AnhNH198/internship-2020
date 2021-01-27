The Kubernetes apiserver has two client CA options:
```
    --client-ca-file
    --requestheader-client-ca-file```
```
Each of these functions independently and can conflict with each other, if not used correctly.

*    --client-ca-file: When a request arrives to the Kubernetes apiserver, if this option is enabled, the Kubernetes apiserver checks the certificate of the request. If it is signed by one of the CA certificates in the file referenced by --client-ca-file, then the request is treated as a legitimate request, and the user is the value of the common name CN=, while the group is the organization O=. See the documentation on TLS authentication.

*   --requestheader-client-ca-file: When a request arrives to the Kubernetes apiserver, if this option is enabled, the Kubernetes apiserver checks the certificate of the request. If it is signed by one of the CA certificates in the file reference by --requestheader-client-ca-file, then the request is treated as a potentially legitimate request. The Kubernetes apiserver then checks if the common name CN= is one of the names in the list provided by --requestheader-allowed-names. If the name is allowed, the request is approved; if it is not, the request is not.

* If both --client-ca-file and --requestheader-client-ca-file are provided, then the request first checks the --requestheader-client-ca-file CA and then the  --client-ca-file. Normally, different CAs, either root CAs or intermediate CAs, are used for each of these options; regular client requests match against --client-ca-file, while aggregation requests match against --requestheader-client-ca-file. However, if both use the same CA, then client requests that normally would pass via --client-ca-file will fail, because the CA will match the CA in --requestheader-client-ca-file, but the common name CN= will not match one of the acceptable common names in --requestheader-allowed-names. This can cause your kubelets and other control plane components, as well as end-users, to be unable to authenticate to the Kubernetes apiserver.

-> For this reason, use different CA certs for the --client-ca-file option - to authorize control plane components and end-users - and the --requestheader-client-ca-file option - to authorize aggregation apiserver requests.