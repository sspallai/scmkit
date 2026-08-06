# Dynamic User Group

| | |
|---|---|
| **Accessor** | `scm.dynamic_user_group` |
| **Class** | `DynamicUserGroup` |
| **Endpoint** | `/config/objects/v1/dynamic-user-groups` |
| **YAML key** | `dynamic_user_groups` |

## Examples

```python
# List
groups = scm.dynamic_user_group.list(folder="Prisma Access")

# Get by name
grp = scm.dynamic_user_group.get("contractors", folder="Prisma Access")

# Create — tag-based user filter
scm.dynamic_user_group.create({
    "name": "contractors",
    "folder": "Prisma Access",
    "filter": "'contractor'",
    "description": "All contractor users",
})

# Update by name
scm.dynamic_user_group.update_by_name("contractors", folder="Prisma Access",
                                       description="External contractor users")

# Delete by name
scm.dynamic_user_group.delete_by_name("contractors", folder="Prisma Access")

# Bulk from YAML
scm.dynamic_user_group.create_from_yaml("tests/data/dynamic_user_groups.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
dynamic_user_groups:
  - name: contractors
    filter: "'contractor'"
    description: All contractor users

  - name: finance-team
    filter: "'finance' and 'full-time'"
    description: Finance department employees
```
