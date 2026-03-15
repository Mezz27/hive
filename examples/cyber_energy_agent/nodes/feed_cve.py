import requests

def collect_cve_feed():

    events = []

    try:

        url = "https://security.access.redhat.com/data/csaf/v2/advisories/2026/rhsa-2026_4174.json"
        r = requests.get(url, timeout=10)

        data = r.json()

        vulns = data.get("vulnerabilities", [])

        for v in vulns:

            cve_id = v.get("cve", "Unknown CVE")
            title = v.get("title", "")

            notes = v.get("notes", [])
            description = ""

            for n in notes:
                if n.get("category") == "description":
                    description = n.get("text")
                    break

            events.append({
                "title": f"{cve_id} - {title}",
                "summary": description,
                "source": "CVE Feed"
            })

    except Exception as e:
        print("CVE feed failed:", e)

    return events