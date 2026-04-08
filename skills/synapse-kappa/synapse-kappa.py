import json
import sys

class GeopoliticalGameSimulator:
    def __init__(self):
        self.actors = {
            'P5_Russia': {'veto_power': 1.0, 'phase': 0.2, 'goal': 'preserve_status_quo'},
            'P5_China': {'veto_power': 1.0, 'phase': 0.3, 'goal': 'preserve_status_quo'},
            'P5_USA': {'veto_power': 1.0, 'phase': 0.7, 'goal': 'expand_with_conditions'},
            'P5_UK': {'veto_power': 1.0, 'phase': 0.8, 'goal': 'expand'},
            'P5_France': {'veto_power': 1.0, 'phase': 0.9, 'goal': 'expand'},
            'G4_Brazil': {'veto_power': 0.0, 'phase': 0.85, 'goal': 'expand_with_veto'},
            'G4_Germany': {'veto_power': 0.0, 'phase': 0.88, 'goal': 'expand_with_veto'},
            'G4_India': {'veto_power': 0.0, 'phase': 0.82, 'goal': 'expand_with_veto'},
            'G4_Japan': {'veto_power': 0.0, 'phase': 0.86, 'goal': 'expand_with_veto'},
            'African_Union': {'veto_power': 0.0, 'phase': 0.35, 'goal': 'expand_with_veto'},
            'Uniting_for_Consensus': {'veto_power': 0.0, 'phase': 0.45, 'goal': 'expand_non_permanent'}
        }
        self.lambda2_global = 0.59
        self.veto_count = 0
        self.legitimacy = 0.62
        self.status = "INITIALIZED"

    def simulate_veto(self, actor_id):
        if actor_id not in self.actors or self.actors[actor_id]['veto_power'] < 1.0:
            return False, "Actor does not have veto power."

        self.lambda2_global -= 0.04
        self.veto_count += 1
        self.legitimacy -= 0.04
        self.status = f"VETO_BY_{actor_id}"

        return True, f"Veto by {actor_id} recorded. Lambda2 dropped to {self.lambda2_global:.2f}."

    def run_uniting_for_peace(self):
        if self.lambda2_global < 0.60:
            self.lambda2_global += 0.17
            self.legitimacy += 0.16
            self.status = "UNITING_FOR_PEACE_ACTIVATED"
            return True, "Circuit Breaker (Uniting for Peace) activated. Lambda2 recovered to 0.72."
        return False, "Lambda2 above threshold; Uniting for Peace not required."

    def apply_phase_lock(self):
        self.lambda2_global = 0.88
        self.legitimacy = 0.89
        self.veto_count = 5 # Reduced after reform
        self.status = "PHASE_LOCK_CONDITIONAL_IMPLEMENTED"
        return True, "Phase-Lock implemented. Coherence restored to 0.88."

    def validate_data_contract(self, contract_json, crisis_metadata=None):
        """
        Implements refactored Article 27 logic.
        """
        try:
            contract = json.loads(contract_json)
        except Exception:
            return False, "Invalid contract JSON."

        if crisis_metadata and crisis_metadata.get("type") == "ATROCITY_CRIMES":
            self.status = "VETO_BYPASSED_HUMANITARIAN"
            return True, "Veto power DISABLED due to ATROCITY_CRIMES (λ₂-humanitarian < 0.90)."

        # Check for GA override trigger
        if self.veto_count > 3:
            self.status = "GA_OVERRIDE_TRIGGERED"
            return True, "TRIGGER_GENERAL_ASSEMBLY_OVERRIDE activated (Veto count > 3)."

        return False, "No automated trigger activated."

def main():
    if len(sys.argv) < 3:
        # Default behavior for discovery/initialization
        sim = GeopoliticalGameSimulator()
        print(json.dumps({
            "lambda2_global": sim.lambda2_global,
            "status": sim.status,
            "report": "Simulator initialized.",
            "skill": "synapse-kappa"
        }))
        return

    action = sys.argv[1]
    actor = sys.argv[2]
    metadata_raw = sys.argv[3] if len(sys.argv) > 3 else "{}"

    try:
        metadata = json.loads(metadata_raw)
    except:
        metadata = {}

    sim = GeopoliticalGameSimulator()
    report = ""

    if action == "P5_VETO":
        success, msg = sim.simulate_veto(actor)
        report += msg
        if sim.lambda2_global < 0.60:
            s2, m2 = sim.run_uniting_for_peace()
            report += " " + m2

    elif action == "VALIDATE_CONTRACT":
        # Simulate contract validation (refactored Art 27)
        contract = {
            "contract_id": "UNSC_VOTE_V3",
            "logic_mode": "CONDITIONAL_CONSENSUS"
        }
        success, msg = sim.validate_data_contract(json.dumps(contract), metadata)
        report = msg

    elif action == "REFORM_PHASE_LOCK":
        success, msg = sim.apply_phase_lock()
        report = msg

    print(json.dumps({
        "lambda2_global": sim.lambda2_global,
        "status": sim.status,
        "report": report,
        "skill": "synapse-kappa"
    }))

if __name__ == "__main__":
    main()
