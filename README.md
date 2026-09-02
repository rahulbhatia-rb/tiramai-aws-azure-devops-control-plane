# Tiramai AWS/Azure DevOps Control Plane

Independent proof-of-work inspired by Tiramai.ai's public Senior DevOps Engineer / Lead role.

This project models an AWS-first, Azure-secondary platform contract for enterprise SaaS and AI-native workloads. It focuses on reliable delivery, EKS, Terraform, GitHub Actions, observability, security, release management, backup/DR, and consistent DevOps standards.

> Based only on the public role description. It does not represent Tiramai.ai's private architecture.

## Architecture

```text
Developers
   |
   v
GitHub Actions
   |
   +--> test / lint / scan
   +--> terraform plan
   +--> container build
   +--> policy gate
   |
   v
ECR / artifact registry
   |
   v
EKS / ECS / Lambda
   |
   +--> Helm
   +--> rolling / blue-green / canary
   +--> IAM / Secrets Manager
   +--> VPC / ALB / Route53 / CloudFront
   |
   v
Observability
   |
   +--> CloudWatch
   +--> Prometheus / Grafana
   +--> OpenTelemetry
   +--> logs / traces / SLOs
```

## Platform contract

### AWS
- EKS production baseline
- EC2/ECS/Lambda service ownership
- ECR image lifecycle
- RDS backup / restore
- S3 encryption / lifecycle
- IAM least privilege
- VPC segmentation
- Route 53 ownership
- CloudFront controls
- CloudWatch telemetry
- Secrets Manager rotation

### Azure
Azure is treated as a secondary cloud rather than forcing artificial symmetry.

The contract validates identity, network boundaries, deployment ownership, logging/alerting, secret handling, backup/restore, and environment parity expectations.

### Kubernetes / EKS
- requests / limits
- probes
- PodDisruptionBudgets
- autoscaling
- topology spread
- workload identity
- NetworkPolicy
- Helm release ownership
- rollback strategy
- node / cluster upgrade readiness

### CI/CD
- required reviews
- short-lived credentials
- IaC validation
- vulnerability scanning
- immutable artifacts
- environment approvals
- deployment health gates
- rollback
- release audit trail

### Observability
- metrics
- logs
- traces
- correlation IDs
- SLOs
- owned alerts
- runbooks
- deployment markers
- capacity signals
- cost telemetry

### Reliability
- backup policy
- restore tests
- RTO / RPO
- multi-AZ
- dependency mapping
- graceful degradation
- rollback
- DR runbook

### Security
- IAM reviews
- secret rotation
- vulnerability scans
- infrastructure hardening
- TLS
- encryption at rest
- audit logging
- privileged-access review

## Release strategy

Use the smallest safe blast radius:

1. validate artifact
2. deploy to non-prod
3. run smoke / integration tests
4. canary or small cohort
5. evaluate health / SLO gate
6. expand rollout
7. automatic stop / rollback on breach

## Developer experience

Teams should inherit Terraform modules, GitHub Actions templates, Helm chart conventions, observability defaults, tagging / ownership, alert routing, environment patterns, and rollback conventions.

The safe path should be the easiest path.

## 30 / 60 / 90 day plan

### 0-30
- map AWS/Azure estate
- baseline EKS, Terraform and CI/CD
- identify recurring production/release issues
- map observability and security gaps
- review backup/restore readiness

### 31-60
- standardize Terraform modules
- improve GitHub Actions templates
- harden EKS baseline
- define SLO / alert ownership
- improve release health gates

### 61-90
- automate environment creation
- validate DR
- improve cost attribution
- reduce deployment toil
- mentor engineers around reusable platform standards

## Run locally

```bash
python -m unittest -v tests.test_gate
python src/cli.py examples/production.json
python src/cli.py examples/unsafe.json
```
