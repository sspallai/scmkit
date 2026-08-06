# External Dynamic List (EDL)

| | |
|---|---|
| **Accessor** | `scm.edl` |
| **Class** | `Edl` |
| **Endpoint** | `/config/objects/v1/external-dynamic-lists` |
| **YAML key** | `edls` |

!!! note
    HTTPS EDLs automatically inject `certificate_profile: "EDL-Hosting-Service-Profile"` if not set.

## Examples

```python
# List
edls = scm.edl.list(folder="Prisma Access")

# Get by name
edl = scm.edl.get("bad-ips", folder="Prisma Access")

# Create — IP type
scm.edl.create({
    "name": "bad-ips",
    "folder": "Prisma Access",
    "type": {
        "ip": {
            "url": "https://feeds.example.com/bad-ips.txt",
            "recurring": {"hourly": {}},
        }
    },
})

# Create — URL type
scm.edl.create({
    "name": "bad-urls",
    "folder": "Prisma Access",
    "type": {
        "url": {
            "url": "https://feeds.example.com/bad-urls.txt",
            "recurring": {"daily": {"at": "03"}},
        }
    },
})

# Create — Domain type (used with DNS Security profiles)
scm.edl.create({
    "name": "bad-domains",
    "folder": "Prisma Access",
    "type": {
        "domain": {
            "url": "https://feeds.example.com/bad-domains.txt",
            "recurring": {"weekly": {"day_of_week": "monday", "at": "02"}},
        }
    },
})

# Update by name
scm.edl.update_by_name("bad-ips", folder="Prisma Access",
                        type={"ip": {"url": "https://feeds.example.com/bad-ips-v2.txt",
                                     "recurring": {"hourly": {}}}})

# Delete by name
scm.edl.delete_by_name("bad-ips", folder="Prisma Access")

# Bulk from YAML
scm.edl.create_from_yaml("tests/data/edls.yaml")
```

## YAML Format

```yaml
folder: Prisma Access
edls:
  - name: bad-ips
    type:
      ip:
        url: https://feeds.example.com/bad-ips.txt
        recurring:
          hourly: {}

  - name: bad-urls
    type:
      url:
        url: https://feeds.example.com/bad-urls.txt
        recurring:
          daily:
            at: "03"

  - name: bad-domains
    type:
      domain:
        url: https://feeds.example.com/bad-domains.txt
        recurring:
          weekly:
            day_of_week: monday
            at: "02"
```

## EDL Types

| Type | Used in | Description |
|---|---|---|
| `ip` | Security rule `source`/`destination` | IP addresses and CIDRs |
| `url` | URL Filtering profile | URLs and URL patterns |
| `domain` | DNS Security profile `botnet_domains.lists` | Domain names (DNS sinkholing) |

## Recurring Schedules

| Key | Fields | Description |
|---|---|---|
| `five_minute` | `{}` | Every 5 minutes |
| `hourly` | `{}` | Every hour |
| `daily` | `at` (HH) | Daily at specified hour |
| `weekly` | `day_of_week`, `at` | Weekly on given day and hour |
| `monthly` | `day_of_month`, `at` | Monthly on given day |
