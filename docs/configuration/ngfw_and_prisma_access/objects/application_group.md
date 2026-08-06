# Application Group

| | |
|---|---|
| **Accessor** | `scm.application_group` |
| **Class** | `ApplicationGroup` |
| **Endpoint** | `/config/objects/v1/application-groups` |
| **YAML key** | `application_groups` |

## Examples

```python
# List
groups = scm.application_group.list(folder="Prisma Access")

# Get by name
grp = scm.application_group.get("saas-apps", folder="Prisma Access")

# Create
scm.application_group.create({
    "name": "saas-apps",
    "folder": "Prisma Access",
    "members": ["office365", "salesforce", "slack"],
})

# Update by name
scm.application_group.update_by_name("saas-apps", folder="Prisma Access",
                                      members=["office365", "salesforce", "slack", "zoom"])

# Delete by name
scm.application_group.delete_by_name("saas-apps", folder="Prisma Access")

# Bulk from YAML
scm.application_group.create_from_yaml("tests/data/application_groups.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
application_groups:
  - name: saas-apps
    members:
      - office365
      - salesforce
      - slack

  - name: collaboration-tools
    members:
      - zoom
      - webex
      - teams
```
