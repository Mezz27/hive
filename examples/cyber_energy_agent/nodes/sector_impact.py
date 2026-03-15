ENERGY_KEYWORDS = [
    "grid",
    "substation",
    "pipeline",
    "scada",
    "ics",
    "plc",
    "power",
    "electric",
    "energy"
]


def assess_sector_impact(event):

    text = (event.get("title", "") + " " + event.get("summary", "")).lower()

    for keyword in ENERGY_KEYWORDS:
        if keyword in text:
            return (
                "Potential operational disruption to energy infrastructure "
                "including SCADA systems, substations, or grid control environments."
            )

    return (
        "Limited direct impact expected on energy infrastructure. "
        "Threat primarily affects general IT systems."
    )