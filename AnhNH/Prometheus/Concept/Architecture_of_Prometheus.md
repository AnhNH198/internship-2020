# Architecture of Prometheus

![](../images/architect.png)

---
### 1. First component: Prometheus Server
![](../images/architect1.png)


-> Core Prometheus system, Basic working of Prometheus server is divided into three parts retrieval
 1. Retrieval: Scrape data from its target nodes, which can be any system or application and then store that data in to the sotrage
 2. TSDB/Storage: Prometheus stores data locally in a custom time series Database and storage that can be HDD or SSD
 3. Stored data is made available to the visualization tools like Grafana through HTTP
---
### 2. How Prometheus retrieves metrics from target nodes

![](../images/architect2.png)
Prometheus, most of the time uses the pull method while monitoring systems.

This is an **important** thing to **note that Prometheus by itself pulls the matrix from target system**. The target system does not push Matrix in Prometheus.

If you have deployed Prometheus to monitor your systems or any applications, then unlike other monitoring tools, your application need not to send metrics to Prometheus. Rather, Prometheus itself pulls or scrapes a matrix from the targets.

This pulling feature of Prometheus over HTTP offers your applications of more flexibility of developing changes.

---

Now, talking little about these targets as targets can be inform of jobs or exporter's jobs as in your own custom defined jobs.

Or you may use some exporters to obtain metrics like a Linux machine or a window machine, etc. not only the external applications, but to make Prometheus highly available. It also allows us the capabilities to pull metrics from other Prometheus servers as well.

So, for example, if there are two Prometheus instances running than one prometheus instance can scrape the metrics of other instance.
Okay, so this is how Prometheus pulled the metrics from targets.

---
### Pushgateway

![](../images/architect3.png)
Now, coming to this push gateway, no doubt that overall Prometheus architecture believes that pulling is slightly better than pushing.

But there are some special components which cannot be directly escaped.For **example**, some **short lived service** level bad jobs can't be scraped through pulling metrics. So to monitor these kind of jobs. 

Prometheus uses a push with the Prometheus push. Pushgateway allows Short-Lived bad jobs to push time series to an intermediary job. 

But again, to have it invested in the code, it will use the pull approach only to fetch those pushed 

So basically the flow will  be the jobs will push metrics into an intermediate entity from where Prometheus will pull those metrics into its score.

---
### Service Discovery
![](../images/architect5.png)
Once you have the applications or your exporters ready and running to get scraped.

The question is how will Prometheus know where they are residing?
I mean, how it will know which all entities it has to monitor.

How will it locate its targets?
This is what a service discovery is for, to make Prometheus aware of your target.

You have two options: 
1. Either way, you can hardcoded targets in Prometheus, which is not the best approach as you may have

2. a long list of dynamic targets that may get increase over that time.

To targets, for example, in a running cluster. You may add any number of nodes in the cluster.

If the targets are **hardcoded** in Prometheus, then the new nodes are **never** going to **get scraped** because Prometheus won't have knowledge about these nodes. Right?

So the **other way for these kind of Dynamic environments**, you can use **service discovery**, which is also the **recommended approach actually in real time environments.**

You probably would know that we have some inventory database of our applications and machines. These inventories may maybe based on DNS K8s, ...

Now, Prometheus has integration with these Common Service discovery mechanisms.

So **whenever a change is made in the inventory**, like if a notice adult, since Prometheus has integration with the inventory, **it would add that note automatically as a target and starts scraping it.**

So these were the Prometheus architectural components that helped in pulling and pushing the metrics from target nodes.

---
### Data visualization and export
![](../images/architect7.png)
Now let's move on and see what happens after the metrics are scraped and stored into the database. 

As already explained, after the metrics are stored in some local storage, these metrics are made available to the user 

using the parameters WebUI. You can request raw data with its query language from Google or out-of-the-box primitives.

Also comes with a feature that can produce graphs and dashboards out of metrics. Also, you can integrate **Grafana out to create your own nice dashboards**.

**Prometheus even gives you the freedom to integrate third party API claims to do custom things with the stored metrics** 
---
### Alert Manager
![](../images/architect6.png)

Now coming towards the last component. It is alert manager.
As we discussed in the previous lecture, that alerts are pushed by the Prometheus servers into the alert manager.

The Alert Manager, after receiving the alerts from Prometheus servers, aggregate those alerts into groups, apply silences, throttles on them and then at last it sends out notifications to email, pager, duty, slack or other services to call in a human to take a look on those alerts.