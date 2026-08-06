# SAML Server Profile

| | |
|---|---|
| **Accessor** | `scm.saml_server_profile` |
| **Class** | `SamlServerProfile` |
| **Endpoint** | `/config/identity/v1/saml-server-profiles` |
| **YAML key** | `saml_server_profiles` |

## Examples

```python
# List
profiles = scm.saml_server_profile.list(folder="Prisma Access")

# Get by name
profile = scm.saml_server_profile.get("okta-saml", folder="Prisma Access")

# Create
scm.saml_server_profile.create({
    "name": "okta-saml",
    "folder": "Prisma Access",
    "entity_id": "https://idp.okta.com/exk123",
    "sso_url": "https://corp.okta.com/app/sso/saml",
    "sso_bindings": "post",
    "certificate": "okta-idp-cert",
    "validate_idp_certificate": True,
    "want_auth_requests_signed": False,
})

# Update by name
scm.saml_server_profile.update_by_name("okta-saml", folder="Prisma Access",
                                        want_auth_requests_signed=True)

# Delete by name
scm.saml_server_profile.delete_by_name("okta-saml", folder="Prisma Access")

# Bulk from YAML
scm.saml_server_profile.create_from_yaml("tests/data/saml_server_profiles.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
saml_server_profiles:
  - name: okta-saml
    entity_id: https://idp.okta.com/exk123
    sso_url: https://corp.okta.com/app/sso/saml
    sso_bindings: post
    certificate: okta-idp-cert
    validate_idp_certificate: true
    want_auth_requests_signed: false
```
