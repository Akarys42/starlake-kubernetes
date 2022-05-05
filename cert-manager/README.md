# Cert-manager Deployment
## Pre-requisites
- Nginx is deployed

## Steps
### Helm Repositories
1. Nginx: `helm repo add jetstack https://charts.jetstack.io`
2. Update repositories: `helm repo update`

### Install Cert-manager
3. Deploy! `helm install -n cert-manager --create-namespace cert-manager -f helm-values.yaml jetstack/cert-manager`

### Install issuers
4. Let's encrypt staging: `kubectl apply -f letsencrypt-staging.yaml`
5. Let's encrypt production: `kubectl apply -f letsencrypt-production.yaml`
