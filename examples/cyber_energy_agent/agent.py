import time

from .nodes.feed_cve import collect_cve_feed
from .nodes.feed_cisa_kev import collect_cisa_exploited
from .nodes.feed_energy_news import collect_energy_news
from .nodes.cve_extractor import extract_cve
from .nodes.event_classifier import classify_event
from .nodes.impact_analyzer import estimate_cyber_impact
from .nodes.risk_engine import calculate_risk
from .nodes.exploit_intel import check_exploit
from .nodes.ics_relevance import detect_ics_relevance
from .nodes.threat_memory import store_event, detect_campaign
from .nodes.dossier_writer import generate_dossier
from .nodes.sector_impact import assess_sector_impact
from .nodes.mitre_mapper import map_mitre_techniques
from .config import DEFAULT_POLL_INTERVAL_SECONDS


PROCESSED_EVENTS = set()


def collect_all_events():
    events = []

    try:
        events += collect_cve_feed()
    except Exception as e:
        print("CVE feed error:", e)

    try:
        events += collect_cisa_exploited()
    except Exception as e:
        print("CISA KEV feed error:", e)

    try:
        events += collect_energy_news()
    except Exception as e:
        print("Energy news feed error:", e)

    return events


def run_real_time(interval_seconds=DEFAULT_POLL_INTERVAL_SECONDS):
    print("Cyber-Energy Threat Intelligence Agent Running...\n")

    while True:
        events = collect_all_events()

        for event in events:

            # --- Extract CVE if not present ---
            text = event.get("title", "") + " " + event.get("summary", "")

            if not event.get("cve"):
                extracted = extract_cve(text)
                if extracted:
                    event["cve"] = extracted

            event_id = event.get("cve") or event.get("title")

            if not event_id or event_id in PROCESSED_EVENTS:
                continue

            PROCESSED_EVENTS.add(event_id)

            # Step 1: classify relevance
            energy_relevant = classify_event(event)
            if not energy_relevant:
                continue

            event["energy_relevant"] = energy_relevant

            # Step 2: cyber impact analysis
            analysis, severity = estimate_cyber_impact(
                event.get("title", "") + " " + event.get("summary", "")
            )

            event["analysis"] = analysis
            event["impact"] = assess_sector_impact(event)
            event["severity"] = severity

            # Confidence scoring
            event["confidence"] = "High" if event.get("cve") else "Medium"

            # Step 3: exploit intelligence
            exploit_prob = False

            if "cve" in event:
                exploit_prob = check_exploit(event["cve"])

            event["exploit"] = exploit_prob

            # Step 4: ICS infrastructure relevance
            ics_relevance = detect_ics_relevance(event)
            event["ics"] = ics_relevance

            # Step 5: MITRE ATT&CK mapping
            techniques = map_mitre_techniques(event)
            event["mitre"] = techniques

            # Step 6: risk calculation
            risk, energy_score, exploit_score = calculate_risk(event, severity)

            event["risk"] = risk
            event["energy_score"] = energy_score
            event["exploit_score"] = exploit_score

            store_event(event)

            # Step 7: campaign detection
            campaigns = detect_campaign()
            event["campaigns"] = campaigns if campaigns else []

            # Step 8: generate threat dossier
            dossier = generate_dossier(event)

            print(dossier)

        print(f"\nSleeping for {interval_seconds} seconds...\n")
        time.sleep(interval_seconds)


if __name__ == "__main__":
    try:
        run_real_time(DEFAULT_POLL_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nAgent stopped by user.")