# Push Status

| | |
|---|---|
| **Accessor** | `scm.push_status` |
| **Class** | `PushStatus` |

## Methods

| Method | Description |
|---|---|
| `get(job_id)` | Get status of a specific commit job |
| `list()` | List recent commit jobs |

## Examples

```python
# Get status of a specific job
status = scm.push_status.get("job-abc123")
print(status["status"])      # running / FIN
print(status["result_str"])  # OK / FAIL

# List recent jobs
jobs = scm.push_status.list()
for job in jobs:
    print(job["job_id"], job["status"], job["result_str"])
```

## Response Fields

| Field | Description |
|---|---|
| `job_id` | Unique commit job identifier |
| `status` | `running`, `FIN`, `PEND` |
| `result_str` | `OK`, `FAIL`, or empty while running |
| `description` | Commit description |
| `start_ts` | Start timestamp |
| `end_ts` | End timestamp (when complete) |
