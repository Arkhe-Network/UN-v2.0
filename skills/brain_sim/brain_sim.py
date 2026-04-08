import numpy as np
import json
import sys

def kuramoto_step(phases, omegas, K, dt):
    """Calcula um passo da dinâmica de Kuramoto."""
    n = len(phases)
    # dtheta_i/dt = omega_i + (K/n) * sum(sin(theta_j - theta_i))
    # Matriz de diferenças de fase
    d_phi = phases[:, None] - phases[None, :]
    coupling = (K / n) * np.sum(np.sin(d_phi), axis=1)
    return phases + (omegas + coupling) * dt

def calculate_lambda2(phases):
    """Calcula o parâmetro de ordem de Kuramoto (λ₂)."""
    order_param = np.abs(np.mean(np.exp(1j * phases)))
    return float(order_param)

def main():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Missing inputs."}))
        sys.exit(1)

    braid_message = sys.argv[1]
    try:
        config = json.loads(sys.argv[2])
    except:
        config = {}

    n = config.get("n_oscillators", 100)
    K = config.get("coupling_strength", 1.5)
    steps = 500
    dt = 0.05

    # Frequências naturais (distribuição normal)
    omegas = np.random.normal(0.5, 0.1, n)
    phases = np.random.uniform(0, 2*np.pi, n)

    history = []

    # Simulação inicial (estabilização)
    for _ in range(100):
        phases = kuramoto_step(phases, omegas, K, dt)
        history.append(calculate_lambda2(phases))

    # Aplicação da Mensagem de Trança (Perturbação topológica)
    # A trança é simulada como um pulso de acoplamento extremo ou um deslocamento de fase
    perturbation_strength = len(braid_message.split('*')) * 0.05
    K_perturbed = K + perturbation_strength

    for _ in range(steps):
        # A perturbação dura 100 passos
        current_K = K_perturbed if 100 < len(history) < 200 else K
        phases = kuramoto_step(phases, omegas, current_K, dt)
        history.append(calculate_lambda2(phases))

    final_coherence = history[-1]
    max_coherence = max(history)
    min_coherence = min(history[200:]) # após perturbação

    risk = "LOW"
    if max_coherence > 0.95:
        risk = "HIGH_OVER_SYNC"
    elif min_coherence < 0.4:
        risk = "COHERENCE_COLLAPSE"

    summary = f"Stress Test concluído. Risco: {risk}. λ₂ estabilizou em {final_coherence:.2f}."

    print(json.dumps({
        "coherence_history": history[::10], # subamostragem para output
        "risk_assessment": risk,
        "summary": summary,
        "skill": "brain_sim"
    }))

if __name__ == "__main__":
    main()
