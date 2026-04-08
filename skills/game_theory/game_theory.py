import numpy as np
import matplotlib.pyplot as plt
import json
import sys
import os

def replicator_dynamics(W, x, dt=0.01):
    """
    Standard Replicator Dynamics equation: dx_i/dt = x_i * (f_i(x) - avg_f(x))
    """
    f = np.dot(W, x)
    avg_f = np.dot(x, f)
    return x * (f - avg_f)

def run_simulation(steps=1000):
    # Payoff Matrix W (3x3)
    # Strategies: 0: Cooperate, 1: Block (Veto), 2: Exit (Alt Block)
    # Corrected payoffs based on Arkhe-Block 850.005
    W = np.array([
        [30, 10, 5],   # Cooperate
        [50, 20, 10],  # Block
        [70, 40, 30]   # Exit (Alternative Block/BRICS+)
    ])

    # Initial proportions (mostly cooperating, some blocking, few exiting)
    x = np.array([0.7, 0.2, 0.1])

    history = [x.copy()]

    for _ in range(steps):
        dx = replicator_dynamics(W, x)
        x = x + dx * 0.01
        x = np.clip(x, 0, 1)
        x = x / np.sum(x)
        history.append(x.copy())

    return np.array(history)

def main():
    history = run_simulation()

    plt.figure(figsize=(10, 6))
    plt.plot(history[:, 0], label='Cooperate (UNSC-SCA)', color='green')
    plt.plot(history[:, 1], label='Block (Veto Monopoly)', color='red')
    plt.plot(history[:, 2], label='Exit (Alternative Block)', color='blue')
    plt.title('UNSC Replicator Dynamics — Arkhe-Block 850.005 Corrected')
    plt.xlabel('Time Steps')
    plt.ylabel('Strategy Proportion')
    plt.legend()
    plt.grid(True)

    plot_path = 'simulation_results.png'
    plt.savefig(plot_path)

    summary = "Simulação concluída. O equilíbrio converge para a estratégia de 'Exit' devido ao alto payoff de blocos alternativos, validando a necessidade crítica de incentivos de coerência (λ₂) e circuit breakers para manter o P5 no sistema."

    print(json.dumps({
        "plot_path": plot_path,
        "summary": summary,
        "final_proportions": {
            "cooperate": float(history[-1, 0]),
            "block": float(history[-1, 1]),
            "exit": float(history[-1, 2])
        }
    }))

if __name__ == "__main__":
    main()
