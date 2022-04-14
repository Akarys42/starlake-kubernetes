# User Accounts

## Starchild User
2. Create user: `kubectl apply -f starchild-service-account.yaml`
3. Bind them: `kubectl apply -f starchild-binding.yaml`
4. Generate kubeconfig: `./generate_kubeconfig.py starchild`

## CI/CD User
1. Create role: `kubectl apply -f ci-role.yaml`
2. Create user: `kubectl apply -f ci-service-account.yaml`
3. Bind them: `kubectl apply -f ci-binding.yaml`
4. Generate kubeconfig: `./generate_kubeconfig.py ci`