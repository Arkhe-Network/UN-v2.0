# Arkhe-Ω Simulation Parameters: 10-Year Coherence Horizon

This document defines the variables for simulating the stability of $R(t)$ (Global Coherence) and the viability of $\lambda\Omega$ tokenomics over a 10-year period.

---

## 1. Physical Degradation Variables

| Variable | Base Value | Range | Unit | Description |
|----------|------------|-------|------|-------------|
| $T_2^*_{\text{decay}}$ | 0.5% | 0.1% - 1.2% | / Year | Natural degradation of NV center coherence over time. |
| $T_{\text{repair}}$ | 30 | 10 - 90 | Days | Average time to replace a QD or VCSEL after failure. |
| $N_{\text{active}}$ | 1,000 | 500 - 5,000 | Nodes | Number of active nodes in the mesh. |
| $N_{\text{standby}}$ | 500 | 250 - 2,500 | Nodes | Number of standby nodes for redundancy. |

---

## 2. Economic Variables

| Variable | Base Value | Adjustment | Unit | Description |
|----------|------------|------------|------|-------------|
| $S_{\text{total}}$ | 750M | 500M - 1B | $\lambda\Omega$ | Total staked supply (minimum vs. optimal). |
| $E_{\text{annual}}$ | 1% | 0.5% - 2.5% | / Year | Inflationary emission rate. |
| $F_{\text{handover}}$ | 0.5% | 0.1% - 1.5% | / Event | Fee paid during node state transfer. |
| $R_{\text{slashing}}$ | 10% | 5% - 50% | / Infraction | Penalty for non-reporting or critical failure. |
| $B_{\text{lockup}}$ | 5% | 0% - 10% | / Year | Reputation bonus for long-term lockup. |

---

## 3. Governance & External Factors

| Variable | Base Value | Unit | Description |
|----------|------------|------|-------------|
| $P_{\lambda\Omega}$ | 1.00 | USD/$\lambda\Omega$ | Relative market value of the governance token. |
| $C_{\text{hardware}}$ | 50,000 | USD | Cost to acquire a new high-purity Quantum Diamond (QD). |
| $U_{\text{handshake}}$ | 1,000,000 | / Day | Average number of network-wide coherence checks. |

---

## 4. Success Metrics (Target KPIs)

1. **Coherence Stability:** $R(t)$ must remain $> 0.95$ globally.
2. **Sustainability:** Coherence Reserve Fund must grow by $> 2\%$ annually (inflation-adjusted).
3. **Redundancy Ratio:** $N_{\text{standby}} / N_{\text{active}}$ should be $\geq 0.5$.
4. **Staking Participation:** $> 70\%$ of circulating $\lambda\Omega$ should be staked or locked.

---

## 5. Simulation Scenarios

- **Scenario A (Steady State):** Nominal degradation and consistent staking.
- **Scenario B (Rapid Decay):** Accelerated $T_2^*$ decay (e.g., radiation event) tests the Coherence Reserve's ability to fund mass hardware replacement.
- **Scenario C (Economic Shock):** 50% drop in $\lambda\Omega$ price tests if handover fees can sustain the mesh independently of emission.
- **Scenario D (Governance Gridlock):** MuSig2 council fails to approve Treasury grants for 6 months.
