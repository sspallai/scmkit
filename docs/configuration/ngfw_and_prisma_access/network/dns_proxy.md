# DNS Proxy

| | |
|---|---|
| **Accessor** | `scm.dns_proxy` |
| **Class** | `DnsProxy` |
| **Endpoint** | `/config/network/v1/dns-proxies` |
| **YAML key** | `dns_proxies` |

## Examples

```python
# List
proxies = scm.dns_proxy.list(folder="Prisma Access")

# Get by name
proxy = scm.dns_proxy.get("default-dns", folder="Prisma Access")

# Create
scm.dns_proxy.create({
    "name": "default-dns",
    "folder": "Prisma Access",
    "interface": ["ethernet1/1"],
    "default": {
        "dns_support": {
            "server": {
                "primary": "8.8.8.8",
                "secondary": "8.8.4.4",
            }
        }
    },
})

# Update by name
scm.dns_proxy.update_by_name("default-dns", folder="Prisma Access",
                              description="Updated DNS proxy")

# Delete by name
scm.dns_proxy.delete_by_name("default-dns", folder="Prisma Access")

# Bulk from YAML
scm.dns_proxy.create_from_yaml("tests/data/dns_proxies.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
dns_proxies:
  - name: default-dns
    interface:
      - ethernet1/1
    default:
      dns_support:
        server:
          primary: 8.8.8.8
          secondary: 8.8.4.4
```
