# Policy Optimizer

| | |
|---|---|
| **Accessor** | `scm.policy_optimizer` |
| **Class** | `PolicyOptimizer` |

## Methods

| Method | Description |
|---|---|
| `list(folder)` | List rules flagged by the optimizer with recommendations |

## Examples

```python
# List optimization recommendations
optimizations = scm.policy_optimizer.list(folder="Prisma Access")
for opt in optimizations:
    print(opt["rule_name"], opt["recommendation"], opt["reason"])
```
