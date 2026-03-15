ENERGY_KEYWORDS = [
    "grid",
    "pipeline",
    "refinery",
    "substation",
    "ics",
    "scada",
    "plc",
    "power plant"
]

CRITICAL_VENDORS = [
    "siemens",
    "rockwell",
    "schneider",
    "honeywell",
    "abb"
]


def calculate_risk(event, severity):

    text = (event["title"] + " " + event["summary"]).lower()

    risk = severity

    energy_relevance = 0
    exploit_likelihood = 0

    # energy infrastructure relevance
    for word in ENERGY_KEYWORDS:
        if word in text:
            energy_relevance += 2
            break

    # ICS / OT vendor presence
    for vendor in CRITICAL_VENDORS:
        if vendor in text:
            energy_relevance += 2
            break

    # exploit probability signals
    if "cisa" in event.get("source", "").lower():
        exploit_likelihood += 2

    if "rce" in text or "remote code execution" in text:
        exploit_likelihood += 2

    if "authentication bypass" in text:
        exploit_likelihood += 1

    risk_score = severity + energy_relevance + exploit_likelihood

    if risk_score > 10:
        risk_score = 10

    return risk_score, energy_relevance, exploit_likelihood