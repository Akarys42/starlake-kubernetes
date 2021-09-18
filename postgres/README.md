# PostgreSQL Deployment

## Steps
### Deploy Engine
2. Load configuration: `kubectl apply -f config.yaml`
3. Generate admin password: `../generate_token.py`.
4. Create secret: `kubectl create secret generic postgres-env --from-literal=POSTGRES_USER=kissland-admin --from-file=POSTGRES_PASSWORD=PASSWORD.txt`
5. Deploy PostgreSQL: `kubectl apply -f deployment.yaml`
6. Create service: `kubectl apply -f service.yaml`
