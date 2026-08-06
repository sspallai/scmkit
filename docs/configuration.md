# Configuration

## Config file

Create `scm_config.yaml` in your working directory (or `~/.scm/config.yaml`).
The file is auto-discovered; you can also pass an explicit path to `from_config()`.

```yaml
scm:
  client_id:     "sa@<tsg_id>.iam.panserviceaccount.com"
  client_secret: "<secret>"
  tsg_id:        "<tsg_id>"

  # QA environment
  token_url: "https://auth.qa.appsvc.paloaltonetworks.com/am/oauth2/access_token"
  base_url:  "https://qa.api.sase.paloaltonetworks.com"
  log_base_url: "https://pa-api-us-qa01.tools.panclouddev.com"

  # Production (swap the three lines above)
  # token_url: "https://auth.apps.paloaltonetworks.com/am/oauth2/access_token"
  # base_url:  "https://api.sase.paloaltonetworks.com"
  # log_base_url: ""

  timeout:     30   # seconds; optional, default 30
  max_retries: 3    # optional, default 3

# Enterprise DLP service — required only for dlp_data_pattern / dlp_data_profile.
# Omit if DLP patterns/profiles are not used.
# dlp:
#   base_url: "https://<dlp-service-host>/"
```

## Config discovery order

1. Explicit path: `SCMSession.from_config("path/to/scm_config.yaml")`
2. `SCM_CONFIG` environment variable
3. `./scm_config.yaml` in the current directory
4. `~/.scm/config.yaml`

## Environment variables

All config values can be set or overridden via environment variables.

| Variable | Config key |
|---|---|
| `SCM_CLIENT_ID` | `scm.client_id` |
| `SCM_CLIENT_SECRET` | `scm.client_secret` |
| `SCM_TSG_ID` | `scm.tsg_id` |
| `SCM_BASE_URL` | `scm.base_url` |
| `SCM_TOKEN_URL` | `scm.token_url` |
| `SCM_LOG_BASE_URL` | `scm.log_base_url` |
| `SCM_DLP_BASE_URL` | `dlp.base_url` |

## Authentication

scmkit uses **OAuth 2.0 client credentials**. A token is fetched at session
creation and automatically refreshed 60 seconds before expiry. No manual
token management is needed.

```python
from scmkit import SCMSession

# From config file
scm = SCMSession.from_config("scm_config.yaml")

# From explicit credentials
scm = SCMSession(
    client_id="sa@123.iam.panserviceaccount.com",
    client_secret="<secret>",
    tsg_id="123",
    base_url="https://qa.api.sase.paloaltonetworks.com",
    token_url="https://auth.qa.appsvc.paloaltonetworks.com/am/oauth2/access_token",
)
```

## Session lifecycle

```python
# Use as context manager (auto-closes HTTP connection)
with SCMSession.from_config() as scm:
    scm.edl.list()

# Or close manually
scm = SCMSession.from_config()
scm.edl.list()
scm.close()
```
