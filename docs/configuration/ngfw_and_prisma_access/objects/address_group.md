# Address Group

| | |
|---|---|
| **Accessor** | `scm.address_group` |
| **Class** | `AddressGroup` |
| **Endpoint** | `/config/objects/v1/address-groups` |
| **YAML key** | `address_groups` |

## Examples

```python
# List all address groups
groups = scm.address_group.list(folder="Prisma Access")

# Get by name
grp = scm.address_group.get("internal-hosts", folder="Prisma Access")

# Create — static group (references existing address objects)
scm.address_group.create({
    "name": "internal-hosts",
    "folder": "Prisma Access",
    "static": ["corp-network", "branch-range"],
    "description": "All internal hosts",
})

# Create — dynamic group (tag-based filter)
scm.address_group.create({
    "name": "tagged-web-servers",
    "folder": "Prisma Access",
    "dynamic": {"filter": "'web-server' and 'production'"},
})

# Update by name
scm.address_group.update_by_name("internal-hosts", folder="Prisma Access",
                                   static=["corp-network", "branch-range", "dc-subnet"])

# Delete by name
scm.address_group.delete_by_name("internal-hosts", folder="Prisma Access")

# Bulk from YAML
scm.address_group.create_from_yaml("tests/data/address_groups.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
address_groups:
  - name: internal-hosts
    static:
      - corp-network
      - branch-range
    description: All internal hosts

  - name: tagged-web-servers
    dynamic:
      filter: "'web-server' and 'production'"
```

## Group Types

| Type | Field | Description |
|---|---|---|
| Static | `static` | List of address object names |
| Dynamic | `dynamic.filter` | Tag expression evaluated at policy match time |
