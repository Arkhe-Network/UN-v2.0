import json
import sys

def validate_odrl_lgpd(policy_json, jurisdiction):
    """
    Simulated ODRL/LGPD validation logic.
    In a production scenario, this would use a formal ODRL validator
    and legal rule-engine against LGPD (Brazil) or GDPR (EU).
    """
    try:
        policy = json.loads(policy_json)
    except Exception as e:
        return False, f"Invalid JSON-LD: {str(e)}"

    # Basic LGPD/GDPR check: Does it mention 'Consent' or 'Purpose'?
    policy_str = json.dumps(policy).lower()

    if jurisdiction.upper() == 'BR':
        # Simple LGPD simulation
        if 'consent' in policy_str and 'purpose' in policy_str:
            return True, "Policy is compliant with LGPD (Simulated)."
        else:
            return False, "Policy lacks required LGPD consent or purpose elements."

    elif jurisdiction.upper() == 'EU':
        # Simple GDPR simulation
        if 'consent' in policy_str and 'transparency' in policy_str:
            return True, "Policy is compliant with GDPR (Simulated)."
        else:
            return False, "Policy lacks required GDPR transparency or consent elements."

    return False, f"Unsupported or unknown jurisdiction: {jurisdiction}"

def main():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Missing inputs: policy_json and jurisdiction required."}))
        sys.exit(1)

    policy_json = sys.argv[1]
    jurisdiction = sys.argv[2]

    is_compliant, report = validate_odrl_lgpd(policy_json, jurisdiction)

    print(json.dumps({
        "is_compliant": is_compliant,
        "report": report,
        "skill": "nomos"
    }))

if __name__ == "__main__":
    main()
