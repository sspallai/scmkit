# Objects

Objects are reusable building blocks referenced by security rules, profiles, and policies.

## Available resources

| Accessor | YAML key | SCM endpoint |
|---|---|---|
| `scm.address` | `addresses` | `/config/objects/v1/addresses` |
| `scm.address_group` | `address_groups` | `/config/objects/v1/address-groups` |
| `scm.service` | `services` | `/config/objects/v1/services` |
| `scm.service_group` | `service_groups` | `/config/objects/v1/service-groups` |
| `scm.edl` | `edls` | `/config/objects/v1/external-dynamic-lists` |
| `scm.tag` | `tags` | `/config/objects/v1/tags` |
| `scm.application` | `applications` | `/config/objects/v1/applications` |
| `scm.application_group` | `application_groups` | `/config/objects/v1/application-groups` |
| `scm.application_filter` | `application_filters` | `/config/objects/v1/application-filters` |
| `scm.dynamic_user_group` | `dynamic_user_groups` | `/config/objects/v1/dynamic-user-groups` |
| `scm.url_category` | `url_categories` | `/config/objects/v1/url-categories` |
| `scm.log_forwarding_profile` | `log_forwarding_profiles` | `/config/objects/v1/log-forwarding-profiles` |
| `scm.hip_object` | `hip_objects` | `/config/objects/v1/hip-objects` |
| `scm.hip_profile` | `hip_profiles` | `/config/objects/v1/hip-profiles` |

---

## Address

```python
scm.address.create(
    name="web-server",
    folder="Prisma Access",
    ip_netmask="10.1.1.10/32",
    description="Production web server",
)
```

```yaml
addresses:
  - name: web-server
    folder: Prisma Access
    ip_netmask: "10.1.1.10/32"
  - name: office-subnet
    folder: Prisma Access
    ip_netmask: "192.168.1.0/24"
  - name: example-fqdn
    folder: Prisma Access
    fqdn: "example.com"
```

---

## Address Group

```yaml
address_groups:
  - name: trusted-servers
    folder: Prisma Access
    static:
      - web-server
      - office-subnet
```

---

## Service

```yaml
services:
  - name: custom-https-8443
    folder: Prisma Access
    protocol:
      tcp:
        port: "8443"
  - name: custom-udp-5000
    folder: Prisma Access
    protocol:
      udp:
        port: "5000"
```

---

## Service Group

```yaml
service_groups:
  - name: web-services
    folder: Prisma Access
    members:
      - service-http
      - service-https
      - custom-https-8443
```

---

## External Dynamic List (EDL)

EDLs pull blocklists from external URLs and refresh automatically.

**EDL types and rule usage:**

| EDL type | In security rule |
|---|---|
| `ip` | `source` / `destination` (acts as address object) |
| `url` | `category` (acts as custom URL category) |
| `domain` | DNS Security Profile `botnet_domains.lists` only |

```yaml
edls:
  - name: my-ip-blocklist
    folder: Prisma Access
    type:
      ip:
        url: "https://example.com/ips.txt"
        recurring:
          five_minute: {}

  - name: my-url-blocklist
    folder: Prisma Access
    type:
      url:
        url: "https://example.com/urls.txt"
        recurring:
          hourly: {}

  - name: my-domain-blocklist
    folder: Prisma Access
    type:
      domain:
        url: "https://example.com/domains.txt"
        recurring:
          hourly: {}
```

Recurring options: `five_minute`, `hourly`, `daily`, `weekly`, `monthly`.

---

## Tag

```yaml
tags:
  - name: critical
    folder: Prisma Access
    color: Red
  - name: internal
    folder: Prisma Access
    color: Blue
```

---

## Application

```yaml
applications:
  - name: my-custom-app
    folder: Prisma Access
    category: business-systems
    subcategory: management
    technology: client-server
    risk: 3
    ports:
      - "tcp/8080,8443"
```

---

## URL Category

```yaml
url_categories:
  - name: internal-domains
    folder: Prisma Access
    type: URL List
    list:
      - "internal.example.com"
      - "portal.example.com"
```
