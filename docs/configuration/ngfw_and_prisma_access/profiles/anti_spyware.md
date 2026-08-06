# Anti-Spyware Profile

| | |
|---|---|
| **Accessor** | `scm.anti_spyware_profile` |
| **Class** | `AntiSpywareProfile` |
| **Endpoint** | `/config/security/v1/anti-spyware-profiles` |
| **YAML key** | `anti_spyware_profiles` |

!!! note
    A bare `rules` list is automatically wrapped as `{"operations": [...]}` before sending to the API.

## Examples

```python
# List
profiles = scm.anti_spyware_profile.list(folder="Prisma Access")

# Get by name
profile = scm.anti_spyware_profile.get("strict-atp", folder="Prisma Access")

# Create
scm.anti_spyware_profile.create({
    "name": "strict-atp",
    "folder": "Prisma Access",
    "description": "Strict ATP blocking profile",
    "rules": [
        {
            "name": "block-critical",
            "severity": ["critical", "high"],
            "category": "any",
            "action": {"block_ip": {"track_by": "attacker", "duration": 300}},
            "threat_name": "any",
            "packet_capture": "single-packet",
        }
    ],
})

# Update by name
scm.anti_spyware_profile.update_by_name("strict-atp", folder="Prisma Access",
                                         description="Updated strict ATP profile")

# Delete by name
scm.anti_spyware_profile.delete_by_name("strict-atp", folder="Prisma Access")

# Bulk from YAML
scm.anti_spyware_profile.create_from_yaml("tests/data/anti_spyware_profiles.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
anti_spyware_profiles:
  - name: strict-atp
    description: Strict ATP blocking profile
    rules:
      - name: block-critical
        severity:
          - critical
          - high
        category: any
        threat_name: any
        action:
          block_ip:
            track_by: attacker
            duration: 300
        packet_capture: single-packet

      - name: alert-medium
        severity:
          - medium
        category: any
        threat_name: any
        action:
          alert: {}
        packet_capture: disable
```
