# Site Deployment
## Pre-requisites
- Nginx is deployed
- mTLS is set up

## Steps

### Configure the Pod
1. Provision a user/database pair: `../postgres/generate_database.sh forum_quiltmc_org`
2. Save developer emails to `DEVELOPER_EMAILS.txt`
3. Save STMP credentials to `STMP_USER_NAME.txt` and `STMP_PASSWORD.txt`
4. Create the secret `kubectl create secret generic forum-quiltmc-org-env --from-file=DISCOURSE_DEVELOPER_EMAILS=DEVELOPER_EMAILS.txt --from-file=DISCOURSE_DB_PASSWORD=PASSWORD_forum_quiltmc_org.txt --from-file=DISCOURSE_STMP_USER_NAME=STMP_USER_NAME.txt --from-file=DISCOURSE_STMP_PASSWORD=STMP_PASSWORD.txt`

### Deploy the Site
5. Deploy! : `kubectl apply -f deployment.yaml`
6. Create the service: `kubectl apply -f service.yaml`
7. Start the ingress `kubectl apply -f ingress.yaml`
