# Profile Group

| | |
|---|---|
| **Accessor** | `scm.profile_group` |
| **Class** | `ProfileGroup` |
| **Endpoint** | `/config/security/v1/profile-groups` |
| **YAML key** | `profile_groups` |

!!! warning "Field name aliases"
    The API uses different field names than what you might expect. scmkit renames them automatically:

    | Use in YAML/Python | API field name |
    |---|---|
    | `virus_and_wildfire_analysis` | `virus_and_wildfire_analysis` |
    | `dns_security` | `dns_security` |

    Do **not** use `wildfire_analysis` or `dns_security_profile` — the sanitizer renames these silently.

## Examples

```python
# List
groups = scm.profile_group.list(folder="Prisma Access")

# Get by name
grp = scm.profile_group.get("strict-security", folder="Prisma Access")

# Create
scm.profile_group.create({
    "name": "strict-security",
    "folder": "Prisma Access",
    "virus_and_wildfire_analysis": "strict-wildfire",
    "spyware": "strict-atp",
    "vulnerability": "strict-vuln",
    "url_filtering": "strict-url",
    "file_blocking": "block-executables",
    "dns_security": "strict-dns",
    "data_filtering": "dlp-profile",
})

# Update by name
scm.profile_group.update_by_name("strict-security", folder="Prisma Access",
                                   url_filtering="updated-url-profile")

# Delete by name
scm.profile_group.delete_by_name("strict-security", folder="Prisma Access")

# Bulk from YAML
scm.profile_group.create_from_yaml("tests/data/profile_groups.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
profile_groups:
  - name: strict-security
    virus_and_wildfire_analysis: strict-wildfire
    spyware: strict-atp
    vulnerability: strict-vuln
    url_filtering: strict-url
    file_blocking: block-executables
    dns_security: strict-dns

  - name: basic-security
    spyware: default
    vulnerability: default
    url_filtering: default
```

## Referencing a Profile Group in Security Rules

```yaml
# security_rules.yaml
folder: Prisma Access
security_rules:
  - name: allow-with-inspection
    source: ["any"]
    destination: ["any"]
    application: ["any"]
    service: ["application-default"]
    action: allow
    profile_setting:
      group:
        - strict-security     # ← reference by name
```
