# Cyber Energy Threat Intelligence Agent

An autonomous Hive agent that collects cyber threat events from vulnerability, exploited-vulnerability, and energy-sector news feeds, scores their relevance to energy infrastructure, detects recurring campaign patterns, and generates a threat dossier.

## Data Sources

- CVE vulnerability feeds
- CISA Known Exploited Vulnerabilities
- Energy sector cybersecurity news

## Configuration

The agent optionally supports LLM-based classification using OpenRouter.

Set your API key:

export OPENROUTER_API_KEY=your_api_key_here

If no API key is provided, the agent automatically falls back to keyword-based classification.

## Capabilities

- Threat classification (energy-relevant detection)
- Cyber impact analysis with severity scoring
- ICS / SCADA relevance detection
- Exploit intelligence checks
- Risk scoring
- Campaign detection using threat memory
- MITRE ATT&CK mapping
- Human-readable threat dossier generation

## Example Use Cases

- SOC monitoring for energy utilities
- Critical infrastructure threat intelligence
- Automated vulnerability risk analysis

## Features

- CVE and exploited vulnerability collection
- Energy-sector relevance classification
- ICS relevance detection
- Exploit intelligence checks
- Risk scoring
- MITRE ATT&CK mapping
- Threat memory and campaign detection
- Human-readable dossier generation

## Run

//bash
export OPENAI_API_KEY="your_api_key_here"
PYTHONPATH=examples uv run python -m cyber_energy_agent

## Example Output

CYBER ENERGY THREAT DOSSIER
===========================

CVE: CVE-2025-61726

Title:
CVE-2025-61726 - golang: net/url: Memory exhaustion in query parameter parsing in net/url

Source:
CVE Feed

Severity Score:
3/5

Confidence:
High

Exploit Available:
False

ICS Relevance:
False

Threat Assessment:
This vulnerability allows for denial-of-service attacks against Go applications processing HTTP requests, potentially impacting energy infrastructure components utilizing such applications for data acquisition, control, or communication.

Potential Energy Sector Impact:
Limited direct impact expected on energy infrastructure. Threat primarily affects general IT systems.

MITRE ATT&CK Techniques:
- T0866 – Exploitation of Remote Services

-------------------------------
