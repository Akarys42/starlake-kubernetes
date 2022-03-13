# Starlake Kubernetes
The Kubernetes manifest for our k0s cluster [deployed through Ansible](https://git.akarys.me/starlake-ansible).

# Services
## Internal
- [MetalLB](https://metallb.universe.tf/): Bare metal node balancer used to expose nginx to the world.
- mTLS: TLS and CA bundles used by Nginx to ensure the integrity of the connection.
- [Nginx](https://kubernetes.github.io/ingress-nginx/): Middleware used to distribute requests across services.

## Backend
- [PostgreSQL](https://www.postgresql.org/): The database powering most other services.
- [Blackbox](https://github.com/lemonsaurus/blackbox): Periodic backup of our databases.

## Frontend
- Luna: Our private instance of the [StarBot](https://git.akarys.me/StarBot) discord bot.
- [Gurkbot](https://github.com/gurkult/gurkbot/): The open source Discord bot of the [Gurkult](https://gurkult.com) community
- athena-test.com: The online test framework of Athena Formation Conseil.
