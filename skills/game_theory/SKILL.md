name: game_theory
version: 1.0.0
description: "Simulação de teoria dos jogos para o CSNU com matriz de payoff corrigida."
inputs:
  - name: config
    type: string
    description: "JSON configuration for the simulation."
  - name: jurisdiction
    type: string
    description: "Jurisdiction context."
outputs:
  - name: plot_path
    type: string
    description: "Path to the generated simulation plot."
  - name: summary
    type: string
    description: "Summary of the simulation results."
capabilities:
  - game_theory
  - replicator_dynamics
  - unsc_simulation
