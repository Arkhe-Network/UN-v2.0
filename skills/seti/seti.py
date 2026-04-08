import numpy as np
from scipy.signal import welch
import json
import sys

class SETILambda2Analyzer:
    TAU_CONSTANT = 0.96

    def __init__(self, instrument_resolution: float):
        self.resolution = instrument_resolution

    def compute_effective_dimension(self, n_modes: int) -> float:
        return np.log2(n_modes * self.resolution / 1000 + 1e-9)

    def compute_coherence(self, signal: np.ndarray) -> float:
        f, Pxx = welch(signal, nperseg=min(len(signal), 256))
        return float(np.mean(Pxx))

    def classify_target(self, lambda2: float, d: float) -> str:
        tau = self.TAU_CONSTANT / np.sqrt(max(d, 1e-9))
        if lambda2 < tau:
            return "NON_CANDIDATE"
        elif lambda2 < 1.5 * tau:
            return "CANDIDATE_OF_INTEREST"
        else:
            return "PRIORITY_CANDIDATE"

    def detect_vortex_intelligence(self, vortex_density: float, non_random_annihilation: bool) -> dict:
        """
        SETI-λ₂ v2.0: Topological vortex analysis.
        """
        T_BKT = 0.679  # Limiar para d=2

        if vortex_density > T_BKT and non_random_annihilation:
            return {
                'classification': 'ARTEFATO_TOPOLOGICO_PRIORITARIO',
                'vortex_density': vortex_density,
                'confidence': min(1.0, (vortex_density - T_BKT) / 0.321)
            }

        return {'classification': 'THERMAL_NOISE', 'vortex_density': vortex_density}

def main():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Missing inputs."}))
        sys.exit(1)

    try:
        signal_data = np.array(json.loads(sys.argv[1]))
        config = json.loads(sys.argv[2])
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

    res = config.get("instrument_resolution", 100000)
    n_modes = config.get("n_modes", 10)

    analyzer = SETILambda2Analyzer(res)
    d = analyzer.compute_effective_dimension(n_modes)
    lambda2 = analyzer.compute_coherence(signal_data)
    classification = analyzer.classify_target(lambda2, d)

    vortex_data = config.get("vortex_analysis", {})
    topological_report = {}
    if vortex_data:
        vortex_density = vortex_data.get("density", 0.0)
        non_random = vortex_data.get("non_random_annihilation", False)
        topological_report = analyzer.detect_vortex_intelligence(vortex_density, non_random)

    print(json.dumps({
        "lambda2": lambda2,
        "effective_dimension": d,
        "classification": classification,
        "topological_analysis": topological_report,
        "skill": "seti"
    }))

if __name__ == "__main__":
    main()
