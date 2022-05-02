# Site Deployment
## Pre-requisites
- Nginx is deployed
- mTLS is set up

## Steps

### Deploy
1. Deploy! : `kubectl apply -f deployment.yaml`
2. Create the service: `kubectl apply -f service.yaml`
3. Start the ingress `kubectl apply -f ingress.yaml`
