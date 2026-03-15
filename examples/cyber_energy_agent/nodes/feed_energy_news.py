import feedparser

def collect_energy_news():

    events = []

    try:

        feed = feedparser.parse(
            "https://news.google.com/rss/search?q=energy+cyberattack+pipeline+power+grid"
        )

        for entry in feed.entries[:10]:

            events.append({
                "title": entry.title,
                "summary": entry.summary,
                "source": "Energy News"
            })

    except Exception as e:
        print("Energy news feed failed:", e)

    return events