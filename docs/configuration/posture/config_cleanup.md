# Config Cleanup

| | |
|---|---|
| **Accessor** | `scm.config_cleanup` |
| **Class** | `ConfigCleanup` |

## Methods

| Method | Description |
|---|---|
| `list(folder)` | List unused/stale objects identified for cleanup |
| `run(folder)` | Trigger a cleanup analysis run |

## Examples

```python
# List cleanup candidates
candidates = scm.config_cleanup.list(folder="Prisma Access")
for item in candidates:
    print(item["type"], item["name"], item["reason"])

# Trigger a new analysis
scm.config_cleanup.run(folder="Prisma Access")
```
