#!/bin/bash
shopt -s nullglob

for file in *-origin-cert.pem; do
  origin=$(echo $file | sed s/-origin-cert\.pem//)
  echo Creating TLS secret for $(echo $origin | sed "s/\(.*\)-/\1\./")

  kubectl delete secret $origin-tls > /dev/null 2>&1
  kubectl create secret generic $origin-tls --from-file=tls.crt=$origin-origin-cert.pem --from-file=tls.key=$origin-origin-key.key
done

for file in *-ca-cert.pem; do
  authority=$(echo $file | sed s/-ca-cert\.pem//)
  echo Creating CA secret for $authority

  kubectl delete secret $authority-ca 2&>1 > /dev/null
  kubectl create secret generic $authority-ca --from-file=ca.crt=$file
done