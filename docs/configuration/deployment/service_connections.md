# Service Connections

| | |
|---|---|
| **Accessor** | `scm.service_connections` |
| **Class** | `ServiceConnections` |
| **Endpoint** | `/config/network/v1/service-connections` |
| **YAML key** | `service_connections` |
| **Default folder** | `Service Connections` |

!!! note
    The default folder is `Service Connections` (not `Prisma Access`). This is injected automatically by the resource class.

## Examples

```python
# List
connections = scm.service_connections.list()

# Get by name
conn = scm.service_connections.get("dc-link")

# Create
scm.service_connections.create({
    "name": "dc-link",
    "folder": "Service Connections",
    "region": "us-east-1",
    "ipsec_tunnel": "dc-tunnel",
    "subnets": ["10.100.0.0/16"],
    "bgp_peer": {
        "local_ip_address": "169.254.0.1",
        "peer_ip_address": "169.254.0.2",
    },
})

# Update by name
scm.service_connections.update_by_name("dc-link",
                                        subnets=["10.100.0.0/16", "10.101.0.0/16"])

# Delete by name
scm.service_connections.delete_by_name("dc-link")

# Bulk from YAML
scm.service_connections.create_from_yaml("tests/data/service_connections.yaml")
```

## YAML Format

```yaml
folder: Service Connections
service_connections:
  - name: dc-link
    region: us-east-1
    ipsec_tunnel: dc-tunnel
    subnets:
      - 10.100.0.0/16
    bgp_peer:
      local_ip_address: 169.254.0.1
      peer_ip_address: 169.254.0.2
```
