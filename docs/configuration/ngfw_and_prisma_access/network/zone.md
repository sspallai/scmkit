# Zone

| | |
|---|---|
| **Accessor** | `scm.zone` |
| **Class** | `Zone` |
| **Endpoint** | `/config/network/v1/zones` |
| **YAML key** | `zones` |

## Examples

```python
# List
zones = scm.zone.list(folder="Prisma Access")

# Get by name
zone = scm.zone.get("trust", folder="Prisma Access")

# Create
scm.zone.create({
    "name": "trust",
    "folder": "Prisma Access",
    "network": {"layer3": ["ethernet1/1", "ethernet1/2"]},
    "enable_user_identification": True,
})

# Update by name
scm.zone.update_by_name("trust", folder="Prisma Access",
                         enable_user_identification=False)

# Delete by name
scm.zone.delete_by_name("trust", folder="Prisma Access")

# Bulk from YAML
scm.zone.create_from_yaml("tests/data/zones.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
zones:
  - name: trust
    network:
      layer3:
        - ethernet1/1
        - ethernet1/2
    enable_user_identification: true

  - name: untrust
    network:
      layer3:
        - ethernet1/3
    enable_user_identification: false
```
