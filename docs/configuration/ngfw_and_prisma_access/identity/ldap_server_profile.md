# LDAP Server Profile

| | |
|---|---|
| **Accessor** | `scm.ldap_server_profile` |
| **Class** | `LdapServerProfile` |
| **Endpoint** | `/config/identity/v1/ldap-server-profiles` |
| **YAML key** | `ldap_server_profiles` |

## Examples

```python
# List
profiles = scm.ldap_server_profile.list(folder="Prisma Access")

# Get by name
profile = scm.ldap_server_profile.get("corp-ldap", folder="Prisma Access")

# Create
scm.ldap_server_profile.create({
    "name": "corp-ldap",
    "folder": "Prisma Access",
    "server": [{"name": "dc1", "address": "dc1.corp.example.com", "port": 389}],
    "base": "dc=corp,dc=example,dc=com",
    "type": "active-directory",
    "bind_dn": "cn=svc-ldap,ou=service-accounts,dc=corp,dc=example,dc=com",
    "bind_password": "secret",
    "ssl": False,
})

# Update by name
scm.ldap_server_profile.update_by_name("corp-ldap", folder="Prisma Access",
                                        ssl=True)

# Delete by name
scm.ldap_server_profile.delete_by_name("corp-ldap", folder="Prisma Access")

# Bulk from YAML
scm.ldap_server_profile.create_from_yaml("tests/data/ldap_server_profiles.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
ldap_server_profiles:
  - name: corp-ldap
    server:
      - name: dc1
        address: dc1.corp.example.com
        port: 389
    base: dc=corp,dc=example,dc=com
    type: active-directory
    bind_dn: cn=svc-ldap,ou=service-accounts,dc=corp,dc=example,dc=com
    bind_password: secret
    ssl: false
```
