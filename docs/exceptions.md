# Exceptions

All scmkit exceptions are importable from `scmkit.exceptions`.

```python
from scmkit.exceptions import SCMAPIError, SCMNotFoundError, SCMAuthError
```

## Reference

| Exception | When raised |
|---|---|
| `SCMAuthError` | OAuth token fetch fails (bad credentials, network error) |
| `SCMAPIError` | API returns any 4xx or 5xx response |
| `SCMNotFoundError` | API returns 404 (subclass of `SCMAPIError`) |
| `SCMConfigError` | Config file is missing, unreadable, or missing required fields |
| `SCMCommitError` | Commit job completes with `result_str != "OK"`, or state is `FAILED`/`CANCELED` |
| `SCMTimeoutError` | Commit poll exceeds the 300 s timeout |

## Usage

```python
from scmkit import SCMSession
from scmkit.exceptions import SCMAPIError, SCMNotFoundError, SCMCommitError

scm = SCMSession.from_config("scm_config.yaml")

# Catch not-found separately
try:
    item = scm.address.get("nonexistent", "Prisma Access")
except SCMNotFoundError:
    print("Address not found")

# Catch any API error
try:
    scm.edl.create(name="__bad__name__", folder="Prisma Access", ...)
except SCMAPIError as e:
    print(e.status_code, e)   # e.g. 400 {"_errors": [...]}

# Catch commit failure
try:
    scm.push_config.commit(folders=["Prisma Access"], description="test")
except SCMCommitError as e:
    print("Commit failed:", e)
except SCMTimeoutError:
    print("Commit timed out after 300s")
```

## `SCMAPIError` attributes

| Attribute | Type | Description |
|---|---|---|
| `status_code` | `int` | HTTP status code |
| `message` | `str` | Raw API response body |

```python
try:
    scm.edl.create(name="bad", folder="Prisma Access")
except SCMAPIError as e:
    print(e.status_code)   # 400
    print(str(e))          # {"_errors": [{"code": "API_I00013", ...}]}
```
