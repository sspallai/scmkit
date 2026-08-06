# Security Profiles

Security profiles inspect and enforce policy on allowed traffic.
They are attached to security rules via a **Profile Group**.

## Available resources

| Accessor | YAML key | SCM endpoint |
|---|---|---|
| `scm.anti_spyware_profile` | `anti_spyware_profiles` | `/config/security/v1/anti-spyware-profiles` |
| `scm.vulnerability_profile` | `vulnerability_profiles` | `/config/security/v1/vulnerability-protection-profiles` |
| `scm.url_filtering_profile` | `url_filtering_profiles` | `/config/security/v1/url-filtering-profiles` |
| `scm.wildfire_profile` | `wildfire_profiles` | `/config/security/v1/wildfire-anti-virus-profiles` |
| `scm.dns_security_profile` | `dns_security_profiles` | `/config/security/v1/dns-security-profiles` |
| `scm.file_blocking_profile` | `file_blocking_profiles` | `/config/security/v1/file-blocking-profiles` |
| `scm.decryption_profile` | `decryption_profiles` | `/config/security/v1/decryption-profiles` |
| `scm.profile_group` | `profile_groups` | `/config/security/v1/profile-groups` |

---

## DNS Security Profile

Enforces DNS-layer controls including blocking domains from EDLs.

!!! note
    Domain-type EDLs **cannot** be used in security rule `category`.
    They must be referenced inside a DNS Security Profile's `botnet_domains.lists`,
    then applied via a Profile Group.

```yaml
dns_security_profiles:
  - name: my-dns-security
    folder: Prisma Access
    description: "Block domains from threat intelligence feeds"
    botnet_domains:
      lists:
        - name: my-domain-blocklist    # must be an existing domain-type EDL
          action:
            block: {}
          packet_capture: disable
        - name: my-domain-blocklist-2
          action:
            sinkhole: {}
          packet_capture: single-packet
```

---

## Anti-Spyware Profile

Detects and blocks spyware, C2 callbacks, and DNS tunnelling.

```yaml
anti_spyware_profiles:
  - name: my-atp-profile
    folder: Prisma Access
    description: "ATP enforcement"
    rules:
      - name: block-critical
        severity: [critical, high]
        category: any
        action:
          block_ip:
            track_by: attacker
            duration: 300
      - name: alert-medium
        severity: [medium]
        category: any
        action:
          alert: {}
```

---

## Vulnerability Profile

Protects against exploits and vulnerability-based attacks.

```yaml
vulnerability_profiles:
  - name: my-vuln-profile
    folder: Prisma Access
    rules:
      - name: block-critical
        severity: [critical, high]
        category: any
        action:
          block_ip:
            track_by: attacker
            duration: 300
```

---

## URL Filtering Profile

Controls web access by URL category.

```yaml
url_filtering_profiles:
  - name: my-url-profile
    folder: Prisma Access
    block:
      - malware
      - phishing
      - command-and-control
    alert:
      - proxy-avoidance-and-anonymizers
      - unknown
```

---

## WildFire Profile

Sends unknown files to WildFire for analysis.

```yaml
wildfire_profiles:
  - name: my-wildfire-profile
    folder: Prisma Access
    rules:
      - name: forward-all
        application: [any]
        file_type: [any]
        direction: both
        analysis: public-cloud
```

---

## Profile Group

A profile group bundles multiple security profiles into a single named object
referenced by security rules via `profile_setting.group`.

**Field aliases:**

| YAML alias | SCM field |
|---|---|
| `wildfire_analysis` | `virus_and_wildfire_analysis` |
| `dns_security_profile` | `dns_security` |

All fields accept a single string or a list.
The `data_filtering` field links a [Data Filtering Profile](../../data_loss_prevention/data_filtering_profile.md).

```yaml
profile_groups:
  - name: my-security-group
    folder: Prisma Access
    spyware:                     [best-practice]
    vulnerability:               [best-practice]
    url_filtering:               [best-practice]
    dns_security:                my-dns-security
    virus_and_wildfire_analysis: [best-practice]
    data_filtering:              my-dlp-filter   # optional, links a DataFilteringProfile
```

!!! warning
    Security rules accept **only** `profile_setting.group` — not individual profile
    references via `profile_setting.profiles`.
