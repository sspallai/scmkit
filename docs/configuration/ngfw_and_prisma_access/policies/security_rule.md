# Security Rule

| | |
|---|---|
| **Accessor** | `scm.security_rule` |
| **Class** | `SecurityRule` |
| **Endpoint** | `/config/security/v1/security-rules` |
| **YAML key** | `security_rules` |

!!! note
    Rules use a `rulebase` parameter (`pre` or `post`, default `pre`). `log_setting` must reference an existing Log Forwarding Profile object by name.

## Methods

| Method | Description |
|---|---|
| `list(folder, rulebase)` | List all rules in rulebase |
| `get(name, folder, rulebase)` | Get rule by name |
| `create(payload)` | Create a rule (`rulebase` in payload) |
| `update(id, payload)` | Update by ID |
| `update_by_name(name, folder, **kwargs)` | Update fields by name |
| `delete(id)` | Delete by ID |
| `delete_by_name(name, folder)` | Delete by name |
| `apply(payload, on_conflict)` | Create or update (idempotent) |
| `create_from_yaml(yaml_path, folder)` | Bulk create from YAML |

## Examples

```python
# List pre-rules
rules = scm.security_rule.list(folder="Prisma Access", rulebase="pre")

# Get by name
rule = scm.security_rule.get("allow-internet", folder="Prisma Access")

# Create — allow with profile group inspection
scm.security_rule.create({
    "name": "allow-with-inspection",
    "folder": "Prisma Access",
    "rulebase": "pre",
    "source": ["internal-hosts"],
    "destination": ["any"],
    "application": ["any"],
    "service": ["application-default"],
    "action": "allow",
    "profile_setting": {"group": ["strict-security"]},
    "log_setting": "default-logging",
    "log_end": True,
})

# Create — block rule
scm.security_rule.create({
    "name": "block-bad-ips",
    "folder": "Prisma Access",
    "rulebase": "pre",
    "source": ["bad-ips"],
    "destination": ["any"],
    "application": ["any"],
    "service": ["any"],
    "action": "deny",
    "log_end": True,
})

# Update by name — change action
scm.security_rule.update_by_name("allow-internet", folder="Prisma Access", action="deny")

# Delete by name
scm.security_rule.delete_by_name("allow-internet", folder="Prisma Access")

# Bulk from YAML
scm.security_rule.create_from_yaml("tests/data/security_rules.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
security_rules:
  - name: block-bad-ips
    rulebase: pre
    source:
      - bad-ips
    destination:
      - any
    application:
      - any
    service:
      - any
    action: deny
    log_end: true

  - name: allow-with-inspection
    rulebase: pre
    source:
      - internal-hosts
    destination:
      - any
    application:
      - any
    service:
      - application-default
    action: allow
    profile_setting:
      group:
        - strict-security
    log_setting: default-logging
    log_end: true

  - name: block-bad-urls
    rulebase: pre
    source:
      - any
    destination:
      - any
    application:
      - ssl
      - web-browsing
    service:
      - application-default
    action: allow
    profile_setting:
      group:
        - url-only-security
    log_end: true
```

## Key Fields

| Field | Description |
|---|---|
| `rulebase` | `pre` (default) or `post` |
| `source` / `destination` | Address or address group names, or `any` |
| `application` | Application names or `any` |
| `service` | Service names, `application-default`, or `any` |
| `action` | `allow`, `deny`, `drop`, `reset-client`, `reset-server`, `reset-both` |
| `profile_setting.group` | List with one profile group name |
| `log_setting` | Log Forwarding Profile name |
