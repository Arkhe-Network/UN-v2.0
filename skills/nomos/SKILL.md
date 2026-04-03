name: nomos
version: 1.0.0
description: "Verifica conformidade de políticas ODRL com LGPD/GDPR e gera evidência digital."
inputs:
  - name: policy_json
    type: string
    description: "The ODRL policy document in JSON-LD format."
  - name: jurisdiction
    type: string
    description: "The jurisdiction code (e.g., BR, EU)."
outputs:
  - name: is_compliant
    type: boolean
    description: "Whether the policy is compliant with local data privacy laws."
  - name: report
    type: string
    description: "Detailed compliance report."
capabilities:
  - odrl_validation
  - lgpd_compliance
  - gdpr_compliance
  - digital_evidence
