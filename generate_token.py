#!/bin/env python
import secrets
import sys
from math import ceil

LENGTH = int(sys.argv[1]) if len(sys.argv) >= 2 and sys.argv[1] != "--" else 64
FILE_NAME = sys.argv[2] if len(sys.argv) >= 3 else "PASSWORD.txt"

# According to the docs, each byte is 1.3 characters due to base 64.
GENERATED_LENGTH = ceil(LENGTH / 1.3) + 1

with open(FILE_NAME, "w") as file:
    file.write(secrets.token_urlsafe(GENERATED_LENGTH)[:LENGTH])

print(f"Generated a {LENGTH} characters secret in `{FILE_NAME}`")
