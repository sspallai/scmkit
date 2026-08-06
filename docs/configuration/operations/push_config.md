# Push Config (Commit)

| | |
|---|---|
| **Accessor** | `scm.push_config` |
| **Class** | `PushConfig` |

## Methods

| Method | Description |
|---|---|
| `commit(folders, description, wait)` | Commit candidate config and optionally poll to completion |

## Examples

```python
# Commit and wait for completion (default)
result = scm.push_config.commit(
    folders=["Prisma Access"],
    description="CDSS ATP test setup",
)
print(result["job_id"], result["result_str"])  # → OK

# Commit without waiting — get job_id immediately
result = scm.push_config.commit(
    folders=["Prisma Access"],
    description="async commit",
    wait=False,
)
job_id = result["job_id"]

# Poll manually after async commit
status = scm.push_status.get(job_id)
print(status["status"], status["result_str"])

# Commit multiple folders
scm.push_config.commit(
    folders=["Prisma Access", "Remote Networks"],
    description="Multi-folder push",
)
```

## Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `folders` | `list[str]` | `["Prisma Access"]` | Folders to include in the commit |
| `description` | `str` | `"scm_auto commit"` | Commit description |
| `wait` | `bool` | `True` | Poll until commit completes; raises `SCMCommitError` on failure, `SCMTimeoutError` after 300s |

## Error Handling

```python
from scmkit.exceptions import SCMCommitError, SCMTimeoutError

try:
    scm.push_config.commit(folders=["Prisma Access"], description="test")
except SCMCommitError as e:
    print("Commit failed:", e)
except SCMTimeoutError:
    print("Commit timed out after 300s")
```
