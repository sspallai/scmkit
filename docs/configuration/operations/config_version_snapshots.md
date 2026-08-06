# Config Version Snapshots

| | |
|---|---|
| **Accessor** | `scm.config_version_snapshots` |
| **Class** | `ConfigVersionSnapshots` |

## Methods

| Method | Description |
|---|---|
| `list()` | List all saved configuration versions |
| `get(version)` | Get details of a specific version |
| `load_config(version)` | Restore a specific version as candidate config |
| `restore(version)` | Alias for `load_config` |

## Examples

```python
# List all versions
versions = scm.config_version_snapshots.list()
for v in versions:
    print(v["version"], v["created_at"], v["description"])

# Get details of a specific version
version = scm.config_version_snapshots.get("42")

# Restore a version as candidate config
scm.config_version_snapshots.load_config("42")
# Then commit to apply it
scm.push_config.commit(folders=["Prisma Access"], description="Restore v42")
```
