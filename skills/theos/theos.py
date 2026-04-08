import numpy as np
import json
import sys

class TheologicalCoherenceMeter:
    """
    Instrumento de mapeamento da 'dança da alma' no espaço de fase teológico.
    Não emite julgamentos de verdade objetiva; apenas mede coerência de adesão subjetiva.
    """

    def __init__(self):
        # Em um sistema real, estes vetores seriam carregados de um modelo pré-treinado (Hwang/GospelVec)
        # Aqui usamos vetores sintéticos ortogonais para demonstração
        self.attractors = {
            'matthew': np.array([1, 0, 0, 0, 0]),
            'mark':    np.array([0, 1, 0, 0, 0]),
            'luke':    np.array([0, 0, 1, 0, 0]),
            'john':    np.array([0, 0, 0, 1, 0]),
            'logos':   np.array([0.5, 0.5, 0.5, 0.5, 1.0])  # Atrator de coerência máxima
        }

    def measure_devotion(self, neural_state: np.ndarray) -> dict:
        """
        Calcula a similaridade de cosseno entre o estado neural e cada atrator.
        """
        results = {}
        neural_norm = np.linalg.norm(neural_state) + 1e-9

        for name, attractor in self.attractors.items():
            attr_norm = np.linalg.norm(attractor) + 1e-9
            alignment = np.dot(neural_state, attractor) / (neural_norm * attr_norm)

            results[name] = {
                'lambda2_alignment': float(alignment),
                'proximity': self._get_proximity_label(alignment)
            }

        # Análise de Perfil
        results['profile'] = self._analyze_profile(results)
        return results

    def _get_proximity_label(self, alignment):
        if alignment > 0.8: return 'unitive'
        if alignment > 0.5: return 'devotional'
        if alignment > 0.2: return 'exploratory'
        return 'distant'

    def _analyze_profile(self, results):
        alignments = [v['lambda2_alignment'] for k, v in results.items() if k != 'profile']
        max_align = max(alignments)

        if results['logos']['lambda2_alignment'] > 0.8:
            return "MISTICISMO_UNIFICADO"
        if max_align > 0.9:
            return "FUNDAMENTALISMO_GEOMETRICO"
        if np.std(alignments) < 0.1:
            return "SINCRETISMO_ESTRUTURAL"

        return "SABEDORIA_INTEGRADA"

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Missing neural state input."}))
        sys.exit(1)

    try:
        neural_state = np.array(json.loads(sys.argv[1]))
        # Se o vetor for menor que 5D, preenchemos com zeros para o exemplo
        if len(neural_state) < 5:
            neural_state = np.pad(neural_state, (0, 5 - len(neural_state)))
        elif len(neural_state) > 5:
            neural_state = neural_state[:5]

        meter = TheologicalCoherenceMeter()
        report = meter.measure_devotion(neural_state)

        print(json.dumps({
            "theological_report": report,
            "skill": "theos",
            "status": "SUCCESS"
        }))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
