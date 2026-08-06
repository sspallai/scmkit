# Application Override Rule

| | |
|---|---|
| **Accessor** | `scm.application_override_rule` |
| **Class** | `ApplicationOverrideRule` |
| **Endpoint** | `/config/security/v1/app-override-rules` |
| **YAML key** | `application_override_rules` |

## Examples

```python
# List
rules = scm.application_override_rule.list(folder="Prisma Access")

# Get by name
rule = scm.application_override_rule.get("override-custom-app", folder="Prisma Access")

# Create
scm.application_override_rule.create({
    "name": "override-custom-app",
    "folder": "Prisma Access",
    "source_zone": ["trust"],
    "destination_zone": ["untrust"],
    "source": ["any"],
    "destination": ["any"],
    "protocol": "tcp",
    "port": [8443],
    "application": "my-custom-app",
})

# Update by name
scm.application_override_rule.update_by_name("override-custom-app",
                                               folder="Prisma Access",
                                               description="Updated override rule")

# Delete by name
scm.application_override_rule.delete_by_name("override-custom-app", folder="Prisma Access")

# Bulk from YAML
scm.application_override_rule.create_from_yaml("tests/data/application_override_rules.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
application_override_rules:
  - name: override-custom-app
    source_zone:
      - trust
    destination_zone:
      - untrust
    source:
      - any
    destination:
      - any
    protocol: tcp
    port:
      - 8443
    application: my-custom-app
```
