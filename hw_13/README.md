# hw_13

## Build image

```powershell
docker build -t denisdataops/hw13-service:latest .
docker push denisdataops/hw13-service:latest
```

## Run with Docker Compose

```powershell
docker compose up -d
```

## Apply Kubernetes manifests

```powershell
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
```

## Check resources

```powershell
kubectl get pods
kubectl get service
kubectl get ingress
curl --header "Host: example.com" http://INGRESS_IP/
```
