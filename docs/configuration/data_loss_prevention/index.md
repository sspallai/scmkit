# Data Loss Prevention (DLP)

DLP in SCM involves two separate services.

| Layer | Service | Config required |
|---|---|---|
| SCM REST | `DataFilteringProfile` | None (uses `scm.base_url`) |
| Enterprise DLP | `DataPattern`, `DataProfile` | `dlp.base_url` in config |

---

## Architecture overview

```
Security Rule
  └── profile_setting.group  →  Profile Group
                                    └── data_filtering  →  DataFilteringProfile  (SCM REST)
                                                               └── (references)   →  DataProfile  (DLP service)
                                                                                      └── detection_rules
                                                                                              └── DataPattern  (DLP service)
```

---

## End-to-end workflow

```python
from scmkit import SCMSession

scm = SCMSession.from_config("scm_config.yaml")  # must include dlp.base_url

# 1. Create data patterns (custom regex)
scm.dlp_data_pattern.create_from_yaml("dlp.yaml")

# 2. Create data profile (groups patterns into detection rules)
scm.dlp_data_profile.create_from_yaml("dlp.yaml")

# 3. Create SCM-side data filtering profile (container)
scm.data_filtering_profile.create_from_yaml("dlp.yaml")

# 4. Create profile group referencing the data filtering profile
scm.profile_group.create_from_yaml("dlp.yaml")

# 5. Create security rule using the profile group
scm.security_rule.create_from_yaml("rules.yaml")

# 6. Commit
scm.push_config.commit(folders=["Prisma Access"], description="DLP policy push")
```

---

## Resources

- [DataFilteringProfile](data_filtering_profile.md) — SCM-side container (no extra config)
- [DataPattern](data_pattern.md) — Custom regex / file-property patterns (requires `dlp.base_url`)
- [DataProfile](data_profile.md) — Detection rules grouping patterns (requires `dlp.base_url`)

---

## DLP config section

Add the `dlp:` block to `scm_config.yaml` to enable DLP pattern and profile management:

```yaml
scm:
  client_id: ...
  base_url:  https://qa.api.sase.paloaltonetworks.com

dlp:
  base_url: "https://<your-dlp-service-host>/"
```

The DLP service uses the same OAuth credentials as SCM.
If `dlp.base_url` is not configured, accessing `scm.dlp_data_pattern` or
`scm.dlp_data_profile` raises `ValueError` with a clear message.
