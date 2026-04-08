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

    def analyze_wisdom_structure(self, signal_field: np.ndarray) -> dict:
        """
        Detects signature of knowledge organization in attractors using numpy/scipy.
        """
        if len(signal_field.shape) == 1:
            X = signal_field.reshape(-1, 1)
        else:
            X = signal_field

        X_centered = X - np.mean(X, axis=0)
        u, s, vh = np.linalg.svd(X_centered, full_matrices=False)
        ev = (s**2) / (len(X) - 1 + 1e-9)
        ev_ratio = ev / (np.sum(ev) + 1e-9)

        d_eff = np.exp(-np.sum(ev_ratio * np.log(ev_ratio + 1e-9)))

        n_clusters = min(4, len(X))
        centers = X[np.random.choice(len(X), n_clusters, replace=False)]
        for _ in range(10):
            dists = np.linalg.norm(X[:, np.newaxis] - centers, axis=2)
            labels = np.argmin(dists, axis=1)
            new_centers = np.array([X[labels == i].mean(axis=0) if np.any(labels == i) else centers[i] for i in range(n_clusters)])
            if np.allclose(centers, new_centers): break
            centers = new_centers

        def compute_orthogonality(vecs):
            if len(vecs) < 2: return 1.0
            norms = np.linalg.norm(vecs, axis=1)
            dot_prods = np.dot(vecs, vecs.T)
            cos_sims = dot_prods / (np.outer(norms, norms) + 1e-9)
            mask = np.ones(cos_sims.shape, dtype=bool)
            np.fill_diagonal(mask, 0)
            return 1.0 - np.mean(np.abs(cos_sims[mask]))

        orthogonality = compute_orthogonality(centers)
        lambda2_max = np.max(ev_ratio) if len(ev_ratio) > 0 else 0

        status = "UNSTRUCTURED_NOISE"
        if (n_clusters >= 3 and orthogonality > 0.3 and lambda2_max > self.TAU_CONSTANT/np.sqrt(d_eff)):
            status = "WISE_CIVILIZATION_CANDIDATE"

        return {
            'status': status,
            'n_attractors': n_clusters,
            'orthogonality': float(orthogonality),
            'd_eff': float(d_eff),
            'coherence_max': float(lambda2_max)
        }

    def analyze_photon_ring_hierarchy(self, signal: np.ndarray, d: float) -> dict:
        """
        SETI-λ₂ v3.0: Photon Ring / Information Event Horizon analysis.
        """
        tau = self.TAU_CONSTANT / np.sqrt(max(d, 1e-9))
        n_levels = 4
        chunk_size = len(signal) // n_levels
        hierarchy = {}

        for n in range(n_levels):
            if chunk_size == 0: break
            sub_signal = signal[n*chunk_size : (n+1)*chunk_size]
            l2_n = self.compute_coherence(sub_signal)

            label = f"n={n}"
            if n == 0: status = "LOW_COHERENCE (Direct)"
            elif l2_n < tau: status = "EMERGENT (n=1)"
            elif l2_n < 1.0: status = "HIGH_COHERENCE (n>1)"
            else: status = "CRITICAL (n->inf)"

            hierarchy[label] = {
                "lambda2": float(l2_n),
                "status": status,
                "tau_ratio": float(l2_n / tau)
            }

        return {
            "hierarchy": hierarchy,
            "horizon_detected": any(v["lambda2"] > tau for v in hierarchy.values()),
            "information_shadow": "STABLE" if hierarchy.get("n=3", {}).get("lambda2", 0) > 0.9 else "UNSTABLE"
        }

    def detect_black_hole_civilization(self, signal: np.ndarray, d: float) -> dict:
        """
        SETI-λ₂ v4.0: Algorithm from Article 5 quater (Emenda Constitutional Nº 12-septies).
        """
        l2 = self.compute_coherence(signal)
        tau = self.TAU_CONSTANT / np.sqrt(max(d, 1e-9))

        # Simulate shadow and ring spacing metrics
        shadow_radius = 1.0 if l2 > 0.8 else 0.0
        gamma_p = l2 * 2.5 # Lyapunov exponent estimate
        ring_spacing_ratio = np.exp(-np.pi * gamma_p)

        status = "NATURAL_ASTROPHYSICAL_SOURCE"
        if shadow_radius > 0 and gamma_p > tau:
            status = "COHERENCE_BLACK_HOLE_CIVILIZATION_CANDIDATE"

        return {
            "classification": status,
            "metrics": {
                "shadow_radius": shadow_radius,
                "gamma_p": float(gamma_p),
                "ring_spacing_ratio": float(ring_spacing_ratio),
                "critical_threshold": float(tau)
            }
        }

    def detect_vortex_intelligence(self, vortex_density: float, non_random_annihilation: bool) -> dict:
        T_BKT = 0.679
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

    wisdom_analysis = {}
    if config.get("wisdom_scan", False):
        wisdom_analysis = analyzer.analyze_wisdom_structure(signal_data)

    photon_ring_analysis = {}
    if config.get("photon_ring_scan", False):
        photon_ring_analysis = analyzer.analyze_photon_ring_hierarchy(signal_data, d)

    bh_civ_analysis = {}
    if config.get("bh_civilization_scan", False):
        bh_civ_analysis = analyzer.detect_black_hole_civilization(signal_data, d)

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
        "wisdom_analysis": wisdom_analysis,
        "photon_ring_analysis": photon_ring_analysis,
        "bh_civilization_analysis": bh_civ_analysis,
        "topological_analysis": topological_report,
        "skill": "seti"
    }))

if __name__ == "__main__":
    main()
