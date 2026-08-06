# Posture

| Accessor | Description |
|---|---|
| `scm.posture_settings` | Global posture and compliance settings |
| `scm.config_cleanup` | Identify unused / stale objects for cleanup |
| `scm.policy_optimizer` | Analyse rule usage and suggest policy optimisations |
| `scm.policy_analyzer` | Evaluate the impact and coverage of policy rules |

```python
# List rules flagged by optimizer
optimizations = scm.policy_optimizer.list()

# List cleanup candidates
candidates = scm.config_cleanup.list()
```
