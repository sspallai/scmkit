# Network

## Available resources

| Accessor | YAML key | SCM endpoint |
|---|---|---|
| `scm.zone` | `zones` | `/config/security/v1/zones` |
| `scm.ethernet_interface` | `ethernet_interfaces` | `/config/network/v1/ethernet-interfaces` |
| `scm.logical_router` | `logical_routers` | `/config/network/v1/logical-routers` |
| `scm.dns_proxy` | `dns_proxies` | `/config/network/v1/dns-proxies` |

## Zone

```yaml
zones:
  - name: trust
    folder: Prisma Access
    network:
      layer3: [ethernet1/1]
  - name: untrust
    folder: Prisma Access
    network:
      layer3: [ethernet1/2]
```

## Ethernet Interface

```yaml
ethernet_interfaces:
  - name: ethernet1/1
    folder: Prisma Access
    layer3:
      ip:
        - addr: "10.0.0.1/24"
```
