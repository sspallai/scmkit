# Application

| | |
|---|---|
| **Accessor** | `scm.application` |
| **Class** | `Application` |
| **Endpoint** | `/config/objects/v1/applications` |
| **YAML key** | `applications` |

## Examples

```python
# List custom applications
apps = scm.application.list(folder="Prisma Access")

# Get by name
app = scm.application.get("my-custom-app", folder="Prisma Access")

# Create a custom application
scm.application.create({
    "name": "my-custom-app",
    "folder": "Prisma Access",
    "category": "business-systems",
    "subcategory": "management",
    "technology": "client-server",
    "risk": 1,
    "description": "Custom internal application",
    "ports": ["tcp/8443"],
})

# Update by name
scm.application.update_by_name("my-custom-app", folder="Prisma Access",
                                description="Updated description")

# Delete by name
scm.application.delete_by_name("my-custom-app", folder="Prisma Access")

# Bulk from YAML
scm.application.create_from_yaml("tests/data/applications.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
applications:
  - name: my-custom-app
    category: business-systems
    subcategory: management
    technology: client-server
    risk: 1
    description: Custom internal application
    ports:
      - tcp/8443

  - name: internal-monitoring
    category: networking
    subcategory: monitoring
    technology: client-server
    risk: 2
    ports:
      - tcp/9090
      - udp/9090
```
