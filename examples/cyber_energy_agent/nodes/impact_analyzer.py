import os

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

if OPENAI_AVAILABLE:
    client = OpenAI(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )


def estimate_cyber_impact(event_text):

    if OPENAI_AVAILABLE:

        prompt = f"""
You are a cyber-energy intelligence analyst.

Evaluate the potential impact of this event on energy infrastructure
(power grids, pipelines, utilities, refineries).

Return ONLY in this format:

Assessment: <one sentence explanation>
Score: <number 1-5>

Event:
{event_text}
"""

        try:

            res = client.chat.completions.create(
                model="openrouter/free",
                messages=[{"role": "user", "content": prompt}]
            )

            response_text = res.choices[0].message.content.strip()

            assessment = "Impact unclear"
            score = 3

            for line in response_text.splitlines():

                line = line.strip()

                if line.lower().startswith("assessment:"):
                    assessment = line.split(":", 1)[1].strip()

                elif line.lower().startswith("score:"):
                    try:
                        score = int(line.split(":", 1)[1].strip()[0])
                    except:
                        score = 3

            return assessment, score

        except Exception as e:
            print("LLM impact analysis failed, using fallback:", e)

    # fallback logic
    txt = event_text.lower()

    if "plc" in txt or "scada" in txt:
        return "Potential disruption to industrial control systems managing energy infrastructure", 5

    if "solarwinds" in txt:
        return "Supply-chain compromise could disrupt utility monitoring systems", 4

    if "rce" in txt or "remote code execution" in txt:
        return "Remote code execution could allow attackers to disrupt energy operations", 5

    if "grid" in txt or "pipeline" in txt:
        return "Possible operational disruption to energy infrastructure", 4

    return "Impact unclear", 3