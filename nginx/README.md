# Nginx Deployment

## Pre-requisites
- MetalLB is deployed

## Steps
### Helm Repositories
1. Nginx: `helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx`
2. Update repositories: `helm repo update`

### Install Nginx
3. Create namespace: `kubectl create namespace ingress-nginx`
4. Deploy Nginx: `helm install -n ingress-nginx -f helm-values.yaml ingress-nginx ingress-nginx/ingress-nginx`
