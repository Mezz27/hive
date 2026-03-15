ICS_KEYWORDS = [
    "scada",
    "plc",
    "industrial control",
    "rockwell",
    "siemens",
    "schneider",
    "energy",
    "grid",
    "substation",
    "pipeline",
]


def detect_ics_relevance(event):

    text = (event["title"] + " " + event["summary"]).lower()

    for word in ICS_KEYWORDS:
        if word in text:
            return True

    return False