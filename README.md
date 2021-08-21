## Fullstack web app deployed to Kubernetes

This is meant to be an example and reference for how to create and deploy a fullstack application to Kubernetes. It's also meant to explain the different components of Kubernetes.

---

|Component|Description|
|---|---|
|Pod|Pods in Kubernetes run a container or containers. They are the smallest "unit" in Kubernetes.|
|Deployment|A deployment tells Kubernets what image or images to run inside the pod, how many pods you want (replicas), what port or ports to expose on the pod and plenty of other information.|
|Service|A service creates a single, constant point of entry to a deployment. Basically, a service is needed to access your pods from outside Kubernetes or to loadbalance between groups of pods.|
|Ingress|Ingress exposes HTTP and HTTPS routes from outside the Kubernetes cluster to services within the cluster. This allows you to access routes inside your Kubernetes cluster from outside the cluster.|

---

## Files and their descriptions
To make it easier on me, I've broken each Kubernetes component into it's own file even though this means for files and more commands to run. The tables below are also setup in the order that I would run the files (top file first, then work your way down).

### Backend
```
kubectl apply -f ./backend/backend-deployment.yaml
kubectl apply -f ./backend/backend-service.yaml
kubectl apply -f ./backend/backend-autoscaler.yaml
```

|File|Description|
|---|---|
|[backend-deployment.yaml](backend/backend-deployment.yaml)|Defines values such as the image to use for the pods, the port(s) to open on the pods, how many pods to start, and the CPU & RAM resources the pod(s) get and their limits.|
|[backend-service.yaml](backend/backend-service.yaml)|Tells Kubernetes to send requests on port 3000 (on the worker nodes) to port 8000 on the 'backend-api' pods.|
|[backend-autoscaler.yaml](backend/backend-autoscaler.yaml)|Defines the minimum and maximum number of replicas that Kubernetes should keep running or scale up to and the criteria for scaling up or down.|


### Traefik
```
kubectl apply -f ./traefik/traefik-cluster-role.yaml
kubectl apply -f ./traefik/traefik-service-account.yaml
kubectl apply -f ./traefik/traefik-cluster-role-binding.yaml
kubectl apply -f ./traefik/traefik-deployment.yaml
kubectl apply -f ./traefik/traefik-service.yaml
kubectl apply -f ./traefik/traefik-ingress.yaml
```

|File|Description|
|---|---|
|[traefik-cluster-role.yaml](traefik/traefik-cluster-role.yaml)|Defines a custom Kubernetes cluster role that service accounts can then be given.|
|[traefik-service-account.yaml](traefik/traefik-service-account.yaml)|Creates a service account that Traefik can use to manage cluster ingress.|
|[traefik-cluster-role-binding.yaml](traefik/traefik-cluster-role-binding.yaml)|Assigns the service account, created in traefik-service-account.yaml, the cluster role defined in traefik-cluster-role.yaml.|
|[traefik-deployment.yaml](traefik/traefik-deployment.yaml)|Defines values such as the image to use for the pods, the port(s) to open on the pods, how many pods to start, and the CPU & RAM resources the pod(s) get and their limits.|
|[traefik-service.yaml](traefik/traefik-service.yaml)|Tells Kubernetes what port(s) on the k8s worker nodes are tied to what pod port(s).|
|[traefik-ingress.yaml](traefik/traefik-ingress.yaml)||
