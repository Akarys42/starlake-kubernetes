# Luna Deployment
## Pre-requisites
- PostgreSQL is deployed

## Steps
### Preparing the deployment
1. Create a database: `../postgres/generate_database.sh starbotluna`
2. Save the bot token to a file named `token.txt`

### Deploy the service
3. Create the secret `kubectl create secret generic luna-env --from-file=TOKEN=token.txt --from-literal=DATABASE_URL=postgresql+asyncpg://starbotluna:(cat PASSWORD_starbotluna.txt)@postgres.default.svc.cluster.local:5432/starbotluna`
4. Create the configmap `kubectl apply -f config.yaml`
5. Deploy! `kubectl apply -f deployment.yaml`