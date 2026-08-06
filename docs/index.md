# scmkit

**scmkit** is a Python package for automating Strata Cloud Manager (SCM) via the REST API.
It covers objects, security profiles, policies, DLP, deployment, and operations
with full YAML-driven idempotent workflows.

---

## Installation

```bash
pip install -e .
```

Requires Python 3.10+.

---

## Quick start

```python
from scmkit import SCMSession

scm = SCMSession.from_config("scm_config.yaml")

# Create resources from YAML (idempotent — safe to re-run)
scm.edl.create_from_yaml("edl_config.yaml")
scm.dns_security_profile.create_from_yaml("profiles.yaml")
scm.profile_group.create_from_yaml("profiles.yaml")
scm.security_rule.create_from_yaml("rules.yaml")

# Commit and wait for completion
scm.push_config.commit(
    folders=["Prisma Access"],
    description="My automated change",
)
```

---

## Core CRUD interface

Every resource exposes the same interface:

| Method | Description |
|---|---|
| `.list(folder)` | List all objects in a folder |
| `.get(name, folder)` | Get by name; returns `None` if not found |
| `.create(payload)` | Create one object |
| `.update(id, payload)` | Update by UUID |
| `.delete(id)` | Delete by UUID |
| `.update_by_name(name, payload, folder)` | Update without knowing the UUID |
| `.delete_by_name(name, folder)` | Delete without knowing the UUID |
| `.apply(payload, on_conflict)` | Create or handle conflict idempotently |
| `.create_from_yaml(yaml_path)` | Load YAML and apply (skip if exists) |
| `.update_from_yaml(yaml_path)` | Load YAML and update existing objects |
| `.delete_from_yaml(yaml_path)` | Load YAML and delete objects |

### `on_conflict` behaviour

| Value | Behaviour |
|---|---|
| `"skip"` | Leave existing unchanged, return it (default for `create_from_yaml`) |
| `"update"` | Overwrite the existing object (default for `apply_from_yaml`) |
| `"fail"` | Raise `SCMAPIError` if the object already exists |

---

## Navigation

- [Configuration](configuration.md) — credentials and config file
- [Objects](configuration/ngfw_and_prisma_access/objects/index.md) — addresses, services, EDLs, …
- [Profiles](configuration/ngfw_and_prisma_access/profiles/index.md) — security profiles and profile groups
- [Policies](configuration/ngfw_and_prisma_access/policies/index.md) — security, NAT, and decryption rules
- [Data Loss Prevention](configuration/data_loss_prevention/index.md) — DLP patterns, profiles, data filtering
- [Network](configuration/ngfw_and_prisma_access/network/index.md) — zones, interfaces, routers
- [Identity](configuration/ngfw_and_prisma_access/identity/index.md) — SAML, LDAP, RADIUS, authentication profiles
- [Deployment](configuration/deployment/index.md) — remote networks, service connections
- [Operations](configuration/operations/index.md) — commit, push status, config snapshots
- [Posture](configuration/posture/index.md) — policy optimizer, cleanup, analyzer
- [Exceptions](exceptions.md) — error handling reference
