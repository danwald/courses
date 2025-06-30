
kubectl create namespace mynamespace
kubectl get namespaces
kubectl run nginx --image=nginx -n mynamespace
kubectl get pods --namespace mynamespace

echo "sleeping .. " && sleep 10

kubectl delete pod nginx --namespace mynamespace
kubectl delete namespace mynamespace
