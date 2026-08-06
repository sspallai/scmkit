# Cloud Identity Engine

| Accessor | Description |
|---|---|
| `scm.user_context` | Query user-to-IP mapping and group membership context |

```python
context = scm.user_context.get(ip="10.1.1.5")
```
