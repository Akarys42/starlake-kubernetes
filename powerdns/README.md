# PowerDNS Setup

Note: This contains setup required to run PowerDNS. The actual service setup is done on the host, 
and can be found in our [Ansible repository](https://git.akarys.me/starlake-ansible).

## Steps:
1. Expose CoreDNS to a static local IP: `kubectl apply -f coredns-local.yaml`
2. Create a database: `../postgres/generate_database.sh powerdns`
3. Update the password inside the Ansible setup.