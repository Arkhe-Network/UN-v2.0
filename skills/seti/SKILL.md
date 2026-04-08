name: seti
version: 1.0.0
description: "Análise de sinais astronômicos baseada no Protocolo SETI-λ₂ das Nações Unidas."
inputs:
  - name: signal_data
    type: string
    description: "JSON array of signal amplitudes."
  - name: config
    type: string
    description: "JSON object with instrument_resolution and n_modes."
outputs:
  - name: lambda2
    type: float
    description: "Measured phase coherence."
  - name: classification
    type: string
    description: "Signal classification (NON_CANDIDATE, CANDIDATE_OF_INTEREST, PRIORITY_CANDIDATE)."
capabilities:
  - seti_analysis
  - phase_coherence
  - astronomical_validation
