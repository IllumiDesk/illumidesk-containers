# IllumiDesk Containers

All things IllumiDesk containers! In addition to the source Dockerfiles, this repo contains some basic examples on how to use containers with `docker` and `docker-compose`. However, the `grader-setup` services is configured to work with Kubernetes since it relies on the `kubectl` Python client.

Future versions may contain a basic Kubernetes-based setup however for these scenarios we recommend using [IllumiDesk's helm chart](https://github.com/illumidesk/helm-chart).

## Requirements

For docker-compose based setup:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

> **NOTE**: refer to README in the kubernetes folder for the kubernetes POC instructions.

## Docker-Compose

This setup has two versions of Docker Compose:

- Dev (`docker-compose-dev.yaml`)
  - Mounts `nginx` and `jupyterhub` configuration files from the local file system
  - Builds the docker images from Dockerfiles located in sub-directories.

- Default (`docker-compose.yaml`)
  - Pulls images located in DockerHub registry

Use the dev version to quickly test different configuration options. Use the default version to launch services with a sensible set of defaults.

## Build, Launch, Test

### Define Environment Variables

1. Copy `.env.example` to `.env`
2. Update values in `.env`. Sensible defaults are provided to enable basic launches.
3. Build:

```bash
docker-compose build --no-cache
```

4. Start:

```bash
docker-compose up -d
```

3. (Optional) Edit configuration files and restart service (container)

- Edit the `nginx/nginx.conf` configuration file to update Nginx's configuration. Then restart the `nginx` container with:

```bash
docker-compose restart nginx
```

- Edit the `jupyterhub/jupyterhub_config.py` configuration file to update JupyterHub's configuration. Then restart the `jupyterhub` container with:

```bash
docker-compose restart jupyterhub
```

### Custom Options

1. Update the `.env` file with your values:
    - `JUPYTERHUB_HOST`: the external facing JupyterHub host URL. Defaults to `http://localhost:8000`.
    - `JUPYTERHUB_CRYPT_KEY`: `JUPYTERHUB_CRYPT_KEY`: the JupyterHub crytographic key used to encrypt the `auth_state` when the authentication dictionary is persisted from the Authenticator to the Spawner using the `JupyterHub.auth_state_enabled = True` setting. Create a secure random string with the `openssl rand -hex 32` command from your preferred terminal. If you don't have access to the `openssl` command, any random value should suffice. **However, please use a secure value for Production!**
    - `KEYCLOAK_INTERNAL_HOST`: the internal Keycloak service scheme, name and port. For example: `https://keycloak:8080`.
    - `KEYCLOAK_EXTERNAL_HOST`: the external Keycloak scheme, host, and port. `https://127.0.0.1:8080`.
    - `KEYCLOAK_REALM`: the Keycloak Realm name. Defaults to `master`.
    - `OAUTH_CLIENT_ID`: the name of the Keycloak client configured with the Keycloak Realm, such as `illumidesk-hub`. Refer to the README in the keycloak folder for instructions on how to set up a keycloak realm.
    - `OAUTH_CLIENT_SECRET`: secure random secret created by Keycloak when setting up a Keycloak client.
    - `OAUTH_CALLBACK_URL`: defaults to ${JUPYTERHUB_HOST}/hub/oauth_callback which is the standard URL for Authenticators that inherit from the `OAuthenticator` class.
    - `OAUTH2_AUTHORIZE_URL`: defaults to `${KEYCLOAK_EXTERNAL_HOST}/auth/realms/${KEYCLOAK_REALM}/protocol/openid-connect/auth`.
    - `OAUTH2_TOKEN_URL`: defaults to `${KEYCLOAK_INTERNAL_HOST}/auth/realms/${KEYCLOAK_REALM}/protocol/openid-connect/token`.
    - `OAUTH2_TLS_VERIFY`: defaults to `False`
    - `GENERICAUTH_LOGIN_SERVICE_NAME`: defaults to `Keycloak`.
    - `GENERICAUTH_USERDATA_URL`: defaults to `${KEYCLOAK_INTERNAL_HOST}/auth/realms/${KEYCLOAK_REALM}/protocol/openid-connect/userinfo`.
    - `GENERICAUTH_USERDATA_METHOD`: defaults to `GET`
    - `GENERICAUTH_USERNAME_KEY`: defaults to `preferred_username`.S
    - `KEYCLOAK_LOGOUT_URL`: defaults to `${KEYCLOAK_INTERNAL_HOST}/auth/realms/${KEYCLOAK_REALM}/protocol/openid-connect/logout`.

## License

MIT
