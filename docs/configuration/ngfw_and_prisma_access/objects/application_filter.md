# Application Filter

| | |
|---|---|
| **Accessor** | `scm.application_filter` |
| **Class** | `ApplicationFilter` |
| **Endpoint** | `/config/objects/v1/application-filters` |
| **YAML key** | `application_filters` |

## Examples

```python
# List
filters = scm.application_filter.list(folder="Prisma Access")

# Get by name
flt = scm.application_filter.get("high-risk-apps", folder="Prisma Access")

# Create — filter by risk and category
scm.application_filter.create({
    "name": "high-risk-apps",
    "folder": "Prisma Access",
    "risk": [4, 5],
    "category": ["peer-to-peer"],
})

# Create — filter by subcategory and technology
scm.application_filter.create({
    "name": "encrypted-tunnels",
    "folder": "Prisma Access",
    "subcategory": ["encrypted-tunnel"],
    "technology": ["peer-to-peer"],
})

# Update by name
scm.application_filter.update_by_name("high-risk-apps", folder="Prisma Access",
                                       risk=[3, 4, 5])

# Delete by name
scm.application_filter.delete_by_name("high-risk-apps", folder="Prisma Access")

# Bulk from YAML
scm.application_filter.create_from_yaml("tests/data/application_filters.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
application_filters:
  - name: high-risk-apps
    risk:
      - 4
      - 5
    category:
      - peer-to-peer

  - name: encrypted-tunnels
    subcategory:
      - encrypted-tunnel
    technology:
      - peer-to-peer
```
