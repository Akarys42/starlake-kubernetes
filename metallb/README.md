# MetalLB Deployment

### Preparation
1. Enable strict ARP mode:
```shell
kubectl get configmap kube-proxy -n kube-system -o yaml | \
sed -e "s/strictARP: false/strictARP: true/" | \
kubectl apply -f - -n kube-system
```

### Helm Repositories
2. MetalLB: `helm repo add metallb https://metallb.github.io/metallb`
3. Update repositories: `helm repo update`

### Install MetalLB
3. Deploy MetalLB: `helm install --create-namespace -n metallb-system -f helm-values.yaml metallb metallb/metallb`