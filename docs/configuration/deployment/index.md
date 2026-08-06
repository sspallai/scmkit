# Deployment

## Available resources

| Accessor | YAML key | SCM endpoint |
|---|---|---|
| `scm.remote_networks` | `remote_networks` | `/config/deployment/v1/remote-networks` |
| `scm.service_connections` | `service_connections` | `/config/deployment/v1/service-connections` |

## Remote Networks

```yaml
remote_networks:
  - name: branch-office-1
    folder: Prisma Access
    region: us-east-1
    spn_name: us-east-spn
    ipsec_tunnel: branch-office-1-tunnel
```

## Service Connections

```yaml
service_connections:
  - name: data-center-1
    folder: Prisma Access
    region: us-west-1
    source_nat: true
```
