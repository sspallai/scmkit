# Identity

## Available resources

| Accessor | YAML key | SCM endpoint |
|---|---|---|
| `scm.saml_server_profile` | `saml_server_profiles` | `/config/identity/v1/saml-server-profiles` |
| `scm.ldap_server_profile` | `ldap_server_profiles` | `/config/identity/v1/ldap-server-profiles` |
| `scm.radius_server_profile` | `radius_server_profiles` | `/config/identity/v1/radius-server-profiles` |
| `scm.authentication_profile` | `authentication_profiles` | `/config/identity/v1/authentication-profiles` |

## SAML Server Profile

```yaml
saml_server_profiles:
  - name: my-idp
    folder: Prisma Access
    entity_id: "https://idp.example.com"
    certificate: my-cert
    sso_url: "https://idp.example.com/sso"
    validate_idp_certificate: true
```

## LDAP Server Profile

```yaml
ldap_server_profiles:
  - name: corp-ldap
    folder: Prisma Access
    server:
      - name: ldap-primary
        address: "ldap.corp.example.com"
        port: 389
    base_dn: "DC=corp,DC=example,DC=com"
    type: active-directory
```

## Authentication Profile

```yaml
authentication_profiles:
  - name: saml-auth
    folder: Prisma Access
    method:
      saml:
        server_profile: my-idp
```
