# Posture Settings

| | |
|---|---|
| **Accessor** | `scm.posture_settings` |
| **Class** | `PostureSettings` |

## Methods

| Method | Description |
|---|---|
| `get()` | Get current global posture settings |
| `update(payload)` | Update posture settings |

## Examples

```python
# Get current settings
settings = scm.posture_settings.get()
print(settings)

# Update settings
scm.posture_settings.update({
    "auto_remediation": True,
    "compliance_threshold": 80,
})
```
