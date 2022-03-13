# Commons

## GHCR login
1. Set your GitHub login to a `GH_LOGIN` environment variable.
2. Create a GitHub token with the scope `read:packages` and save it to a `GHCR_TOKEN.txt` file.
3. Log to the GitHub Container Registry: `cat GHCR_TOKEN.txt | docker login https://ghcr.io -u $GH_LOGIN --password-stdin`
4. Create a Kubernetes secret:
```
kubectl create secret generic ghcr-login \
   --from-file=.dockerconfigjson=$HOME/.docker/config.json \
   --type=kubernetes.io/dockerconfigjson
```