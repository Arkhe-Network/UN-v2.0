import numpy as np
import matplotlib.pyplot as plt

class VirtualBrain:
    def __init__(self, N=10000, K=1.2, dt=0.01):
        self.N = N
        self.K = K
        self.dt = dt
        # Grade 100x100 (topografia cortical)
        self.grid_size = int(np.sqrt(N))
        self.omega = np.random.normal(0, 0.2, N)  # frequências naturais
        self.theta = np.random.uniform(0, 2*np.pi, N)  # fases iniciais
        self.lambda_history = []

    def compute_order_parameter(self):
        z = np.mean(np.exp(1j * self.theta))
        return np.abs(z)

    def external_braid_signal(self, t, complexity=5):
        """
        Gera sinal externo baseado em uma trança de alta complexidade.
        """
        carrier = 40.0  # Hz (ritmo gama)
        modulation = 0.2 * np.sin(2*np.pi*complexity*t) * np.cos(2*np.pi*t)
        phase = 2 * np.pi * carrier * t + modulation
        return np.sin(phase)

    def step(self, t, ext_amp=0.0):
        # Simplificação para 10k osciladores: acoplamento de campo médio local ou global reduzido para performance
        # Usando aproximação de vizinhos próximos na grade
        dtheta = self.omega.copy()

        # Para performance Jules, vamos usar uma amostra representativa ou campo médio se N for muito grande
        # Aqui, vamos fazer o cálculo vetorizado para o campo médio global ponderado por K
        z = np.mean(np.exp(1j * self.theta))
        coupling = self.K * np.abs(z) * np.sin(np.angle(z) - self.theta)

        # Forçamento externo
        external = ext_amp * self.external_braid_signal(t, complexity=10) * np.sin(0 - self.theta)

        dtheta += coupling + external
        self.theta += dtheta * self.dt
        self.theta %= 2*np.pi

        lambda2 = self.compute_order_parameter()
        self.lambda_history.append(lambda2)
        return lambda2

    def run_stress_test(self, duration=30.0, ext_amp_start=0.0, ext_amp_peak=0.8, peak_time=15.0):
        steps = int(duration / self.dt)
        for step in range(steps):
            t = step * self.dt
            if t < peak_time:
                ext_amp = ext_amp_start + (ext_amp_peak - ext_amp_start) * (t / peak_time)
            elif t < peak_time + 5:
                ext_amp = ext_amp_peak
            else:
                ext_amp = max(0.0, ext_amp_peak * (1 - (t - peak_time - 5)/10.0))

            self.step(t, ext_amp=ext_amp)

        return np.array(self.lambda_history)

if __name__ == "__main__":
    brain = VirtualBrain(N=10000)
    lambda_hist = brain.run_stress_test(duration=30.0, ext_amp_peak=0.8, peak_time=15.0)

    plt.figure(figsize=(10,4))
    plt.plot(np.arange(0, 30, 0.01), lambda_hist)
    plt.axvline(15, color='r', linestyle='--', label='Início mensagem')
    plt.axvline(20, color='r', linestyle='--', label='Fim mensagem')
    plt.xlabel('Tempo (s)')
    plt.ylabel('λ₂ (coerência)')
    plt.title('Stress Test: Impacto de Mensagem Exógena no Cérebro Virtual')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.savefig('brain_stress_test.png')

    print(f"Stress test completed. Final λ₂: {lambda_hist[-1]:.4f}")
