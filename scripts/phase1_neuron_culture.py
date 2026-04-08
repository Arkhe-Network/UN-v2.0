import numpy as np
import matplotlib.pyplot as plt

class NeuronCulture:
    def __init__(self, n_electrodes=16):
        self.n = n_electrodes

    def stimulate(self, frequency=20, duration=30.0, dt=0.001):
        t = np.arange(0, duration, dt)
        spikes = np.zeros(len(t))
        for i in range(self.n):
            spike_train = np.random.poisson(frequency * dt, len(t))
            spikes += spike_train
        field = np.convolve(spikes, np.exp(-t[:100]/0.01), mode='same')
        return t, field

    def detect_vortices(self, field):
        vortex_density = np.abs(field)**2 / 1000
        return vortex_density

    def run(self):
        t, field = self.stimulate(frequency=40, duration=30.0)
        vortex = self.detect_vortices(field)

        plt.figure(figsize=(10,4))
        plt.plot(t, field / (np.max(field)+1e-9), label='Campo elétrico (normalizado)')
        plt.plot(t, vortex / (np.max(vortex)+1e-9), label='Densidade de vórtices', alpha=0.7)
        plt.xlabel('Tempo (s)')
        plt.ylabel('Amplitude normalizada')
        plt.title('Fase 1: Cultura de Neurônios – Correlação atividade vs. vórtices')
        plt.legend()
        plt.grid(alpha=0.3)
        plt.savefig('phase1_neuron_culture.png')
        print("Phase 1 simulation completed.")

if __name__ == "__main__":
    culture = NeuronCulture()
    culture.run()
