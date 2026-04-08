import subprocess
import json
import unittest

class TestSynapseKappa(unittest.TestCase):
    def run_skill(self, action, actor, metadata=None):
        cmd = ["python3", "skills/synapse-kappa/synapse-kappa.py", action, actor]
        if metadata:
            cmd.append(json.dumps(metadata))
        result = subprocess.run(cmd, capture_output=True, text=True)
        return json.loads(result.stdout)

    def test_p5_veto_and_recovery(self):
        # Initial Veto
        output = self.run_skill("P5_VETO", "P5_Russia")
        self.assertEqual(output["status"], "UNITING_FOR_PEACE_ACTIVATED")
        self.assertIn("Circuit Breaker (Uniting for Peace) activated", output["report"])
        self.assertAlmostEqual(output["lambda2_global"], 0.72)

    def test_atrocity_crimes_bypass(self):
        # Validation with Atrocity Crimes
        metadata = {"type": "ATROCITY_CRIMES"}
        output = self.run_skill("VALIDATE_CONTRACT", "P5_Russia", metadata)
        self.assertEqual(output["status"], "VETO_BYPASSED_HUMANITARIAN")
        self.assertIn("Veto power DISABLED", output["report"])

    def test_phase_lock(self):
        # Reform Phase-Lock
        output = self.run_skill("REFORM_PHASE_LOCK", "ANY")
        self.assertEqual(output["status"], "PHASE_LOCK_CONDITIONAL_IMPLEMENTED")
        self.assertAlmostEqual(output["lambda2_global"], 0.88)

if __name__ == "__main__":
    unittest.main()
