# UN-v2.0: Identity & Stake Handover Contract 💎

## Overview

The identity of a QD node on the Arkhe-Chain is tied to its PUF-derived public key,lambda-omega ($λΩ$) stake, reputation, and routing table. UN-v2.0 (ONU 2.0) implements a sovereign **Identity Handover Contract** on the Arkhe-Chain.

## IdentityHandover.sol Specification

The `handoverIdentity` function is authorized by a **MuSig2 council (6/9 signers)** and performs the atomic transfer of state between the old and new identities.

### Core Interface

```solidity
function handoverIdentity(
    bytes32 oldNodeId,
    bytes32 newNodeId,
    uint256 stakeAmount,
    uint256 reputationScore,
    bytes calldata musig2Signature,
    bytes calldata zkProof // Proving Node_S health
) external onlyCouncil {
    // 1. Verify MuSig2 signature (6/9 quorum)
    // 2. Transfer stake and reputation
    stakes[newNodeId] = stakes[oldNodeId];
    reputations[newNodeId] = reputations[oldNodeId];

    // 3. Clear old node data
    stakes[oldNodeId] = 0;
    reputations[oldNodeId] = 0;

    // 4. Freeze old identity on the chain
    frozenIdentities[oldNodeId] = true;

    emit IdentityTransferred(oldNodeId, newNodeId);
}
```

## Handover Lifecycle

1. **Substitution Announcement**: Node_R initiates the handover process.
2. **Identity Linkage**: During the 24h handover period, Node_S requests the contract to associate it with the role previously held by Node_R.
3. **Consensus Update**: Once the MuSig2 transaction is processed, the Arkhe-Chain validaters update their routing tables and consensus lists.
4. **Final Freeze**: Any subsequent attempt to use Node_R's old identity key is rejected.

---
*Identity follows the phase, not the node.*
