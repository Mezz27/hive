import requests

def collect_cisa_exploited():

    events = []

    try:

        url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
        r = requests.get(url, timeout=10)

        data = r.json()

        for vuln in data["vulnerabilities"][:10]:

            cve = vuln["cveID"]
            vendor = vuln["vendorProject"]
            product = vuln["product"]
            summary = vuln["shortDescription"]

            events.append({
                "title": f"{cve} - {vendor} {product}",
                "summary": summary,
                "source": "CISA KEV"
            })

    except Exception as e:
        print("CISA feed failed:", e)

    return events