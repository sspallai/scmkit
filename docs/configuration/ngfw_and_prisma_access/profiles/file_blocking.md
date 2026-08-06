# File Blocking Profile

| | |
|---|---|
| **Accessor** | `scm.file_blocking_profile` |
| **Class** | `FileBlockingProfile` |
| **Endpoint** | `/config/security/v1/file-blocking-profiles` |
| **YAML key** | `file_blocking_profiles` |

## Examples

```python
# List
profiles = scm.file_blocking_profile.list(folder="Prisma Access")

# Get by name
profile = scm.file_blocking_profile.get("block-executables", folder="Prisma Access")

# Create
scm.file_blocking_profile.create({
    "name": "block-executables",
    "folder": "Prisma Access",
    "description": "Block executable uploads and downloads",
    "rules": [
        {
            "name": "block-exe",
            "application": ["any"],
            "file_type": ["pe", "dll", "bat", "com"],
            "direction": "both",
            "action": "block",
        }
    ],
})

# Update by name
scm.file_blocking_profile.update_by_name("block-executables", folder="Prisma Access",
                                          description="Updated file blocking profile")

# Delete by name
scm.file_blocking_profile.delete_by_name("block-executables", folder="Prisma Access")

# Bulk from YAML
scm.file_blocking_profile.create_from_yaml("tests/data/file_blocking_profiles.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
file_blocking_profiles:
  - name: block-executables
    description: Block executable uploads and downloads
    rules:
      - name: block-exe
        application:
          - any
        file_type:
          - pe
          - dll
          - bat
          - com
        direction: both
        action: block

      - name: alert-scripts
        application:
          - any
        file_type:
          - ps
          - vbs
        direction: both
        action: alert
```
