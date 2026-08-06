# Policy Analyzer

| | |
|---|---|
| **Accessor** | `scm.policy_analyzer` |
| **Class** | `PolicyAnalyzer` |

## Methods

| Method | Description |
|---|---|
| `analyze(folder)` | Analyze policy coverage, shadowed rules, and unused rules |

## Examples

```python
# Analyze policy coverage
analysis = scm.policy_analyzer.analyze(folder="Prisma Access")
print(analysis["shadowed_rules"])
print(analysis["unused_rules"])
print(analysis["coverage_score"])
```
