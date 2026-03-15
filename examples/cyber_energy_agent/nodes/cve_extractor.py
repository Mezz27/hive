import re

CVE_PATTERN = r"CVE-\d{4}-\d{4,7}"

def extract_cve(text):

    matches = re.findall(CVE_PATTERN, text, re.IGNORECASE)

    if matches:
        return matches[0].upper()

    return None