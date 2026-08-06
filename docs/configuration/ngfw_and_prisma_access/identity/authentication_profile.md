# Authentication Profile

| | |
|---|---|
| **Accessor** | `scm.authentication_profile` |
| **Class** | `AuthenticationProfile` |
| **Endpoint** | `/config/identity/v1/authentication-profiles` |
| **YAML key** | `authentication_profiles` |

## Examples

```python
# List
profiles = scm.authentication_profile.list(folder="Prisma Access")

# Get by name
profile = scm.authentication_profile.get("ldap-auth", folder="Prisma Access")

# Create
scm.authentication_profile.create({
    "name": "ldap-auth",
    "folder": "Prisma Access",
    "method": {"ldap": {"server_profile": "corp-ldap", "login_attribute": "sAMAccountName"}},
    "allow_list": ["all"],
})

# Update by name
scm.authentication_profile.update_by_name("ldap-auth", folder="Prisma Access",
                                            allow_list=["domain-users"])

# Delete by name
scm.authentication_profile.delete_by_name("ldap-auth", folder="Prisma Access")

# Bulk from YAML
scm.authentication_profile.create_from_yaml("tests/data/authentication_profiles.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
authentication_profiles:
  - name: ldap-auth
    method:
      ldap:
        server_profile: corp-ldap
        login_attribute: sAMAccountName
    allow_list:
      - all

  - name: radius-auth
    method:
      radius:
        server_profile: corp-radius
    allow_list:
      - all
```
