# UN-v2.0: Quantum State Transfer & QD Handover Protocol 🌌

## Overview

To prevent information vacuums and maintain network coherence ($R(t)$), UN-v2.0 (ONU 2.0) implements a **Quantum Handover Protocol** for nodes transitioning out of the mesh (due to retirement, slashing, or failure).

## 1. Quantum Teleportation of Memory States

Stored quantum states (session keys, EPR pairs, ZK anchors) cannot be copied (No-Cloning Theorem). Instead, they are **teleported** from the old node (Node_R) to the replacement (Node_S).

### 1.1. EPR Pair Pre-requisite
During a 24-hour **smooth handover** period, Node_R and Node_S establish a dedicated EPR pair via standard handshake (Bell violation confirmed).

### 1.2. Teleportation Workflow
1. **Preparation**: Node_R prepares the state $|\psi\rangle$ in an NV-center diamond.
2. **Bell Measurement**: Node_R performs a Bell measurement between $|\psi\rangle$ and its half of the EPR pair.
3. **Classical Correction**: Node_R sends the 2-bit measurement result to Node_S via an authenticated classical channel (qhttp).
4. **Recovery**: Node_S applies the corresponding Pauli correction (X, Z, or XZ) to its half of the EPR pair, reconstructing $|\psi\rangle$.

## 2. Preventing the Information Vacuum

### 2.1. Dual Routing & Overlap
- **Coexistence**: Node_R and Node_S operate simultaneously for 24h.
- **Double Routing**: The coordinator sends duplicate messages to both nodes until Node_S is fully operational.
- **Message Buffering**: Neighbors maintain a circular buffer of messages to prevent loss during the transition.

### 2.2. Distributed Backup
Critical states are replicated across two other QD nodes using a **[[5,1,3]] quantum error correction code**, allowing for state reconstruction if Node_R fails abruptly before the handover completes.

---
*Ensuring the Giza Resonance remains uninterrupted.*
