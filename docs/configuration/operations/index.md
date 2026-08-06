# Operations

## Commit

**Accessor:** `scm.push_config`

Pushes the candidate configuration to Prisma Access and optionally polls
until the job completes.

```python
result = scm.push_config.commit(
    folders=["Prisma Access"],       # list of folders to push
    description="My change",         # no '+' character allowed
    wait=True,                       # poll until FIN (default True)
)
```

### Polling behaviour

When `wait=True` (default), `commit()` polls the job every 5 seconds
and returns the final job response once status is `FIN`.

Raises `SCMCommitError` if `result_str != "OK"` or job state is `FAILED`/`CANCELED`.  
Raises `SCMTimeoutError` after 300 seconds.

### Reading the result

```python
result = scm.push_config.commit(folders=["Prisma Access"], description="test")

job = (result.get("data") or [{}])[0]
print(job.get("status_str"))    # "FIN"
print(job.get("result_str"))    # "OK"
print(job.get("id"))            # job ID integer
print(job.get("end_ts"))        # completion timestamp
print(job.get("uname"))         # user who triggered
```

### Commit description rules

- Maximum length: ~256 characters
- The `+` character is **not** allowed — use `"and"` instead.

---

## Push Status

**Accessor:** `scm.push_status`

Query job status without triggering a new commit.

```python
# Get a specific job by ID
job_response = scm.push_status.get("4255")
job = (job_response.get("data") or [{}])[0]
print(job.get("status_str"))

# List recent jobs
jobs = scm.push_status.list()
```

---

## Config Version Snapshots

**Accessor:** `scm.config_version_snapshots`

```python
scm.config_version_snapshots.list()
```

---

## Posture

| Accessor | Description |
|---|---|
| `scm.posture_settings` | Global posture settings |
| `scm.config_cleanup` | Identify and clean up unused objects |
| `scm.policy_optimizer` | Analyse rule usage and suggest optimisations |
| `scm.policy_analyzer` | Policy impact analysis |
