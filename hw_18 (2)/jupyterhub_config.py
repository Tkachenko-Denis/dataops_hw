import os
from pathlib import Path

from jupyterhub.app import JupyterHub
from traitlets.config import get_config


c = get_config()

data_dir = Path("/srv/jupyterhub/data")
data_dir.mkdir(parents=True, exist_ok=True)

admin_user = os.environ.get("JUPYTERHUB_ADMIN_USER", "admin")
admin_password = os.environ.get("JUPYTERHUB_ADMIN_PASSWORD", "admin-password")

c.JupyterHub.bind_url = "http://0.0.0.0:8000"
c.JupyterHub.cookie_secret = bytes.fromhex(
    os.environ["JUPYTERHUB_COOKIE_SECRET_HEX"]
)
c.JupyterHub.db_url = f"sqlite:///{data_dir / 'jupyterhub.sqlite'}"
c.JupyterHub.authenticator_class = "dummy"
c.JupyterHub.spawner_class = "simple"
c.JupyterHub.admin_access = True
c.JupyterHub.log_level = "INFO"

c.Authenticator.admin_users = {admin_user}
c.DummyAuthenticator.password = admin_password

c.ConfigurableHTTPProxy.auth_token = os.environ["CONFIGPROXY_AUTH_TOKEN"]
c.Spawner.default_url = "/lab"
c.Spawner.notebook_dir = "/tmp"
