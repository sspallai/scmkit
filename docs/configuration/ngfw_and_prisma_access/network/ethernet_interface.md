# Ethernet Interface

| | |
|---|---|
| **Accessor** | `scm.ethernet_interface` |
| **Class** | `EthernetInterface` |
| **Endpoint** | `/config/network/v1/ethernet-interfaces` |
| **YAML key** | `ethernet_interfaces` |

## Examples

```python
# List
interfaces = scm.ethernet_interface.list(folder="Prisma Access")

# Get by name
iface = scm.ethernet_interface.get("ethernet1/1", folder="Prisma Access")

# Create — Layer 3
scm.ethernet_interface.create({
    "name": "ethernet1/1",
    "folder": "Prisma Access",
    "layer3": {
        "ip": [{"name": "192.168.1.1/24"}],
        "mtu": 1500,
    },
    "comment": "LAN interface",
})

# Update by name
scm.ethernet_interface.update_by_name("ethernet1/1", folder="Prisma Access",
                                       comment="Updated LAN interface")

# Delete by name
scm.ethernet_interface.delete_by_name("ethernet1/1", folder="Prisma Access")

# Bulk from YAML
scm.ethernet_interface.create_from_yaml("tests/data/ethernet_interfaces.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
ethernet_interfaces:
  - name: ethernet1/1
    layer3:
      ip:
        - name: 192.168.1.1/24
      mtu: 1500
    comment: LAN interface

  - name: ethernet1/2
    layer3:
      ip:
        - name: 10.0.0.1/30
      mtu: 1500
    comment: WAN interface
```
