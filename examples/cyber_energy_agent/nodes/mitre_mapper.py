MITRE_TECHNIQUES = {
    "rce": ("T0866", "Exploitation of Remote Services"),
    "remote code execution": ("T0866", "Exploitation of Remote Services"),
    "exploit": ("T0866", "Exploitation of Remote Services"),
    "dos": ("T0814", "Denial of Service"),
    "denial": ("T0814", "Denial of Service"),
    "tls": ("T0859", "Valid Accounts"),
    "authentication": ("T0859", "Valid Accounts"),
    "credential": ("T0859", "Valid Accounts"),
    "scada": ("T0886", "Manipulation of Control"),
    "plc": ("T0886", "Manipulation of Control"),
    "ics": ("T0886", "Manipulation of Control"),
}

def map_mitre_techniques(event):

    text = (event.get("title", "") + " " + event.get("summary", "")).lower()

    techniques = []

    for keyword, (tech_id, tech_name) in MITRE_TECHNIQUES.items():

        if keyword in text:
            techniques.append(f"{tech_id} – {tech_name}")

    return list(set(techniques))