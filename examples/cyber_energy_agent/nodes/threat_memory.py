from collections import defaultdict
from datetime import datetime, timedelta

REPORTED_CAMPAIGNS = set()

THREAT_HISTORY = []

WINDOW_HOURS = 24


def store_event(event):

    event["timestamp"] = datetime.utcnow()
    THREAT_HISTORY.append(event)

    cleanup_old_events()


def cleanup_old_events():

    cutoff = datetime.utcnow() - timedelta(hours=WINDOW_HOURS)

    global THREAT_HISTORY
    THREAT_HISTORY = [e for e in THREAT_HISTORY if e["timestamp"] > cutoff]


def detect_campaign():

    vendor_counts = defaultdict(int)

    for event in THREAT_HISTORY:

        text = (event.get("title", "") + " " + event.get("summary", "")).lower()

        if "siemens" in text:
            vendor_counts["siemens"] += 1

        if "rockwell" in text:
            vendor_counts["rockwell"] += 1

        if "schneider" in text:
            vendor_counts["schneider"] += 1

        if "ics" in text or "scada" in text or "plc" in text:
            vendor_counts["ics"] += 1

    campaigns = []

    for vendor, count in vendor_counts.items():

        if count >= 3:

            message = f"Potential coordinated activity targeting {vendor} infrastructure ({count} events in last {WINDOW_HOURS}h)"

            # prevent duplicate alerts
            if message not in REPORTED_CAMPAIGNS:
                campaigns.append(message)
                REPORTED_CAMPAIGNS.add(message)

    return campaigns