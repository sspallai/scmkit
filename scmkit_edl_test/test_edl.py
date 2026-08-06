import json
from scmkit import SCMSession

scm = SCMSession.from_config("scm_config.yaml")

# 1. EDL objects (IP, URL, domain lists)
scm.edl.create_from_yaml('edl_config.yaml')

# 2. DNS Security Profile (domain EDLs in botnet_domains.lists)
scm.dns_security_profile.create_from_yaml('dns_security_config.yaml')

# 3. Profile Group (dns_security: cpt-dns-security-domain-block)
scm.profile_group.create_from_yaml('dns_security_config.yaml')

# 4. Security rules (IP block, URL block, domain block via profile group)
scm.security_rule.create_from_yaml('security_rules_config.yaml')

# 5. Commit and wait for job to complete
result = scm.push_config.commit(
    folders=["Prisma Access"],
    description="CPT EDL objects and security rules",
)
# 6. Print final job status (result is the polled response from push_config.commit)
job_data = result.get("data", [{}])
job_data = job_data[0] if isinstance(job_data, list) else job_data
print("\n── Commit Status ─────────────────────────────")
print(json.dumps({
    "job_id":    job_data.get("id"),
    "status":    job_data.get("status_str"),
    "result":    job_data.get("result_str"),
    "end_time":  job_data.get("end_ts"),
    "by":        job_data.get("uname"),
}, indent=2))

# ── Cleanup (uncomment to remove everything) ──────────────────────────────────
#scm.security_rule.delete_from_yaml('security_rules_config.yaml')
#scm.profile_group.delete_from_yaml('dns_security_config.yaml')
#scm.dns_security_profile.delete_from_yaml('dns_security_config.yaml')
#scm.edl.delete_from_yaml('edl_config.yaml')
