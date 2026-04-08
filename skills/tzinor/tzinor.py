import json
import sys
import hashlib

def main():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Missing inputs."}))
        sys.exit(1)

    target = sys.argv[1]
    oracle_alert = sys.argv[2]

    # Protocolo de Silêncio (Art. 10)
    if oracle_alert == "CRITICAL":
        status = "HALTED"
        reason = "Protocolo de Silêncio ativado: Detectados padrões hostis na CMB."
    else:
        status = "TRANSMITTING"
        reason = f"Handshake autorizado para {target}."

    # Trança da Terra (π sequence)
    earth_braid = "σ3 σ2_inv σ2 σ1_inv σ1 σ3_inv"
    payload_hash = hashlib.sha256(earth_braid.encode()).hexdigest()

    print(json.dumps({
        "target": target,
        "transmission_status": status,
        "payload_hash": payload_hash,
        "reason": reason,
        "skill": "tzinor"
    }))

if __name__ == "__main__":
    main()
