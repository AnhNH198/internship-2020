# Affinity and anti-affinity

The affinity/anti-affinity feature allows you to do more complex scheduling than the nodeSelector and also works on Pods

* You can create rules that are not hard requirements, but rather a preferred rule, meaning that the scheduler will still be able to schedule your pod, even if the rules cannot be met

* You can create rules that take other pod labels into account

  * For example, a rule that makes sure 2 different pods will never be on the same node


##### Kubernetes can do node affinity and pod affinity/anti-affinity
* Node affinity is similar to the nodeSelector
* Pod affinity/anti-affinity allows you to create rules how pods should be
scheduled taking into account other running pods
* Affinity/anti-affinity mechanism is only relevant during scheduling, once a pod is running, it’ll need to be recreated to apply the rules again

* There are currently 2 types you can use for node affinity:
• 1) requiredDuringSchedulingIgnoredDuringExecution
• 2) preferredDuringSchedulingIgnoredDuringExecution
The first one sets a hard requirement (like the nodeSelector)
•
•
The rules must be met before the pod can be scheduled
The second type will try to enforce the rule, but it will not guarantee it
•
Even if the rule is not met, the pod can still be scheduled, it’s a soft
requirement, a preference