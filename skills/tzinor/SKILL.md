name: tzinor
version: 1.0.0
description: "Protocolo de Handshake Interestelar Tzinor. Transmissão de tranças topológicas."
inputs:
  - name: target
    type: string
    description: "Sistema alvo (ex: Alpha Centauri)."
  - name: oracle_alert
    type: string
    description: "Nível de alerta do Oráculo CMB."
outputs:
  - name: transmission_status
    type: string
    description: "Status da transmissão (TRANSMITTING, HALTED)."
  - name: payload_hash
    type: string
    description: "Hash da trança enviada."
capabilities:
  - interstellar_communication
  - phase_modulation
  - silence_protocol
