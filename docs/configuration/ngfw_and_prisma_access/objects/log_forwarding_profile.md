# Log Forwarding Profile

| | |
|---|---|
| **Accessor** | `scm.log_forwarding_profile` |
| **Class** | `LogForwardingProfile` |
| **Endpoint** | `/config/objects/v1/log-forwarding-profiles` |
| **YAML key** | `log_forwarding_profiles` |

!!! note
    Security rules reference log forwarding profiles via the `log_setting` field. The name must exactly match an existing profile.

## Examples

```python
# List
profiles = scm.log_forwarding_profile.list(folder="Prisma Access")

# Get by name
profile = scm.log_forwarding_profile.get("default-logging", folder="Prisma Access")

# Create
scm.log_forwarding_profile.create({
    "name": "default-logging",
    "folder": "Prisma Access",
    "description": "Default log forwarding to Cortex",
    "match_list": [
        {
            "name": "forward-traffic",
            "log_type": "traffic",
            "filter": "All Logs",
            "send_to_panorama": True,
        }
    ],
})

# Update by name
scm.log_forwarding_profile.update_by_name("default-logging", folder="Prisma Access",
                                            description="Updated log forwarding profile")

# Delete by name
scm.log_forwarding_profile.delete_by_name("default-logging", folder="Prisma Access")

# Bulk from YAML
scm.log_forwarding_profile.create_from_yaml("tests/data/log_forwarding_profiles.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
log_forwarding_profiles:
  - name: default-logging
    description: Default log forwarding to Cortex
    match_list:
      - name: forward-traffic
        log_type: traffic
        filter: All Logs
        send_to_panorama: true

      - name: forward-threats
        log_type: threat
        filter: All Logs
        send_to_panorama: true
```
