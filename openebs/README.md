# OpenEBS Deployment

## Helm Repositories
1. Jiva: `helm repo add openebs-jiva https://openebs.github.io/jiva-operator`
2. Update repositories: `helm repo update`

## Jiva Operator
3. Install Jiva Operator: `helm install --create-namespace -n openebs-jiva -f helm-values.yaml openebs-jiva openebs-jiva/jiva`