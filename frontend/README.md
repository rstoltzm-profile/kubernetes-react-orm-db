# Deploy Front-end
```
kubectl apply -f deployment.yaml
kubectl port-forward service/my-react-app-service 1080:80
```