# DataPattern

**Accessor:** `scm.dlp_data_pattern`  
**YAML key:** `data_patterns`  
**DLP endpoint:** `/v1/api/data-pattern`  
**Config required:** `dlp.base_url` in `scm_config.yaml`

---

## Overview

Data patterns are the lowest-level building blocks of DLP.
Each pattern defines how content is detected — either via regular expressions
or file property metadata (e.g. Titus labels).

Patterns are referenced inside [DataProfile](data_profile.md) detection rules by their integer `id`.

---

## Detection techniques

| `detection_technique` | Description |
|---|---|
| `regex` | Match content against regular expressions with optional proximity keywords |
| `fileproperty` | Match file metadata / Titus classification labels |

---

## Methods

| Method | Description |
|---|---|
| `.list()` | List all custom patterns |
| `.get(name)` | Get by name (returns `None` if not found) |
| `.get_by_id(id)` | Get by integer ID |
| `.create(payload)` | Create a pattern |
| `.update(id, payload)` | Update by integer ID |
| `.delete(id)` | Delete by integer ID |
| `.apply(payload, on_conflict)` | Create or handle conflict |
| `.create_from_yaml(yaml_path)` | Load YAML and apply |
| `.delete_from_yaml(yaml_path)` | Load YAML and delete |

---

## Python

```python
scm = SCMSession.from_config("scm_config.yaml")  # dlp.base_url required

# Create regex pattern
scm.dlp_data_pattern.create({
    "name": "ccn-pattern",
    "type": "custom",
    "status": "active",
    "detection_technique": "regex",
    "description": "Credit card number detection",
    "delimiter": ";",
    "regexes": ["\\b(?:\\d[ -]?){13,16}\\d\\b"],
    "proximity_keywords": ["card", "visa", "mastercard"],
    "metadataCriteria": {},
})

# List patterns
patterns = scm.dlp_data_pattern.list()

# Get integer ID (needed for DataProfile detection rules)
p = scm.dlp_data_pattern.get("ccn-pattern")
print(p["id"])   # e.g. 12345

# Delete
scm.dlp_data_pattern.delete(p["id"])
```

---

## YAML

### Regex pattern

```yaml
data_patterns:
  - name: ccn-pattern
    type: custom
    status: active
    detection_technique: regex
    description: "Credit card number"
    delimiter: ";"
    regexes:
      - "\\b(?:\\d[ -]?){13,16}\\d\\b"
    proximity_keywords:
      - card
      - visa
      - mastercard
    metadataCriteria: {}
```

### File property / Titus pattern

```yaml
data_patterns:
  - name: titus-confidential
    type: custom
    status: active
    detection_technique: fileproperty
    description: "Titus-labelled confidential files"
    metadataCriteria:
      label: Confidential
    regexes: []
    proximity_keywords: []
```

```python
scm.dlp_data_pattern.create_from_yaml("dlp.yaml")
```

---

## Payload fields

| Field | Required | Description |
|---|---|---|
| `name` | Yes | Pattern name |
| `type` | Yes | `custom` |
| `status` | Yes | `active` \| `inactive` |
| `detection_technique` | Yes | `regex` \| `fileproperty` |
| `description` | No | Human-readable description |
| `delimiter` | No | Delimiter for multiple regex values, default `;` |
| `regexes` | Yes | List of regex strings (empty list for fileproperty) |
| `proximity_keywords` | No | Keywords that must appear near a regex match |
| `metadataCriteria` | No | File property criteria (for fileproperty technique) |

---

## Notes

- Pattern IDs are **integers** assigned by the DLP service (not UUIDs).
- Use `.get(name)["id"]` to retrieve the integer ID before referencing
  it in a [DataProfile](data_profile.md) detection rule.
- The DLP service list endpoint returns `response["resources"]` (not `response["data"]`
  as used by SCM REST endpoints).
