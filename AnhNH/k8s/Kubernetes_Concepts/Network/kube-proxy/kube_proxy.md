# Introduce kube-proxy
Everything related to Services is handled by the kube-proxy process running on each
node. Initially, the kube-proxy was an actual proxy waiting for connections and for
each incoming connection, opening a new connection to one of the pods. This was
called the userspace proxy mode. Later, a better-performing iptables proxy mode
replaced it. This is now the default, but you can still configure Kubernetes to use the
old mode if you want.
Before we continue, let’s quickly review a few things about Services, which are rele-
vant for understanding the next few paragraphs.
We’ve learned that each Service gets its own stable IP address and port. Clients
(usually pods) use the service by connecting to this IP address and port. The IP
address is virtual—it’s not assigned to any network interfaces and is never listed as
either the source or the destination IP address in a network packet when the packet
leaves the node. A key detail of Services is that they consist of an IP and port pair (or
multiple IP and port pairs in the case of multi-port Services), so the service IP by itself
doesn’t represent anything. That’s why you can’t ping them.