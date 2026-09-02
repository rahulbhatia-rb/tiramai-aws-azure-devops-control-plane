REQUIRED = {
    "aws": ["eks","ec2_ecs_lambda","ecr","rds_backup","s3_controls","iam_least_privilege","vpc_segmentation","route53_owner","cloudfront_controls","cloudwatch","secrets_rotation"],
    "azure": ["identity_model","network_boundary","deployment_owner","logging_alerting","secret_handling","backup_restore","environment_expectations"],
    "kubernetes": ["requests_limits","health_probes","pdb","autoscaling","topology_spread","workload_identity","network_policy","helm_ownership","rollback","upgrade_readiness"],
    "cicd": ["required_reviews","short_lived_credentials","iac_validation","vulnerability_scan","immutable_artifact","environment_approval","health_gate","rollback","release_audit"],
    "observability": ["metrics","logs","traces","correlation_ids","slos","alert_owner","runbooks","deployment_markers","capacity_signals","cost_telemetry"],
    "reliability": ["backup_policy","restore_test","rto_rpo","multi_az","dependency_mapping","graceful_degradation","rollback","dr_runbook"],
    "security": ["iam_review","secret_rotation","vuln_scan","hardening","tls","at_rest_encryption","audit_logs","privileged_access_review"],
    "standards": ["terraform_modules","gha_templates","helm_conventions","ownership_tags","release_process","environment_management","mentoring","docs"]
}

def evaluate(spec):
    findings=[]
    for section, fields in REQUIRED.items():
        values=spec.get(section,{})
        for field in fields:
            if not values.get(field):
                findings.append(f"{section}.{field} is required")
    return {"allowed": not findings, "findings": findings}
