# Blackbox Setup

## Setup environment

1. Save the dawnfm S3 credentials in a `key_id.txt` and `access_key.txt` file.
2. Save the webhook URL in a `webhook.txt` file.
3. Create the secret: 
```
kubectl create secret generic blackbox-env \
  --from-literal=POSTGRES_USER=kissland-admin --from-file=POSTGRES_PASSWORD=../postgres/PASSWORD.txt \
  --from-file=KEY_ID=key_id.txt --from-file=ACCESS_KEY=access_key.txt \
  --from-file=WEBHOOK_URL=webhook.txt

## Deploy Blackbox

4. Apply the configmap: `kubectl apply -f config.yaml`
5. Apply the cronjob: `kubectl apply -f cronjob.yaml`

## Test Run

6. Test that everything is working as excepted: `kubectl create job --from=cronjob/blackbox blackbox-manual-001`
