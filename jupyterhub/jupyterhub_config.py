""" Configuration file for jupyterhub. """
import os

from dotenv import load_dotenv

from oauthenticator.generic import GenericOAuthenticator


load_dotenv()


c.JupyterHub.allow_root = True
c.JupyterHub.allow_origin = '*'

# Set port and IP
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000

# Set log level
c.Application.log_level = 'DEBUG'

# Header settings for iFrame and SameSite
c.JupyterHub.tornado_settings = {
    "headers": {"Content-Security-Policy": "frame-ancestors 'self' *"},
    "cookie_options": {"SameSite": "None", "Secure": True},
}

# Upgrade the database automatically on start
c.JupyterHub.upgrade_db = True

# Database with Postgres
c.JupyterHub.db_url = 'postgresql://jupyterhub:{password}@{host}/{db}'.format(
    host=os.environ['POSTGRES_HOST'],
    password=os.environ['POSTGRES_PASSWORD'],
    db=os.environ['POSTGRES_DB'],
)

# Set the authenticator. Uncomment the GenericOAuthenticator to test authentication with OIDC/OAuth2.
c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'
# c.JupyterHub.authenticator_class = GenericOAuthenticator

# Set the spawner to the local process spawner
c.JupyterHub.spawner_class = 'jupyterhub.spawner.SimpleLocalProcessSpawner'

# Custom logo file
c.JupyterHub.logo_file = '/home/ubuntu/jhubui/extra-assets/images/illumidesk.png'

# User info
c.Authenticator.admin_users = {'foo'}
c.Authenticator.auto_login = False
c.Authenticator.allowed_users = {'foo', 'bizz', 'bazz'}

# Verify TLS certificates.
if os.environ.get('OAUTH2_TLS_VERIFY') == 'True':
    c.OAuthenticator.tls_verify = True
else:
    c.OAuthenticator.tls_verify = False

# OAuthenticator settings for OAuth2
c.OAuthenticator.client_id = os.environ.get('OAUTH_CLIENT_ID') or 'illumidesk-hub'
c.OAuthenticator.client_secret = os.environ.get('OAUTH_CLIENT_SECRET')
c.OAuthenticator.oauth_callback_url = os.environ.get('OAUTH_CALLBACK_URL') or 'http://127.0.0.1/hub/oauth_callback'
c.OAuthenticator.authorize_url = os.environ.get('OAUTH2_AUTHORIZE_URL')
c.OAuthenticator.token_url = os.environ.get('OAUTH2_TOKEN_URL')
c.OAuthenticator.enable_auth_state = True

# Login service name
c.GenericOAuthenticator.login_service = os.environ.get('GENERICAUTH_LOGIN_SERVICE_NAME') or 'Custom'
# TODO: clarify scopes
c.GenericOAuthenticator.scope = ['openid']
c.GenericOAuthenticator.userdata_url = os.environ.get('OAUTH2_USERDATA_URL')
c.GenericOAuthenticator.userdata_method = os.environ.get('GENERICAUTH_USERDATA_METHOD') or 'GET'
c.GenericOAuthenticator.userdata_params = { 'state': 'state' }
c.GenericOAuthenticator.username_key = os.environ.get('OAUTH2_USERNAME_KEY') or 'preferred_username'
