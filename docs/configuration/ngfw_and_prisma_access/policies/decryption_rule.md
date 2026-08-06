# Decryption Rule

| | |
|---|---|
| **Accessor** | `scm.decryption_rule` |
| **Class** | `DecryptionRule` |
| **Endpoint** | `/config/security/v1/decryption-rules` |
| **YAML key** | `decryption_rules` |

## Examples

```python
# List
rules = scm.decryption_rule.list(folder="Prisma Access")

# Get by name
rule = scm.decryption_rule.get("decrypt-outbound-ssl", folder="Prisma Access")

# Create — SSL Forward Proxy decryption
scm.decryption_rule.create({
    "name": "decrypt-outbound-ssl",
    "folder": "Prisma Access",
    "source_zone": ["trust"],
    "destination_zone": ["untrust"],
    "source": ["any"],
    "destination": ["any"],
    "service": ["any"],
    "action": "decrypt",
    "type": {"ssl_forward_proxy": {}},
    "profile": "strict-decrypt",
})

# Create — no-decrypt exclusion
scm.decryption_rule.create({
    "name": "no-decrypt-finance",
    "folder": "Prisma Access",
    "source_zone": ["trust"],
    "destination_zone": ["untrust"],
    "destination": ["finance-sites"],
    "action": "no-decrypt",
})

# Update by name
scm.decryption_rule.update_by_name("decrypt-outbound-ssl", folder="Prisma Access",
                                    profile="updated-decrypt-profile")

# Delete by name
scm.decryption_rule.delete_by_name("decrypt-outbound-ssl", folder="Prisma Access")

# Bulk from YAML
scm.decryption_rule.create_from_yaml("tests/data/decryption_rules.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
decryption_rules:
  - name: no-decrypt-finance
    source_zone:
      - trust
    destination_zone:
      - untrust
    destination:
      - finance-sites
    action: no-decrypt

  - name: decrypt-outbound-ssl
    source_zone:
      - trust
    destination_zone:
      - untrust
    source:
      - any
    destination:
      - any
    service:
      - any
    action: decrypt
    type:
      ssl_forward_proxy: {}
    profile: strict-decrypt
```
