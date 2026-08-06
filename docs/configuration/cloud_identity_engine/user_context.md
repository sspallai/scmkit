# User Context

| | |
|---|---|
| **Accessor** | `scm.user_context` |
| **Class** | `UserContext` |

## Methods

| Method | Description |
|---|---|
| `list(folder)` | List all user context entries |
| `get(name, folder)` | Get user-to-IP mapping and group membership by username or IP |

## Examples

```python
# Get context for a specific IP
context = scm.user_context.get(ip="10.1.1.5")
print(context["username"])
print(context["groups"])

# List all context entries
all_contexts = scm.user_context.list(folder="Prisma Access")
```
