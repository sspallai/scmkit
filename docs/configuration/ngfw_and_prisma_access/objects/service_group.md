# Service Group

| | |
|---|---|
| **Accessor** | `scm.service_group` |
| **Class** | `ServiceGroup` |
| **Endpoint** | `/config/objects/v1/service-groups` |
| **YAML key** | `service_groups` |

## Examples

```python
# List
groups = scm.service_group.list(folder="Prisma Access")

# Get by name
grp = scm.service_group.get("web-services", folder="Prisma Access")

# Create
scm.service_group.create({
    "name": "web-services",
    "folder": "Prisma Access",
    "members": ["application-default", "svc-http-8080", "svc-https-8443"],
})

# Update by name
scm.service_group.update_by_name("web-services", folder="Prisma Access",
                                  members=["application-default", "svc-http-8080"])

# Delete by name
scm.service_group.delete_by_name("web-services", folder="Prisma Access")

# Bulk from YAML
scm.service_group.create_from_yaml("tests/data/service_groups.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
service_groups:
  - name: web-services
    members:
      - application-default
      - svc-http-8080
      - svc-https-8443

  - name: custom-ports
    members:
      - svc-custom-udp
      - svc-tcp-range
```
