# DataFilteringProfile

**Accessor:** `scm.data_filtering_profile`  
**YAML key:** `data_filtering_profiles`  
**SCM endpoint:** `/config/security/v1/data-filtering-profiles`  
**Config required:** None (uses `scm.base_url`)

---

## Overview

`DataFilteringProfile` is the **SCM-side container** that links an Enterprise DLP
data profile to a security profile group. The object itself holds only `name` and
`folder` — the DLP inspection content (patterns, thresholds, detection rules) is
managed separately via [DataPattern](data_pattern.md) and [DataProfile](data_profile.md)
on the Enterprise DLP service.

Once created, reference it from a profile group via the `data_filtering` field.

---

## Methods

Inherits the full [SCMResource interface](../../index.md#core-crud-interface).

---

## Python

```python
from scmkit import SCMSession

scm = SCMSession.from_config("scm_config.yaml")

# Create
scm.data_filtering_profile.create(
    name="pii-filter",
    folder="Prisma Access",
)

# List
profiles = scm.data_filtering_profile.list(folder="Prisma Access")

# Get by name
p = scm.data_filtering_profile.get("pii-filter", "Prisma Access")
print(p["id"])

# Delete by name
scm.data_filtering_profile.delete_by_name("pii-filter", "Prisma Access")

# Idempotent (skip if exists)
scm.data_filtering_profile.apply(
    {"name": "pii-filter", "folder": "Prisma Access"},
    on_conflict="skip",
)
```

---

## YAML

```yaml
data_filtering_profiles:
  - name: pii-filter
    folder: Prisma Access
  - name: financial-data-filter
    folder: Prisma Access
```

```python
scm.data_filtering_profile.create_from_yaml("dlp.yaml")
scm.data_filtering_profile.delete_from_yaml("dlp.yaml")
```

---

## Attach to Profile Group

```yaml
profile_groups:
  - name: my-dlp-group
    folder: Prisma Access
    spyware:      [best-practice]
    vulnerability: [best-practice]
    data_filtering: pii-filter      # reference by name
```

`data_filtering` accepts a string or a list — scmkit coerces it to a list automatically.

---

## Response schema

```json
{
  "id":     "11ce01ae-00ad-41d2-a5f3-17b76f3839c6",
  "name":   "pii-filter",
  "folder": "Prisma Access"
}
```
