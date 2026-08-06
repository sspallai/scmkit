# Logical Router

| | |
|---|---|
| **Accessor** | `scm.logical_router` |
| **Class** | `LogicalRouter` |
| **Endpoint** | `/config/network/v1/logical-routers` |
| **YAML key** | `logical_routers` |

## Examples

```python
# List
routers = scm.logical_router.list(folder="Prisma Access")

# Get by name
router = scm.logical_router.get("default-router", folder="Prisma Access")

# Create
scm.logical_router.create({
    "name": "default-router",
    "folder": "Prisma Access",
    "interfaces": ["ethernet1/1", "ethernet1/2"],
    "static_routes": {
        "ip": [
            {
                "name": "default-route",
                "destination": "0.0.0.0/0",
                "nexthop": {"ip_address": "10.0.0.1"},
            }
        ]
    },
})

# Update by name
scm.logical_router.update_by_name("default-router", folder="Prisma Access",
                                   interfaces=["ethernet1/1", "ethernet1/2", "ethernet1/3"])

# Delete by name
scm.logical_router.delete_by_name("default-router", folder="Prisma Access")

# Bulk from YAML
scm.logical_router.create_from_yaml("tests/data/logical_routers.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
logical_routers:
  - name: default-router
    interfaces:
      - ethernet1/1
      - ethernet1/2
    static_routes:
      ip:
        - name: default-route
          destination: 0.0.0.0/0
          nexthop:
            ip_address: 10.0.0.1
```
