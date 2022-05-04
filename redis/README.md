# Redis Deployment

1. Generate a password: `../generate_token.py`
2. Convert it to a config file: `echo "requirepass $(cat PASSWORD.txt)" > redis.conf`
3. Create a secret: `kubectl create secret generic redis-config --from-file=redis.conf`
4. Deploy Redis: `kubectl apply -f deployment.yaml`
5. Create service: `kubectl apply -f service.yaml`

# Used Database Indices
- `00`: Reserved
- `01`: [forum.quiltmc.org](../forum.quiltmc.org)
