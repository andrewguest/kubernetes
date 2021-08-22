### Routes
|Route|Query Parameters|Description|
|---|---|---|
|/dogfacts|facts_limit|Returns random dog facts. The default is 10 random facts, but the "facts_limit" parameter can be used to increase or decrease this number.|
|/healthcheck|None|Used as a healthcheck for Kubernetes to verify that status of the pod.|

---

Build the image (if you cloned the repo):
<br />
```docker build -t <docker hub username>/kubernetes-example-backend:1.0 .```

Push the image to Docker Hub:
<br />
```docker push <docker hub username>/kubernetes-example-backend:1.0```

Run the container with Docker (locally):
<br />
```docker run -d -p 8000:8000 aguest/kubernetes-example-backend:1.0```