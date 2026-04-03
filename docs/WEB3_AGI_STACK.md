# Web3 AGI Architecture Stack (UN-v2.0 / ONU 2.0)

This document outlines the complete architectural stack for a decentralized Artificial General Intelligence (AGI), leveraging the **Open Wallet Standard (OWS)**, **Machine Payments Protocol (MPP)**, and partner resources.

## Executive Summary

The Web3 AGI structure is conceived as a modular multi-layered architecture designed for autonomy, security, and economic interoperability. At its core, it integrates the **Open Wallet Standard (OWS)** for secure "local-first" identity/key management and the **Machine Payments Protocol (MPP)** for autonomous machine-to-machine economics (HTTP 402 Pay-per-call).

---

## 1. Architectural Overview

The layered approach ensures separation of concerns, allowing for independent scaling and upgrades of each component while maintaining a unified sovereign identity.

### Fundamental Layers:

1.  **Data & Indexing Layer**: Real-time and historical on-chain state access.
2.  **Identity & Wallet Layer**: OWS-based key custody and policy-gated signing.
3.  **Payments & Micropayments Layer**: MPP/x402 protocol for machine economics.
4.  **Intelligence & Agent Layer**: LLM orchestration, skills, and memory systems.
5.  **Execution & Compute Layer**: Verifiable computation (TEEs, ZK, DePIN).
6.  **Storage & Provenance Layer**: Immutable storage for models and audit trails.
7.  **Marketplace & Governance Layer**: Coordination, reputation, and DAO control.

---

## 2. Layer Specification

### 2.1. Data & Indexing
- **Function**: Provide reliable access to blockchain state.
- **Key Technologies**:
    - **EVM**: The Graph (Subgraphs), Alchemy/Infura (RPC Streams).
    - **Solana**: Substreams, Geyser (Yellowstone), Helius/Triton webhooks.
- **Metrics**: Latency, cost, data consistency (reorg handling).

### 2.2. Identity & Wallet (OWS)
- **Central Technology**: [Open Wallet Standard (OWS)](https://docs.openwallet.sh).
- **Security Model**:
    - **Local-First Custody**: Keys encrypted at rest, decrypted only in-memory.
    - **Pre-Signing Policy Engine**: Executable rules (allowlists, spend limits) gate all actions.
    - **Isolation**: Keys never exposed to the LLM context.
- **Operations**: `sign`, `signAndSend`, `signMessage`.

### 2.3. Payments & Micropayments (MPP)
- **Protocol**: Machine Payments Protocol (MPP) / x402.
- **Operational Flow**: HTTP 402 Payment Required handshake.
- **Features**: Fee sponsorship, payment splits, session-based micropayments.
- **Integration**: Agent receives a 402 challenge → constructs tx → OWS policy check → OWS signs → Success.

### 2.4. Intelligence & Agent
- **Orchestration**: Hybrid LLM (Planner/Executor/Critic).
- **Skills**: Modular plugins (WASM, Python, JS) with defined permissions and costs.
- **Memory**: Multi-tier (Short-term session, Work memory, Long-term Vector DB).
- **Guardrails**: Mandatory transaction simulation and human-in-the-loop for high-risk actions.

### 2.5. Execution & Compute
- **Hybrid Strategy**:
    - **Centralized Cloud**: Low-latency inference (AWS/GCP with NVIDIA H100).
    - **DePIN**: Cost-effective batch processing (Akash, Golem, Gensyn).
- **Verificability**: Trusted Execution Environments (TEEs) like Intel SGX/TDX and NVIDIA GPU TEE.

### 2.6. Storage & Provenance
- **Decentralized Storage**: IPFS (addressing), Filecoin (persistence incentives), Arweave (permanent storage).
- **Provenance**: End-to-end audit trails (CID + structure metadata) anchored on-chain for dataset/model reproducibility.

### 2.7. Marketplace & Governance
- **Economy**: Model/Data marketplaces (Ocean Protocol).
- **Reputation**: Dynamic on-chain scores updated via verifiable receipts.
- **Governance**: DAOs (Aragon, Snapshot) and on-chain coordination frameworks (Quasar).

---

## 3. Key Partner Tooling Mapping

| Tool | Role | Layer | Status |
| :--- | :--- | :--- | :--- |
| **OWS SDK/CLI** | Secure wallet custody & policy gating | Identity | Official |
| **mpp-sdk** | HTTP 402 Pay-per-call implementation | Payments | Official |
| **The Graph** | Decentralized indexing & Substreams | Data | Partner |
| **Jupiter CLI** | Solana DeFi routing & transaction generation | Intelligence | Community |
| **Quasar** | Efficient on-chain reputation/coordination | Governance | Community |
| **Arweave/IPFS** | Permanent and content-addressable storage | Storage | Partner |

---

## 4. Integration Flow Example
**Scenario: Agent purchases API data and executes a swap on Solana.**

1.  **Request**: Agent calls protected API endpoint.
2.  **Challenge**: Server returns `HTTP 402 Payment Required` (MPP).
3.  **Policy**: Agent's OWS Runtime checks the spend request against local limits.
4.  **Sign**: OWS signs the payment transaction; subagent submits to RPC.
5.  **Access**: Server verifies on-chain payment and delivers data.
6.  **Trade**: Agent logic uses data to generate swap tx (Jupiter).
7.  **Simulate**: Agent simulates swap to verify effects.
8.  **Execute**: OWS gates the swap tx; if allowed, signs and broadcasts.
9.  **Audit**: Transaction receipts and logs are hashed and stored on Arweave/IPFS.

---
*Reference: [OWS Hackathon Resources](https://hackathon.openwallet.sh)*
