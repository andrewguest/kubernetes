Build the image (if you cloned the repo):
<br />
```docker build -t <docker hub username>/kubernetes-example-frontend:1.2 .```

Push the image to Docker Hub:
<br />
```docker push <docker hub username>/kubernetes-example-frontend:1.2```

Run the container with Docker (locally):
<br />
```docker run -d -p 8000:8000 aguest/kubernetes-example-frontend:1.2```