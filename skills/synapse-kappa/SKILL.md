name: synapse-kappa
version: 1.0.0
description: "Geopolitical Game Theory Simulation and Smart Sanctions Engine."
inputs:
  - name: action
    type: string
    description: "The action to simulate (e.g., 'P5_VETO', 'REFORM_PROPOSAL')."
  - name: actor
    type: string
    description: "The actor performing the action (e.g., 'P5_Russia', 'G4_Brazil')."
  - name: metadata
    type: string
    description: "Optional metadata in JSON format (e.g., crisis type)."
outputs:
  - name: lambda2_global
    type: float
    description: "The global coherence value after the action."
  - name: status
    type: string
    description: "The simulation status and detected triggers."
  - name: report
    type: string
    description: "Detailed simulation report."
capabilities:
  - game_theory_simulation
  - geopolitical_modeling
  - smart_sanctions
  - sca_global_validation
