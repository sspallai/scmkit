# DNS Security Profile

| | |
|---|---|
| **Accessor** | `scm.dns_security_profile` |
| **Class** | `DnsSecurityProfile` |
| **Endpoint** | `/config/security/v1/dns-security-profiles` |
| **YAML key** | `dns_security_profiles` |

!!! warning
    Domain-type EDLs must be listed under `botnet_domains.lists` — **not** under `rules[].category`. EDL type must be `domain`.

## Examples

```python
# List
profiles = scm.dns_security_profile.list(folder="Prisma Access")

# Get by name
profile = scm.dns_security_profile.get("strict-dns", folder="Prisma Access")

# Create
scm.dns_security_profile.create({
    "name": "strict-dns",
    "folder": "Prisma Access",
    "description": "DNS Security with EDL sinkholing",
    "botnet_domains": {
        "lists": [
            {
                "name": "bad-domains",   # references a domain-type EDL
                "action": {"sinkhole": {}},
                "packet_capture": "single-packet",
            }
        ],
        "sinkhole": {
            "ipv4_address": "pan-sinkhole-default-ip",
            "ipv6_address": "::1",
        },
        "threat_exception": [],
    },
})

# Update by name
scm.dns_security_profile.update_by_name("strict-dns", folder="Prisma Access",
                                         description="Updated DNS security profile")

# Delete by name
scm.dns_security_profile.delete_by_name("strict-dns", folder="Prisma Access")

# Bulk from YAML
scm.dns_security_profile.create_from_yaml("tests/data/dns_security_profiles.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
dns_security_profiles:
  - name: strict-dns
    description: DNS Security with EDL sinkholing
    botnet_domains:
      lists:
        - name: bad-domains       # must be a domain-type EDL
          action:
            sinkhole: {}
          packet_capture: single-packet
      sinkhole:
        ipv4_address: pan-sinkhole-default-ip
        ipv6_address: "::1"
      threat_exception: []
```
