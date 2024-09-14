# Build the image only
docker-build:
	docker build -t aguest/quotes-api:latest .


# Run the container locally
docker-run:
	docker run -d -p 8000:8000 aguest/quotes-api:latest


# Build and push the image to Docker Hub
docker-build-push:
	docker build -t aguest/quotes-api:latest . \
	&& \
	docker push aguest/quotes-api:latest


# Update the k8s deployment
k8s-deployment:
	kubectl apply -f ./kubernetes/quotes_api_deployment.yaml


# Update the k8s service
k8s-service:
	kubectl apply -f ./kubernetes/quotes_api_service.yaml


# Upate the k8s ingress
k8s-ingress:
	kubectl apply -f ./kubernetes/quotes_api_ingress.yaml
