# NAT Rule

| | |
|---|---|
| **Accessor** | `scm.nat_rule` |
| **Class** | `NatRule` |
| **Endpoint** | `/config/network/v1/nat-rules` |
| **YAML key** | `nat_rules` |

## Examples

```python
# List pre-rules
rules = scm.nat_rule.list(folder="Prisma Access", rulebase="pre")

# Get by name
rule = scm.nat_rule.get("outbound-nat", folder="Prisma Access")

# Create — source NAT (SNAT)
scm.nat_rule.create({
    "name": "outbound-nat",
    "folder": "Prisma Access",
    "rulebase": "pre",
    "source_zone": ["trust"],
    "destination_zone": "untrust",
    "source": ["internal-hosts"],
    "destination": ["any"],
    "service": "any",
    "nat_type": "ipv4",
    "source_translation": {
        "dynamic_ip_and_port": {
            "interface_address": {"interface": "ethernet1/1"},
        }
    },
})

# Create — destination NAT (DNAT)
scm.nat_rule.create({
    "name": "inbound-dnat-web",
    "folder": "Prisma Access",
    "rulebase": "pre",
    "source_zone": ["untrust"],
    "destination_zone": "untrust",
    "destination": ["public-ip"],
    "service": "svc-http",
    "nat_type": "ipv4",
    "destination_translation": {
        "translated_address": "web-server-internal",
        "translated_port": 8080,
    },
})

# Update by name
scm.nat_rule.update_by_name("outbound-nat", folder="Prisma Access",
                             description="Updated SNAT rule")

# Delete by name
scm.nat_rule.delete_by_name("outbound-nat", folder="Prisma Access")

# Bulk from YAML
scm.nat_rule.create_from_yaml("tests/data/nat_rules.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
nat_rules:
  - name: outbound-nat
    rulebase: pre
    source_zone:
      - trust
    destination_zone: untrust
    source:
      - internal-hosts
    destination:
      - any
    service: any
    nat_type: ipv4
    source_translation:
      dynamic_ip_and_port:
        interface_address:
          interface: ethernet1/1

  - name: inbound-dnat-web
    rulebase: pre
    source_zone:
      - untrust
    destination_zone: untrust
    destination:
      - public-ip
    service: svc-http
    nat_type: ipv4
    destination_translation:
      translated_address: web-server-internal
      translated_port: 8080
```
