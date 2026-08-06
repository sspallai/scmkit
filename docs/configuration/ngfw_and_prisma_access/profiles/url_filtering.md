# URL Filtering Profile

| | |
|---|---|
| **Accessor** | `scm.url_filtering_profile` |
| **Class** | `UrlFilteringProfile` |
| **Endpoint** | `/config/security/v1/url-access-profiles` |
| **YAML key** | `url_filtering_profiles` |

## Examples

```python
# List
profiles = scm.url_filtering_profile.list(folder="Prisma Access")

# Get by name
profile = scm.url_filtering_profile.get("strict-url", folder="Prisma Access")

# Create
scm.url_filtering_profile.create({
    "name": "strict-url",
    "folder": "Prisma Access",
    "description": "Block high-risk categories",
    "access_rules": [
        {
            "name": "block-malicious",
            "action": "block",
            "categories": ["malware", "phishing", "command-and-control"],
        },
        {
            "name": "alert-social",
            "action": "alert",
            "categories": ["social-networking"],
        },
    ],
})

# Update by name
scm.url_filtering_profile.update_by_name("strict-url", folder="Prisma Access",
                                          description="Updated URL filtering profile")

# Delete by name
scm.url_filtering_profile.delete_by_name("strict-url", folder="Prisma Access")

# Bulk from YAML
scm.url_filtering_profile.create_from_yaml("tests/data/url_filtering_profiles.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
url_filtering_profiles:
  - name: strict-url
    description: Block high-risk URL categories
    access_rules:
      - name: block-malicious
        action: block
        categories:
          - malware
          - phishing
          - command-and-control

      - name: alert-social
        action: alert
        categories:
          - social-networking
          - personal-sites-and-blogs
```
