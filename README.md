# jinja_renderer
jinja_renderer app

docker build -t muzammilpeer/jinja-render .
docker push muzammilpeer/jinja-render
kubectl apply -f backend-deployment.yaml
kubectl apply -f hpa.yaml

kubectl get all
kubectl get hpa


# smart refresh
kubectl set image deployment/jinja-render jinja-render=muzammilpeer/jinja-render:latest --record

![Sampel App interface](/jinja-sample-app.png)
