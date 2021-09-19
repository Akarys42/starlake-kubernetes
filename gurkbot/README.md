# Gurkbot Deployment
## Pre-requisites
- PostgreSQL is deployed

## Steps
### Preparing the deployment
1. Create a database: `../postgres/generate_database.sh gurkbot`
2. Save the bot token to a file named `token.txt`

### Deploy the service
3. Create the secret `kubectl create secret generic gurkbot-env --from-file=TOKEN=token.txt --from-literal=DATABASE_URL=postgres://gurkbot:(cat PASSWORD_gurkbot.txt)@postgres.default.svc.cluster.local:5432/gurkbot --from-literal=ENVIRONMENT=production`
4. Deploy! `kubectl apply -f deployment.yaml`