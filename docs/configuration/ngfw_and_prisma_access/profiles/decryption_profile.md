# Decryption Profile

| | |
|---|---|
| **Accessor** | `scm.decryption_profile` |
| **Class** | `DecryptionProfile` |
| **Endpoint** | `/config/security/v1/decryption-profiles` |
| **YAML key** | `decryption_profiles` |

## Examples

```python
# List
profiles = scm.decryption_profile.list(folder="Prisma Access")

# Get by name
profile = scm.decryption_profile.get("strict-decrypt", folder="Prisma Access")

# Create
scm.decryption_profile.create({
    "name": "strict-decrypt",
    "folder": "Prisma Access",
    "description": "Strict TLS inspection profile",
    "ssl_forward_proxy": {
        "auto_include_altname": True,
        "block_client_cert": False,
        "block_expired_certificate": True,
        "block_untrusted_issuer": True,
        "block_unknown_cert": True,
        "client_cert_expiry_days": 0,
        "strip_alpn": False,
    },
})

# Update by name
scm.decryption_profile.update_by_name("strict-decrypt", folder="Prisma Access",
                                       description="Updated decryption profile")

# Delete by name
scm.decryption_profile.delete_by_name("strict-decrypt", folder="Prisma Access")

# Bulk from YAML
scm.decryption_profile.create_from_yaml("tests/data/decryption_profiles.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
decryption_profiles:
  - name: strict-decrypt
    description: Strict TLS inspection profile
    ssl_forward_proxy:
      auto_include_altname: true
      block_expired_certificate: true
      block_untrusted_issuer: true
      block_unknown_cert: true
      strip_alpn: false
```
