#!/bin/bash
set -e

if [ $# -eq 0 ]; then
  echo "No service name supplied."
  exit 1
fi

service=$1
pod=$(kubectl get pods --selector "app=postgres" --output=name)

echo "=> Creating user/database pair \`$service\` on pod \`$pod\`"

if [ -f PASSWORD_$service.txt ]; then
  echo "- Using existing password."
else
  echo "- Generating password in \`PASSWORD_$service.txt\`.."
  ../generate_token.py 32 PASSWORD_$service.txt
fi

echo "- Creating database.."
kubectl exec "$pod" -- psql -U kissland-admin -c "CREATE DATABASE $service;"

echo "- Creating user.."
kubectl exec "$pod" -- psql -U kissland-admin -c "CREATE USER $service WITH ENCRYPTED PASSWORD '$(cat PASSWORD_$service.txt)';"

echo "- Granting access to the user.."
kubectl exec "$pod" -- psql -U kissland-admin -c "GRANT ALL PRIVILEGES ON DATABASE $service TO $service;"

echo "=> Done!"
