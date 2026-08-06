# DataProfile

**Accessor:** `scm.dlp_data_profile`  
**YAML key:** `data_profiles`  
**DLP endpoints:**  
  `GET/DELETE /v1/api/data-profile/{id}`  
  `POST /v1/api/data-profile/create`  
  `PUT  /v1/api/data-profile/{id}`  
**Config required:** `dlp.base_url` in `scm_config.yaml`

---

## Overview

A data profile groups one or more detection rules into a named DLP policy.
Detection rules reference [DataPattern](data_pattern.md) objects by their integer `id`.

A data profile is ultimately referenced by a [DataFilteringProfile](data_filtering_profile.md)
on the SCM side.

---

## Detection rule types

### `expression_tree` — pattern-based

References one or more DataPattern IDs. Use when you want to detect specific
regex-matched content.

```yaml
detection_rules:
  - rule_type: expression_tree
    expression_tree:
      sub_expressions:
        - rule_item:
            name: ccn-pattern   # human label (for readability)
            id: 12345           # integer ID from DataPattern
```

### `multi_profile` — child profile links

Links existing DLP profile IDs together. Use for hierarchical / composite profiles.

```yaml
detection_rules:
  - rule_type: multi_profile
    multi_profile:
      data_profile_ids: [101, 102]
```

---

## Methods

| Method | Description |
|---|---|
| `.list()` | List all data profiles |
| `.get(name)` | Get by name (returns `None` if not found) |
| `.get_by_id(id)` | Get by integer ID |
| `.get_id(name)` | Return integer ID for a named profile |
| `.create(payload)` | Create a profile |
| `.update(id, payload)` | Update by integer ID |
| `.delete(id)` | Delete by integer ID |
| `.apply(payload, on_conflict)` | Create or handle conflict |
| `.create_from_yaml(yaml_path)` | Load YAML and apply |
| `.delete_from_yaml(yaml_path)` | Load YAML and delete |

---

## Python

```python
scm = SCMSession.from_config("scm_config.yaml")   # dlp.base_url required

# Get pattern ID first
pattern_id = scm.dlp_data_pattern.get("ccn-pattern")["id"]

# Create profile
scm.dlp_data_profile.create({
    "name": "pii-profile",
    "type": "custom",
    "status": "active",
    "is_granular_profile": False,
    "detection_rules": [
        {
            "rule_type": "expression_tree",
            "expression_tree": {
                "sub_expressions": [
                    {"rule_item": {"name": "ccn-pattern", "id": pattern_id}}
                ]
            }
        }
    ]
})

# Get integer ID
profile_id = scm.dlp_data_profile.get_id("pii-profile")

# Delete
scm.dlp_data_profile.delete(profile_id)
```

---

## YAML

### Standard profile (expression_tree)

```yaml
data_profiles:
  - name: pii-profile
    type: custom
    status: active
    is_granular_profile: false
    detection_rules:
      - rule_type: expression_tree
        expression_tree:
          sub_expressions:
            - rule_item:
                name: ccn-pattern
                id: 12345          # integer ID from DataPattern.get("ccn-pattern")["id"]
            - rule_item:
                name: ssn-pattern
                id: 12346
```

### Granular / composite profile (multi_profile)

```yaml
data_profiles:
  - name: pii-combined
    type: custom
    status: active
    is_granular_profile: true
    detection_rules:
      - rule_type: multi_profile
        multi_profile:
          data_profile_ids: [101, 102]  # integer IDs of child DataProfiles
```

```python
scm.dlp_data_profile.create_from_yaml("dlp.yaml")
```

---

## Payload fields

| Field | Required | Description |
|---|---|---|
| `name` | Yes | Profile name |
| `type` | Yes | `custom` |
| `status` | Yes | `active` \| `inactive` |
| `is_granular_profile` | Yes | `false` for expression_tree, `true` for multi_profile |
| `detection_rules` | Yes | List of detection rule objects (see above) |
| `description` | No | Human-readable description |

---

## Notes

- Profile IDs are **integers** assigned by the DLP service (not UUIDs).
- Pattern IDs referenced in `expression_tree.sub_expressions[].rule_item.id`
  must exist as active [DataPattern](data_pattern.md) objects.
- The create endpoint is `/v1/api/data-profile/create` (not `/v1/api/data-profile`);
  the body is wrapped as `{"dataProfile": {...}}` — scmkit handles this automatically.
