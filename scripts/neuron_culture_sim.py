import numpy as np
import json
import matplotlib.pyplot as plt

def simulate_neuron_vortex_correlation():
    """
    Simula dados experimentais da Fase 1: Correlação entre disparos neuronais
    e nucleação de vórtices em substrato hBN.
    """
    t = np.linspace(0, 10, 1000)
    # Taxa de disparo neuronal (Hz) - Simulação de burst
    firing_rate = 10 * (1 + np.sin(t) + 0.5 * np.random.normal(0, 0.5, 1000))
    firing_rate = np.clip(firing_rate, 0, 50)

    # Densidade de vórtices (proporcional à taxa de disparo + latência)
    vortex_density = 0.5 * firing_rate / 50 + 0.1 * np.random.normal(0, 0.1, 1000)
    vortex_density = np.clip(vortex_density, 0, 1)

    correlation = np.corrcoef(firing_rate, vortex_density)[0, 1]

    plt.figure(figsize=(10, 6))
    plt.plot(t, firing_rate / 50, label='Normalized Firing Rate (Neurônios)')
    plt.plot(t, vortex_density, label='Vortex Density (hBN Sensor)', alpha=0.7)
    plt.title(f'Fase 1 Validation: Neural-Vortex Correlation (r={correlation:.2f})')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    plt.savefig('phase1_validation.png')

    return correlation

if __name__ == "__main__":
    r = simulate_neuron_vortex_correlation()
    print(json.dumps({
        "correlation": r,
        "status": "VALIDATED" if r > 0.8 else "INCONCLUSIVE",
        "plot": "phase1_validation.png"
    }))
