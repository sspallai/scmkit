# RADIUS Server Profile

| | |
|---|---|
| **Accessor** | `scm.radius_server_profile` |
| **Class** | `RadiusServerProfile` |
| **Endpoint** | `/config/identity/v1/radius-server-profiles` |
| **YAML key** | `radius_server_profiles` |

## Examples

```python
# List
profiles = scm.radius_server_profile.list(folder="Prisma Access")

# Get by name
profile = scm.radius_server_profile.get("corp-radius", folder="Prisma Access")

# Create
scm.radius_server_profile.create({
    "name": "corp-radius",
    "folder": "Prisma Access",
    "server": [{"name": "radius1", "server": "radius.corp.example.com", "port": 1812}],
    "secret": "shared-secret",
    "timeout": 10,
    "retries": 3,
})

# Update by name
scm.radius_server_profile.update_by_name("corp-radius", folder="Prisma Access",
                                          timeout=15)

# Delete by name
scm.radius_server_profile.delete_by_name("corp-radius", folder="Prisma Access")

# Bulk from YAML
scm.radius_server_profile.create_from_yaml("tests/data/radius_server_profiles.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
radius_server_profiles:
  - name: corp-radius
    server:
      - name: radius1
        server: radius.corp.example.com
        port: 1812
    secret: shared-secret
    timeout: 10
    retries: 3
```
