# Starlake Kubernetes
The Kubernetes manifest for our cluster [deployed through Ansible](https://git.akarys.me/starlake-kubernetes).

This node is running the k0s distribution. It hosts the following services:
- PostgreSQL: The database powering most other services.
- Luna: Our private instance of the [StarBot](https://git.akarys.me/StarBot) discord bot.
- [Gurkbot](https://github.com/gurkult/gurkbot/): The open source Discord bot of the [Gurkult](https://gurkult.com) community
