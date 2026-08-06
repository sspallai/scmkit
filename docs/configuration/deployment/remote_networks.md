# Remote Networks

| | |
|---|---|
| **Accessor** | `scm.remote_networks` |
| **Class** | `RemoteNetworks` |
| **Endpoint** | `/config/network/v1/remote-networks` |
| **YAML key** | `remote_networks` |
| **Default folder** | `Remote Networks` |

!!! note
    The default folder is `Remote Networks` (not `Prisma Access`). This is injected automatically by the resource class.

## Examples

```python
# List (uses "Remote Networks" folder by default)
networks = scm.remote_networks.list()

# Get by name
net = scm.remote_networks.get("branch-site-a")

# Create
scm.remote_networks.create({
    "name": "branch-site-a",
    "folder": "Remote Networks",
    "region": "us-east-1",
    "ecmp_load_balancing": "disable",
    "ipsec_tunnel": "branch-a-tunnel",
    "subnets": ["192.168.10.0/24", "192.168.11.0/24"],
})

# Update by name
scm.remote_networks.update_by_name("branch-site-a",
                                    subnets=["192.168.10.0/24"])

# Delete by name
scm.remote_networks.delete_by_name("branch-site-a")

# Bulk from YAML
scm.remote_networks.create_from_yaml("tests/data/remote_networks.yaml")
```

## YAML Format

```yaml
folder: Remote Networks
remote_networks:
  - name: branch-site-a
    region: us-east-1
    ecmp_load_balancing: disable
    ipsec_tunnel: branch-a-tunnel
    subnets:
      - 192.168.10.0/24
      - 192.168.11.0/24

  - name: branch-site-b
    region: us-west-2
    ecmp_load_balancing: disable
    ipsec_tunnel: branch-b-tunnel
    subnets:
      - 10.20.0.0/24
```
