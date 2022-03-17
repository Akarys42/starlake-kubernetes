# User Accounts

### CI/CD User
1. Create role: `kubectl apply -f ci-role.yaml`
2. Create user: `kubectl apply -f ci-service-account.yaml`
3. Bind them: `kubectl apply -f ci-binding.yaml`
4. Generate kubeconfig: `./generate_kubeconfig.py ci`