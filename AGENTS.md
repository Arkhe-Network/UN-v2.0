# AGENTS.md

## Project Standards for Developers and Automated Agents

This project follows strict architectural and legal guidelines to ensure suitability for UN-regulated geogovernance environments. All code changes and architectural decisions MUST adhere to the following standards:

### 1. Security First
- **Control Plane Isolation:** Physical and logical separation of public telemetry from privileged control traffic.
- **Authentication:** All control APIs MUST use mutual TLS (mTLS) for workload identity and short-lived, sender-constrained (DPoP) JWTs for user authorization.
- **Zero-Trust:** Use the SPIFFE framework for workload identities and OIDC/SAML for human identities.

### 2. Legal and Compliance
- **Data Privacy:** All data processing, especially GPS data, must comply with LGPD (Brazil) and GDPR (EU).
- **Pseudonymization:** Personal Identifiable Information (PII) MUST be isolated in an encrypted "PII Vault". Only pseudonymous identifiers should be recorded in public or audit ledgers.
- **Local Residency:** Prioritize data storage in regions with legal adequacy (e.g., AWS São Paulo or UNICC infrastructure).

### 3. Ontological Design
- **Open Standards:** Use GeoSPARQL for geospatial data and PROV-O for provenance tracking.
- **Interoperability:** Align with SKOS, GeoDCAT-AP, and ISO 19115 metadata profiles.
- **Validation:** Use Shapes Constraint Language (SHACL) for ensuring data integrity and consistency within the ontology.

### 4. Verifiable Ledger (Compliance Ledger)
- **Immutable Audit Trail:** Implement using a Merkle Tree structure over an append-only database.
- **Legal Anchoring:** Root hashes MUST be periodically anchored to ICP-Brasil (DOC-ICP-12) to ensure evidentiary weight.

### 5. Sandboxed Execution (AO Sandbox)
- **Layered Isolation:** Use MicroVMs (Firecracker/Kata) for high-risk execution and WASM for low-latency tasks.
- **Egress Controls:** Implement "deny-by-default" network egress policies (e.g., via Cilium).
- **Monitoring:** Utilize Falco for anomaly detection and automated "kill-switch" responses.

### 6. Transparency and Open Source
- **Licensing:** All code must be licensed under Apache 2.0.
- **Auditability:** Provide Software Bill of Materials (SBOM) signed with Sigstore/Cosign.
- **Integrity:** Avoid using "AGI" or other hyperbolic branding; focus on verifiable technical capabilities.

### 7. Version Control and Security Hygiene
- **No Binaries:** Compiled binaries, object files, and secrets (keys, certs, .env files) MUST NOT be committed to the repository. Use `.gitignore` to prevent accidental commits.

---
*Failure to comply with these standards will result in the rejection of pull requests.*
