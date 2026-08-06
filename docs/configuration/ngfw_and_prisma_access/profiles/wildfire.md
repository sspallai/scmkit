# WildFire Anti-Virus Profile

| | |
|---|---|
| **Accessor** | `scm.wildfire_profile` |
| **Class** | `WildfireProfile` |
| **Endpoint** | `/config/security/v1/wildfire-anti-virus-profiles` |
| **YAML key** | `wildfire_profiles` |

!!! note
    When attached via ProfileGroup, use `virus_and_wildfire_analysis` (not `wildfire_analysis`). The sanitizer renames it automatically.

## Examples

```python
# List
profiles = scm.wildfire_profile.list(folder="Prisma Access")

# Get by name
profile = scm.wildfire_profile.get("strict-wildfire", folder="Prisma Access")

# Create
scm.wildfire_profile.create({
    "name": "strict-wildfire",
    "folder": "Prisma Access",
    "description": "WildFire with blocking",
    "rules": [
        {
            "name": "default",
            "direction": "both",
            "analysis": "public-cloud",
            "application": ["any"],
            "file_type": ["any"],
        }
    ],
})

# Update by name
scm.wildfire_profile.update_by_name("strict-wildfire", folder="Prisma Access",
                                     description="Updated WildFire profile")

# Delete by name
scm.wildfire_profile.delete_by_name("strict-wildfire", folder="Prisma Access")

# Bulk from YAML
scm.wildfire_profile.create_from_yaml("tests/data/wildfire_profiles.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
wildfire_profiles:
  - name: strict-wildfire
    description: WildFire analysis for all traffic
    rules:
      - name: default
        direction: both
        analysis: public-cloud
        application:
          - any
        file_type:
          - any
```
