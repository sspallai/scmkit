# HIP Object

| | |
|---|---|
| **Accessor** | `scm.hip_object` |
| **Class** | `HipObject` |
| **Endpoint** | `/config/objects/v1/hip-objects` |
| **YAML key** | `hip_objects` |

## Examples

```python
# List
objects = scm.hip_object.list(folder="Prisma Access")

# Get by name
obj = scm.hip_object.get("managed-windows", folder="Prisma Access")

# Create — disk encryption check
scm.hip_object.create({
    "name": "encrypted-disk",
    "folder": "Prisma Access",
    "description": "Requires disk encryption",
    "disk_encryption": {
        "criteria": {"is_installed": True, "encrypted_locations": []},
    },
})

# Create — patch management check
scm.hip_object.create({
    "name": "fully-patched",
    "folder": "Prisma Access",
    "patch_management": {
        "criteria": {"is_installed": True, "missing_patches": {"severity": {"greater_equal": 3}}},
    },
})

# Update by name
scm.hip_object.update_by_name("encrypted-disk", folder="Prisma Access",
                               description="Requires full disk encryption")

# Delete by name
scm.hip_object.delete_by_name("encrypted-disk", folder="Prisma Access")

# Bulk from YAML
scm.hip_object.create_from_yaml("tests/data/hip_objects.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
hip_objects:
  - name: encrypted-disk
    description: Requires disk encryption
    disk_encryption:
      criteria:
        is_installed: true
        encrypted_locations: []

  - name: fully-patched
    description: Requires all critical patches
    patch_management:
      criteria:
        is_installed: true
        missing_patches:
          severity:
            greater_equal: 3
```
