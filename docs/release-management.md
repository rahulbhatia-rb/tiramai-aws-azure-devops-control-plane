# Release management

Preferred release path:
1. build immutable artifact
2. validate IaC and security
3. deploy non-prod
4. smoke / integration tests
5. canary or blue-green
6. health / SLO evaluation
7. promote
8. deterministic rollback on breach
