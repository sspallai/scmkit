# Service

| | |
|---|---|
| **Accessor** | `scm.service` |
| **Class** | `Service` |
| **Endpoint** | `/config/objects/v1/services` |
| **YAML key** | `services` |

## Examples

```python
# List
services = scm.service.list(folder="Prisma Access")

# Get by name
svc = scm.service.get("svc-http-8080", folder="Prisma Access")

# Create — TCP service
scm.service.create({
    "name": "svc-http-8080",
    "folder": "Prisma Access",
    "protocol": {"tcp": {"port": "8080"}},
    "description": "Custom HTTP on 8080",
})

# Create — TCP port range
scm.service.create({
    "name": "svc-ephemeral",
    "folder": "Prisma Access",
    "protocol": {"tcp": {"port": "8080-8090", "source_port": "1024-65535"}},
})

# Create — UDP service
scm.service.create({
    "name": "svc-custom-udp",
    "folder": "Prisma Access",
    "protocol": {"udp": {"port": "5000-5010"}},
})

# Update by name
scm.service.update_by_name("svc-http-8080", folder="Prisma Access",
                            description="Updated description")

# Delete by name
scm.service.delete_by_name("svc-http-8080", folder="Prisma Access")

# Bulk from YAML
scm.service.create_from_yaml("tests/data/services.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
services:
  - name: svc-http-8080
    protocol:
      tcp:
        port: "8080"
    description: Custom HTTP on 8080

  - name: svc-tcp-range
    protocol:
      tcp:
        port: "8080-8090"
        source_port: "1024-65535"

  - name: svc-custom-udp
    protocol:
      udp:
        port: "5000-5010"
```
