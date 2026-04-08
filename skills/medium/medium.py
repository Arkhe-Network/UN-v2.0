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
        if lambda2 < 0.7:
            state = "COLLAPSED"
            report += "ALERTA: Colapso de coerência detectado!"
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
