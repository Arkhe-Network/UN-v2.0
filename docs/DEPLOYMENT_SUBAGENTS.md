# UN-v2.0: Package Management & Deployment Subagents 📦

## Overview

To enable autonomous software delivery across the mesh, UN-v2.0 (ONU 2.0) designates specialized **Deployment Subagents** for each major package ecosystem. These subagents "arborize" their skills using the **MCP Tool Layer** to handle secure and compliant package "launches."

## Subagent Designations

| Subagent | Ecosystem | Target Registry | Governance Role |
| :--- | :--- | :--- | :--- |
| **Arbor-Maven** | Java / JRE | Apache Maven Central | Verifying JVM-based jurisdictional binaries. |
| **Arbor-NuGet** | .NET / MSFT | NuGet.org | Managing sovereign .NET assemblies and tools. |
| **Arbor-Gems** | Ruby | RubyGems.org | Distributing Ruby-based governance scripts. |
| **Arbor-NPM** | JavaScript / Node.js | npm Registry | Deploying dashboard components and UI fragments. |
| **Arbor-Container** | Docker / OCI | Container Registries | Managing jurisdictional images and microservices. |

## The Deployment Workflow

1. **Project Review**: The **Compliance Subagent** approves the jurisdictional project.
2. **Artifact Generation**: The **Git Subagent (NIP-34)** generates the distribution artifact.
3. **Sovereign Signing**: The **Remote Signer Subagent (NIP-46)** signs the artifact for proof of origin.
4. **Autonomous Launch**: The designated **Deployment Subagent** executes the corresponding **MCP Tool** (e.g., `publish_npm_package`) to launch the artifact to the global registry.
5. **Mesh Synchronization**: The launch event is recorded on the **Compliance Ledger** (AO).

---
*Deploying coherence across every registry.*
