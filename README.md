# IllumiDesk Containers

All things IllumiDesk containers! In addition to the source Dockerfiles, this repo contains some basic examples on how to use containers with `docker` and `docker-compose`. However, the `grader-setup` services is configured to work with Kubernetes since it relies on the `kubectl` Python client.

Future versions may contain a basic Kubernetes-based setup however for these scenarios we recommend using [IllumiDesk's helm chart](https://github.com/illumidesk/helm-chart).

## Requirements

For docker-compose based setup:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

> **NOTE**: refer to README in the kubernetes folder for the kubernetes POC instructions.

## Docker-Compose

This setup uses docker-compose to launch a JupyterHub instance configure with Postgres. This helps validates custom configurations and assets, such as custom html templates.

## Build, Launch, Test

Install requirements:

1. Install [docker-compose](https://docs.docker.com/compose/install/)

2. Define Environment Variables

- Copy `.env.example` to `.env`
- Update values in `.env`. Sensible defaults are provided to enable basic launches.

3. Build:

```bash
docker-compose build --no-cache
```

> **NOTE**: the `illumidesk/jupyterhub:chp` image that runs with the `docker-compose` version includes the `CHP - Configurable HTTP Proxy`. The standard version of the `illumidesk/jupyterhub:latest` is configured for Kubernetes and therefore will not run with a standard `docker` image.

4. Start:

```bash
docker-compose up -d
```

- Edit the `jupyterhub/jupyterhub_config.py` configuration file to update JupyterHub's configuration. Then restart the `jupyterhub` container with:

```bash
docker-compose restart jupyterhub
```

## Custom Options

1. Update the `.env` file with your values:
    - `JUPYTERHUB_HOST`: the external facing JupyterHub host URL. Defaults to `http://localhost:8000`.
    - `JUPYTERHUB_CRYPT_KEY`: `JUPYTERHUB_CRYPT_KEY`: the JupyterHub crytographic key used to encrypt the `auth_state` when the authentication dictionary is persisted from the Authenticator to the Spawner using the `JupyterHub.auth_state_enabled = True` setting. Create a secure random string with the `openssl rand -hex 32` command from your preferred terminal. If you don't have access to the `openssl` command, any random value should suffice. **However, please use a secure value for Production!**
    - `POSTGRES_DB`: the database name. Defaults to `jupyterhub`.
    - `POSTGRES_USER`: the database's username. Defaults to `jupyterhub`.
    - `POSTGRES_PASSWORD`: the database's password. Defaults to `password`.
    - `POSTGRES_HOST`: the database host. Defaults to `postgres-hub`.
    - `OAUTH_CLIENT_ID`: the value of the OAuth2 client.
    - `OAUTH_CLIENT_SECRET`: secure random secret created by the OIDC/OAuth2 Authorization Server when setting up a the client.
    - `OAUTH_CALLBACK_URL`: defaults to ${JUPYTERHUB_HOST}/hub/oauth_callback which is the standard URL for Authenticators that inherit from the `OAuthenticator` class.
    - `OAUTH2_AUTHORIZE_URL`: defaults to `None`.
    - `OAUTH2_TOKEN_URL`: defaults to `None`.
    - `OAUTH2_TLS_VERIFY`: defaults to `False`
    - `GENERICAUTH_LOGIN_SERVICE_NAME`: defaults to `Custom`.
    - `GENERICAUTH_USERDATA_URL`: defaults to `None`.
    - `GENERICAUTH_USERDATA_METHOD`: defaults to `GET`
    - `GENERICAUTH_USERNAME_KEY`: defaults to `preferred_username`.S

## License

MIT
