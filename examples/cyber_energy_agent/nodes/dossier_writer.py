def generate_dossier(event):

    report = f"""
CYBER ENERGY THREAT DOSSIER
===========================

CVE: {event.get("cve", "Unknown")}

Title:
{event.get("title", "Unknown")}

Source:
{event.get("source", "Unknown")}

Severity Score:
{event.get("severity", "Unknown")}/5

Confidence:
{event.get("confidence", "Unknown")}

Exploit Available:
{event.get("exploit", False)}

ICS Relevance:
{event.get("ics", False)}

Threat Assessment:
{event.get("analysis", "Unknown")}

Potential Energy Sector Impact:
{event.get("impact", "Unknown")}
"""

    # MITRE ATT&CK techniques
    mitre = event.get("mitre", [])

    report += "\nMITRE ATT&CK Techniques:\n"

    if mitre:
        for technique in mitre:
            report += f"- {technique}\n"
    else:
        report += "- No direct MITRE technique identified\n"
    
    # Campaign intelligence
    campaigns = event.get("campaigns", [])

    if campaigns:
        report += "\nCampaign Indicators:\n"
        for c in campaigns:
            report += f"- {c}\n"

    report += "\n-------------------------------\n"

    return report