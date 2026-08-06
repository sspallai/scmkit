# Tag

| | |
|---|---|
| **Accessor** | `scm.tag` |
| **Class** | `Tag` |
| **Endpoint** | `/config/objects/v1/tags` |
| **YAML key** | `tags` |

## Examples

```python
# List
tags = scm.tag.list(folder="Prisma Access")

# Get by name
tag = scm.tag.get("production", folder="Prisma Access")

# Create
scm.tag.create({
    "name": "production",
    "folder": "Prisma Access",
    "color": "Red",
    "comments": "Production workloads",
})

# Update by name
scm.tag.update_by_name("production", folder="Prisma Access",
                        comments="All production workloads")

# Delete by name
scm.tag.delete_by_name("production", folder="Prisma Access")

# Bulk from YAML
scm.tag.create_from_yaml("tests/data/tags.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
tags:
  - name: production
    color: Red
    comments: Production workloads

  - name: web-server
    color: Blue

  - name: dmz
    color: Orange
```
