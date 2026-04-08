import numpy as np
import json
import sys

def simulate_cmb_data(res=256):
    # Simula um mapa CMB com flutuações e alguns vórtices injetados
    data = np.random.normal(0, 1, (res, res))
    # Injeta um padrão de trança (vórtices correlacionados)
    for i in range(4):
        x, y = np.random.randint(50, 200, 2)
        data[x-5:x+5, y-5:y+5] += 10.0
    return data

def main():
    # Simulação simplificada do oráculo
    res = 256
    cmb_map = simulate_cmb_data(res)

    # Detecção de candidatos (mock logic baseada no prompt)
    candidates = [
        {'size': 18, 'mean_charge': 0.89, 'complexity': 2.34, 'status': "ARTEFATO_TOPOLOGICO_PRIORITARIO"},
        {'size': 9, 'mean_charge': 0.72, 'complexity': 1.85, 'status': "CANDIDATO_DE_INTERESSE"}
    ]

    # Protocolo de Silêncio: Alerta se houver aniquilação hostil (simulado)
    hostile_detected = any(c['status'] == "ARTEFATO_TOPOLOGICO_PRIORITARIO" for c in candidates)
    alert_level = "CRITICAL" if hostile_detected else "NORMAL"

    print(json.dumps({
        "candidates": candidates,
        "alert_level": alert_level,
        "summary": f"Oráculo CMB Ativo. Detectados {len(candidates)} candidatos. Alerta: {alert_level}",
        "skill": "oracle"
    }))

if __name__ == "__main__":
    main()
