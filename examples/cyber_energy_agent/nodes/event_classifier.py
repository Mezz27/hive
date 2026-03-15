import os

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


CYBER_KEYWORDS = [
    "cve", "vulnerability", "exploit", "rce",
    "ics", "scada", "plc", "pipeline",
    "grid", "substation", "energy"
]


def get_llm_client():
    """
    Safely initialize OpenRouter client only if API key exists.
    """
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not OPENAI_AVAILABLE or not api_key:
        return None

    try:
        return OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )
    except Exception:
        return None


def classify_event(event):

    client = get_llm_client()

    if client:

        prompt = f"""
You are a cyber threat analyst.

Determine if this event could impact energy infrastructure.

Respond ONLY with:
YES
or
NO

Event:
Title: {event['title']}
Summary: {event['summary']}
"""

        try:

            response = client.chat.completions.create(
                model="openrouter/free",
                messages=[{"role": "user", "content": prompt}]
            )

            answer = response.choices[0].message.content.strip().upper()

            return answer.startswith("YES")

        except Exception as e:
            print("LLM classification failed, using keyword fallback:", e)

    # Keyword fallback
    text = (event.get("title", "") + " " + event.get("summary", "")).lower()

    for keyword in CYBER_KEYWORDS:
        if keyword in text:
            return True

    return False