# Policies

## Available resources

| Accessor | YAML key | SCM endpoint |
|---|---|---|
| `scm.security_rule` | `security_rules` | `/config/security/v1/security-rules` |
| `scm.nat_rule` | `nat_rules` | `/config/security/v1/nat-rules` |
| `scm.application_override_rule` | `application_override_rules` | `/config/security/v1/application-override-rules` |
| `scm.decryption_rule` | `decryption_rules` | `/config/security/v1/decryption-rules` |

---

## Security Rule

### Fields

| Field | Type | Description |
|---|---|---|
| `name` | string | Rule name |
| `folder` | string | Folder (`Prisma Access`, etc.) |
| `rulebase` | `pre` \| `post` | Rule position |
| `from` | list | Source zones |
| `to` | list | Destination zones |
| `source` | list | Source addresses / address groups / EDLs (IP-type) |
| `destination` | list | Destination addresses / address groups / EDLs (IP-type) |
| `application` | list | Application objects |
| `service` | list | Service objects |
| `category` | list | URL categories / URL-type EDLs |
| `action` | `allow` \| `deny` \| `drop` | Rule action |
| `profile_setting.group` | list | Profile group names (for inspection) |
| `log_setting` | string | Log Forwarding Profile name |

!!! note
    `profile_setting.group` is the **only** supported profile attachment method.
    Individual profile references (`profile_setting.profiles.*`) are not accepted by the SCM REST API.

### YAML example

```yaml
security_rules:

  # Block bad IPs in destination
  - name: block-bad-ip-destination
    folder: Prisma Access
    rulebase: pre
    description: "Block outbound traffic to known bad IPs"
    from: [any]
    to: [any]
    source: [any]
    destination:
      - my-ip-blocklist-01
      - my-ip-blocklist-02
    application: [any]
    service: [any]
    action: deny

  # Block bad URLs
  - name: block-bad-urls
    folder: Prisma Access
    rulebase: pre
    description: "Block access to URLs in EDL URL lists"
    from: [any]
    to: [any]
    source: [any]
    destination: [any]
    application: [any]
    service: [any]
    category:
      - my-url-blocklist-01
    action: deny

  # Allow web traffic with security inspection
  - name: allow-web-with-inspection
    folder: Prisma Access
    rulebase: pre
    description: "Allow web traffic with full security inspection"
    from: [trust]
    to: [untrust]
    source: [any]
    destination: [any]
    application: [web-browsing, ssl]
    service: [application-default]
    action: allow
    profile_setting:
      group: [my-security-group]
    log_setting: my-log-forwarding-profile

  # Block domains via DNS Security (domain-type EDLs)
  - name: block-bad-domains
    folder: Prisma Access
    rulebase: pre
    description: "DNS security blocks domain-type EDLs"
    from: [any]
    to: [any]
    source: [any]
    destination: [any]
    application: [dns]
    service: [application-default]
    action: allow
    profile_setting:
      group: [my-dns-security-group]
```

---

## NAT Rule

```yaml
nat_rules:
  - name: outbound-nat
    folder: Prisma Access
    nat_type: ipv4
    from: [trust]
    to: [untrust]
    source: [any]
    destination: [any]
    service: any
    source_translation:
      dynamic_ip_and_port:
        interface_address:
          interface: ethernet1/1
```

---

## Decryption Rule

```yaml
decryption_rules:
  - name: decrypt-outbound-ssl
    folder: Prisma Access
    rulebase: pre
    from: [trust]
    to: [untrust]
    source: [any]
    destination: [any]
    service: [any]
    category: [any]
    action: decrypt
    profile: my-decryption-profile
    type:
      ssl_forward_proxy: {}
```
