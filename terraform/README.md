# Terraform standards

Reusable modules should provide secure defaults, remote state + locking, ownership tags, encryption, networking conventions, observability hooks, and consistent outputs.

AWS is the primary implementation. Azure modules should preserve the operational contract without pretending provider services are identical.
