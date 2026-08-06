# Address

| | |
|---|---|
| **Accessor** | `scm.address` |
| **Class** | `Address` |
| **Endpoint** | `/config/objects/v1/addresses` |
| **YAML key** | `addresses` |

## Methods

| Method | Description |
|---|---|
| `list(folder)` | List all addresses in a folder |
| `get(name, folder)` | Get by name |
| `create(payload)` | Create a new address |
| `update(id, payload)` | Update by ID |
| `update_by_name(name, folder, **kwargs)` | Update fields by name |
| `delete(id)` | Delete by ID |
| `delete_by_name(name, folder)` | Delete by name |
| `apply(payload, on_conflict)` | Create or update (idempotent) |
| `create_from_yaml(yaml_path, folder)` | Bulk create from YAML file |
| `delete_from_yaml(yaml_path, folder)` | Bulk delete from YAML file |

## Examples

```python
from scmkit import SCMSession

scm = SCMSession.from_config("scm_config.yaml")

# List all addresses
addresses = scm.address.list(folder="Prisma Access")

# Get by name
addr = scm.address.get("corp-network", folder="Prisma Access")

# Create — IP netmask
scm.address.create({
    "name": "corp-network",
    "folder": "Prisma Access",
    "ip_netmask": "10.0.0.0/8",
    "description": "Corporate network range",
})

# Create — IP range
scm.address.create({
    "name": "branch-range",
    "folder": "Prisma Access",
    "ip_range": "192.168.10.1-192.168.10.254",
})

# Create — FQDN
scm.address.create({
    "name": "example-fqdn",
    "folder": "Prisma Access",
    "fqdn": "example.com",
})

# Update by name
scm.address.update_by_name("corp-network", folder="Prisma Access",
                            description="Updated corporate network")

# Delete by name
scm.address.delete_by_name("corp-network", folder="Prisma Access")

# Idempotent apply
scm.address.apply({
    "name": "corp-network",
    "folder": "Prisma Access",
    "ip_netmask": "10.0.0.0/8",
}, on_conflict="skip")

# Bulk create from YAML
scm.address.create_from_yaml("tests/data/addresses.yaml")

# Bulk delete from YAML
scm.address.delete_from_yaml("tests/data/addresses.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
addresses:
  - name: corp-network
    ip_netmask: 10.0.0.0/8
    description: Corporate network range

  - name: branch-range
    ip_range: 192.168.10.1-192.168.10.254

  - name: example-fqdn
    fqdn: example.com

  - name: wildcard-net
    ip_wildcard: 10.20.1.0/0.0.248.255
```

## Address Types

| Field | Example | Description |
|---|---|---|
| `ip_netmask` | `10.0.0.0/8` | CIDR notation or host address |
| `ip_range` | `192.168.1.1-192.168.1.254` | Contiguous IP range |
| `ip_wildcard` | `10.20.1.0/0.0.248.255` | Wildcard mask |
| `fqdn` | `example.com` | Fully qualified domain name |
