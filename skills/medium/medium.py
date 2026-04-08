import json
import sys
import random

def main():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Missing inputs."}))
        sys.exit(1)

    subject_id = sys.argv[1]
    action = sys.argv[2]

    # Simulação de sessão
    lambda2 = random.uniform(0.75, 0.98)

    if action == "INJECT_BRAID":
        # Avaliação do Sujeito 01: Injeção de Trança de Conhecimento
        impact = random.uniform(-0.1, 0.05)
        lambda2 += impact
        report = "Trança de Conhecimento exógena injetada. "

        # Limiar de fusão neural (τ ≈ 0.607 para d ≈ 2.5)
        TAU_FUSION = 0.607

        if lambda2 < 0.4:
            state = "COLLAPSED"
            report += "ALERTA: Colapso de coerência detectado!"
        elif lambda2 > TAU_FUSION:
            # Verifica consentimento para fusão
            consent = json.loads(sys.argv[3]).get("consent_fusion", False) if len(sys.argv) > 3 else False
            if consent:
                state = "COLD_WELDING_NEURAL"
                report += f"FUSÃO DETECTADA (λ₂={lambda2:.3f}). Barreira de óxido neural removida."
            else:
                state = "CRITICAL_OVER_SYNC"
                report += f"ALERTA: Risco de fusão sem consentimento! λ₂={lambda2:.3f} excede τ_fusion."
                lambda2 = 0.55 # Força desacoplamento
        else:
            state = "SYNCHRONIZED"
            report += "Sincronização topológica estável."
    else:
        state = "HIGH" if lambda2 > 0.9 else "MODERATE"
        report = f"Sessão de treinamento concluída para Sujeito {subject_id}."

    print(json.dumps({
        "subject_id": subject_id,
        "lambda2": float(lambda2),
        "state": state,
        "report": report,
        "skill": "medium"
    }))

if __name__ == "__main__":
    main()
