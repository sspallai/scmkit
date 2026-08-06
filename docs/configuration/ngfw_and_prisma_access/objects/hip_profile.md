# HIP Profile

| | |
|---|---|
| **Accessor** | `scm.hip_profile` |
| **Class** | `HipProfile` |
| **Endpoint** | `/config/objects/v1/hip-profiles` |
| **YAML key** | `hip_profiles` |

## Examples

```python
# List
profiles = scm.hip_profile.list(folder="Prisma Access")

# Get by name
profile = scm.hip_profile.get("compliant-endpoints", folder="Prisma Access")

# Create — combines multiple HIP objects
scm.hip_profile.create({
    "name": "compliant-endpoints",
    "folder": "Prisma Access",
    "description": "Fully compliant endpoint posture",
    "match": "\"encrypted-disk\" and \"fully-patched\"",
})

# Update by name
scm.hip_profile.update_by_name("compliant-endpoints", folder="Prisma Access",
                                description="Updated compliance profile")

# Delete by name
scm.hip_profile.delete_by_name("compliant-endpoints", folder="Prisma Access")

# Bulk from YAML
scm.hip_profile.create_from_yaml("tests/data/hip_profiles.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
hip_profiles:
  - name: compliant-endpoints
    description: Fully compliant endpoint posture
    match: '"encrypted-disk" and "fully-patched"'

  - name: basic-managed
    description: Minimum managed device requirements
    match: '"managed-windows" or "managed-macos"'
```
