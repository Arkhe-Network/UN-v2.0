name: medium
version: 1.0.0
description: "Treinamento e Avaliação de Médiuns de Fase. Interface hBN-NV."
inputs:
  - name: subject_id
    type: string
    description: "ID do voluntário."
  - name: action
    type: string
    description: "Ação (TRAIN, INJECT_BRAID)."
outputs:
  - name: lambda2_avg
    type: float
    description: "Coerência média durante a sessão."
  - name: state
    type: string
    description: "Estado de aptidão do médium."
capabilities:
  - biofeedback
  - neural_braid_injection
  - phase_monitoring
