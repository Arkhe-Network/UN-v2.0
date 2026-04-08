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

    def test_phase_coach_normal(self):
        # Neural Phase Coach - Normal
        metadata = {"neural_field": [0.1, 0.2, 0.8]}
        output = self.run_skill("PHASE_COACH", "ANY", metadata)
        self.assertEqual(output["status"], "PHASE_COACH_ACTIVE")
        self.assertIn("vortex_2", output["coach_report"])
        self.assertEqual(output["coach_report"]["vortex_2"]["emotional_signature"], "POSITIVE")

    def test_phase_coach_warning(self):
        # Neural Phase Coach - Trauma Warning (simulated by a field value that maps to a trauma sink)
        # Note: In the current implementation, all > 0.5 are POSITIVE.
        # I'll adjust the implementation or the test to ensure we can trigger NEGATIVE/TRAUMA.
        # Actually, let's look at the code: valence = "POSITIVE" if val > 0.5 else "NEGATIVE"
        # and project_attractor_to_phenomenology returns "TRAUMA_LOOP_SINK" if valence is "NEGATIVE".
        # So values between threshold (0.263) and 0.5 should be NEGATIVE.
        metadata = {"neural_field": [0.4]}
        output = self.run_skill("PHASE_COACH", "ANY", metadata)
        self.assertEqual(output["status"], "PHASE_COACH_WARNING")
        self.assertIn("ATENÇÃO: Você está estabilizando um vórtice de trauma", output["report"])
        self.assertEqual(output["coach_report"]["vortex_0"]["emotional_signature"], "NEGATIVE")

if __name__ == "__main__":
    unittest.main()
