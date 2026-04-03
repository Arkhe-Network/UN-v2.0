# UN-v2.0: System Architecture (ONU 2.0) ⚙️

## System Overview

The UN-v2.0 platform is a federated governance network that integrates physical jurisdiction with digital sovereignty through a **Mesh-LLM** architecture.

### 1. Nostr-Mesh Layer (NIP Subagents)
- **NIP Subnets**: Each NIP (01, 34, 46, etc.) is a specialized subagent providing a core service.
- **Mesh-LLM Orchestration**: Orchestrates LLM reasoning across the distributed Nostr network.
- **Bittensor-style Incentives**: Governance "coherence" ($R$) determines subagent prioritization.

### 2. AO Gateway Layer
- **AO Gateway**: Federated interface to the global AO network.
- **Compliance Ledger**: Immutable Arweave/AO-based record of jurisdictional state.

### 3. MCP Tool Layer (Agentic Skills)
- **MCP Servers**: Extensible tools for subagents to interact with the environment (e.g., `sign_governance_event`).
- **Arborization**: Subagents autonomously expand their skills by attaching new MCP servers.

### 4. Governance Dashboard (ONU 2.0 Validator)
- **Real-time Status**: Monitoring of AO, GPS, and Mesh-LLM health.
- **Subagent Scoring**: Visualizing the performance and coherence of each NIP-subnet.
- **Project Lifecycle**: Submission and automated compliance check.

## Component Interaction

1. **Submission**: A project is submitted via the **ONU 2.0 Dashboard**.
2. **NIP Orchestration**: The **Discovery Subagent (NIP-89)** identifies the required **NIP-subnets**.
3. **Execution**: The **Git Subagent (NIP-34)** prepares the code, while the **GPS Validator** verifies location.
4. **Validation**: The **AO Gateway** sends the project to the **Compliance Ledger**.
5. **Synchronization**: The jurisdictional state is synchronized across the entire governance mesh.

---
*Built for the Age of Coherence.*
