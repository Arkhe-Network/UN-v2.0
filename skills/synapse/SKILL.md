name: synapse
version: 1.0.0
description: "Calcula métricas λ₂-Global e monitora a coerência de fase do sistema de governança."
inputs:
  - name: geopolitical_data
    type: string
    description: "JSON object containing regional representation and decision metrics."
  - name: jurisdiction
    type: string
    description: "The jurisdiction context (usually GLOBAL)."
outputs:
  - name: lambda_global
    type: float
    description: "The calculated global coherence score (λ₂)."
  - name: dashboard
    type: string
    description: "Visual dashboard representation of the coherence state."
capabilities:
  - coherence_monitoring
  - kuramoto_sincronization
  - geopolitical_analysis
