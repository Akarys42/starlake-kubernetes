# Site Deployment
## Pre-requisites
- Nginx is deployed
- Redis is deployed
- mTLS is set up

## Steps

### Configure the Pod
1. Provision a user/database pair: `../postgres/generate_database.sh forum_quiltmc_org`
2. Save developer emails to `DEVELOPER_EMAILS.txt`
3. Save SMTP credentials to `STMP_USER_NAME.txt` and `STMP_PASSWORD.txt`
4. Create the secret 
```
kubectl create secret generic forum-quiltmc-org-env \
    --from-file=DISCOURSE_DEVELOPER_EMAILS=DEVELOPER_EMAILS.txt \
    --from-file=DISCOURSE_DB_PASSWORD=PASSWORD_forum_quiltmc_org.txt \
    --from-file=DISCOURSE_SMTP_USER_NAME=SMTP_USER_NAME.txt \
    --from-file=DISCOURSE_SMTP_PASSWORD=SMTP_PASSWORD.txt \
    --from-file=DISCOURSE_S3_ACCESS_KEY_ID=S3_ACCESS_KEY.txt \
    --from-file=DISCOURSE_S3_SECRET_ACCESS_KEY=S3_SECRET_KEY.txt \
    --from-file=DISCOURSE_REDIS_PASSWORD=../redis/PASSWORD.txt
```

### Deploy the Site
5. Deploy! : `kubectl apply -f deployment.yaml`
6. Create the service: `kubectl apply -f service.yaml`
7. Start the ingress `kubectl apply -f ingress.yaml`
