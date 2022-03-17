#!/usr/bin/env python3
GET_LOCAL_KUBECONFIG = ["kubectl", "config", "view", "--minify=true", "--raw"]
GET_SECRET_NAME = ["kubectl", "get", None, "-o", "jsonpath='{.secrets[0].name}'"]
GET_TOKEN = ["kubectl", "get", "secret", None, "-o", "jsonpath='{.data.token}'"]

HELP_TEXT = """
Usage:
    generate_kubeconfig.py USER

    Generates a kubeconfig file for the specified user, based on the current
    context.
""".strip()

import base64
import sys
from subprocess import run

import yaml


def main():
    user = sys.argv[1]
    kubeconfig = yaml.safe_load(
        run(GET_LOCAL_KUBECONFIG, capture_output=True, check=True).stdout.decode(
            "utf-8"
        )
    )

    get_secret_name = GET_SECRET_NAME.copy()
    get_secret_name[2] = f"serviceaccount/{user}"
    secret_name = run(get_secret_name, capture_output=True, check=True).stdout.decode(
        "utf-8"
    )

    get_token = GET_TOKEN.copy()
    get_token[3] = secret_name.strip(" \n'")
    token = base64.b64decode(
        run(get_token, capture_output=True, check=True).stdout.decode("utf-8")
    ).decode("utf-8")

    kubeconfig["users"] = [{"name": user, "user": {"token": token.strip(" \n'")}}]
    kubeconfig["contexts"][0]["context"]["user"] = user

    with open(f"../{user}-kubeconfig.yaml", "w") as f:
        yaml.dump(kubeconfig, f)

    print(f"Wrote kubeconfig for `{user}` to `{user}-kubeconfig.yaml`")


if len(sys.argv) < 2:
    print(HELP_TEXT)
    sys.exit(1)

main()
