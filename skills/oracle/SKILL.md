name: oracle
version: 1.0.0
description: "Oráculo de Monitoramento de Coerência Cósmica. Busca por padrões de trança na CMB."
inputs:
  - name: config
    type: string
    description: "Configurações do scan (resolution, band)."
outputs:
  - name: candidates
    type: array
    description: "Lista de candidatos a tranças naturais detectados."
  - name: alert_level
    type: string
    description: "Nível de alerta para o Protocolo de Silêncio."
capabilities:
  - cmb_analysis
  - phase_singularity_detection
  - braid_search
