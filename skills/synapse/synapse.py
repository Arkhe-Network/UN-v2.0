import json
import sys

def calculate_coherence(data):
    """
    Calculates λ₂-Global based on regional representation and efficacy.
    Formula (simplified): λ₂ = average(regional_coherence) * (1 - decision_latency_penalty)
    """
    regions = data.get("regions", {})
    if not regions:
        return 0.0, "No regional data provided."

    total_coherence = 0.0
    count = 0

    report_lines = []
    report_lines.append("┌─────────────────────────────────────────────────────────────┐")
    report_lines.append("│           ARKHE GLOBAL COHERENCE — CSNU MONITOR             │")
    report_lines.append("├─────────────────────────────────────────────────────────────┤")

    for region, score in regions.items():
        total_coherence += score
        count += 1
        status = "🔴" if score < 0.4 else "🟡" if score < 0.8 else "🟢"
        bar = "█" * int(score * 10) + "░" * (10 - int(score * 10))
        report_lines.append(f"│  • {region.ljust(18)}: {score:.2f} {status} [{bar}]")

    lambda_global = total_coherence / count if count > 0 else 0.0

    # Apply latency penalty if present
    latency = data.get("decision_latency", 0.0) # 0.0 (low) to 1.0 (high)
    lambda_global = lambda_global * (1.0 - (latency * 0.5))

    status_global = "CRITICAL" if lambda_global < 0.6 else "STABLE" if lambda_global > 0.85 else "WARNING"
    color_global = "🔴" if lambda_global < 0.6 else "🟢" if lambda_global > 0.85 else "🟡"

    global_bar = "█" * int(lambda_global * 20) + "░" * (20 - int(lambda_global * 20))

    report_lines.insert(3, f"│  λ₂-Global:        {lambda_global:.2f} [{global_bar}] {int(lambda_global*100)}% {color_global} {status_global} │")
    report_lines.insert(4, "│                                                             │")
    report_lines.append("│                                                             │")
    report_lines.append(f"│  Veto Efficiency:    ${data.get('veto_cost', 'N/A')}B/coherent resolution       │")
    report_lines.append(f"│  Legitimacy Drift:   {data.get('legitimacy_drift', '0')}% (anual)                 │")
    report_lines.append("└─────────────────────────────────────────────────────────────┘")

    return lambda_global, "\n".join(report_lines)

def main():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Missing inputs: geopolitical_data and jurisdiction required."}))
        sys.exit(1)

    try:
        geopolitical_data = json.loads(sys.argv[1])
    except Exception as e:
        print(json.dumps({"error": f"Invalid JSON input: {str(e)}"}))
        sys.exit(1)

    jurisdiction = sys.argv[2]

    lambda_global, dashboard = calculate_coherence(geopolitical_data)

    print(json.dumps({
        "lambda_global": lambda_global,
        "dashboard": dashboard,
        "skill": "synapse",
        "jurisdiction": jurisdiction
    }))

if __name__ == "__main__":
    main()
