# ONU 2.0: Verifiable Geogovernance Roadmap (9–15 Months)

## Executive Summary
ONU 2.0 (SMC v2) is a functional prototype for multi-level governance featuring native GPS-based jurisdictional controls and a sandboxed execution environment. This project aims to transition this prototype into a production-ready platform suitable for UN-regulated environments by addressing critical security, legal, and operational gaps.

## Strategic Imperative
The primary objective is to expand ONU 2.0 from a prototype to a comprehensive geogovernance platform aligned with United Nations priorities. This involves implementing an interoperable ontology, enterprise-grade security, and robust evidentiary trails, while adhering to strict legal frameworks like LGPD (Brazil) and GDPR (EU).

## 9-15 Month Roadmap

### Immediate Actions (First 90 Days)
- **Security:** Seal the control plane with strong authentication (mTLS and short-lived JWTs). Transition to a zero-trust architecture.
- **Infrastructure:** Migrate from Replit to enterprise cloud (AWS São Paulo or UNICC) to mitigate data sovereignty and international transfer risks.
- **Transparency:** Move source code to a public repository (Apache 2.0), establish a Vulnerability Disclosure Program (VDP), and remove "AGI" branding to focus on verifiable capabilities.

### Mid-Term Goals (4-9 Months)
- **Ontological Design:** Implement a domain ontology based on open standards (GeoSPARQL, PROV-O) for semantic interoperability.
- **Verifiable Ledger:** Transform the "Compliance Ledger" into a cryptographically verifiable audit trail using Merkle trees anchored to ICP-Brasil (DOC-ICP-12).
- **Hardened Sandbox:** Enhance the AO Sandbox using MicroVMs (Firecracker/Kata) and WASM runtimes with strict egress controls.

### Long-Term Objectives (9-15 Months)
- **Pilot Programs:** Launch low-risk pilots (e.g., micro-donation eligibility, cultural heritage cataloging).
- **Compliance & Partnerships:** Finalize Data Protection Impact Assessments (DPIA), join the Esri Partner Network, and establish co-sell partnerships with cloud providers.

## Core Principles
- **Privacy by Design:** Use pseudonymization and PII vaults to comply with privacy laws while maintaining auditability.
- **Zero-Trust:** Identity-based security for both humans (SSO/OIDC) and workloads (SPIFFE).
- **Interoperability:** Use open standards and linked data to ensure multinational adoption.

---
*This project is an evolution of the SMC v2/Parallax AO platform.*
