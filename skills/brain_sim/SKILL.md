name: brain_sim
version: 1.0.0
description: "Simula o impacto de mensagens exógenas (tranças) na coerência de um cérebro humano virtual."
inputs:
  - name: braid_message
    type: string
    description: "The encoded braid word (e.g., σ1 * σ2_inv * σ1)."
  - name: config
    type: string
    description: "Brain simulation parameters (n_oscillators, coupling_strength)."
outputs:
  - name: coherence_history
    type: array
    description: "λ₂ values over time during the stress test."
  - name: risk_assessment
    type: string
    description: "Assessment of coherence collapse or over-sync risk."
capabilities:
  - kuramoto_brain_model
  - braid_perturbation
  - coherence_stress_test
