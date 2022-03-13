# Site Deployment
## Pre-requisites
- Nginx is deployed
- mTLS is set up
- (commons) GHCR login is set up

## Steps

### Configure the Pod
1. Generate secret key: `../generate_token.py 64 SECRET_KEY.txt`
2. Provision a user/database pair: `../postgres/generate_database.sh athena_test_com`
3. Save the S3 secret key to `S3_SECRET_KEY.txt`
4. Create the secret `kubectl create secret generic athena-test-com-env --from-file=SECRET_KEY=SECRET_KEY.txt --from-file=DATABASE_PASSWORD=PASSWORD_athena_test_com.txt --from-file=S3_SECRET_KEY=S3_SECRET_KEY.txt `
5. Apply the config map: `kubectl apply -f config.yaml`

### Deploy the Site
6. Deploy! : `kubectl apply -f deployment.yaml`
7. Create the service: `kubectl apply -f service.yaml`
8. Start the ingress `kubectl apply -f ingress.yaml`
