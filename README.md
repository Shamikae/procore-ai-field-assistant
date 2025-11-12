---
sdk: streamlit
colorFrom: blue
colorTo: purple
---


![CI](https://github.com/Shamikae/procore-ai-field-assistant/actions/workflows/ci.yml/badge.svg)
![Deploy – HF Space](https://github.com/Shamikae/procore-ai-field-assistant/actions/workflows/deploy-hf-space.yml/badge.svg)
![Docker – GHCR](https://github.com/Shamikae/procore-ai-field-assistant/actions/workflows/docker-ghcr.yml/badge.svg)

# Procore AI Field Assistant (Mock Case Study)

**Author:** Shamika Earle  
**Role Fit:** Construction Technology Specialist — Haugland Group  
**Focus Pain Point:** Users don’t know how to use digital tools (Procore) effectively.

This mock repo demonstrates how an AI assistant can guide field teams through Procore workflows using **natural language**,
**smart templates**, and **adaptive SOPs** — without requiring live API keys or paid services.

---

## 🎯 Goals
- Turn complex Procore tasks into simple, guided, step-by-step flows.
- Auto-generate **Action Plans, Daily Logs, Inspections, and RFIs** from voice/text.
- Standardize data capture to improve **compliance, quality, and reporting speed**.
- Provide field-friendly **micro-SOPs** and **one-pagers** that reinforce adoption.

---

## 🧩 What’s Inside
- `app/app.py` — A **local Streamlit stub** that simulates the assistant with canned logic. No API costs.
- `data/` — Example **Procore-ready JSON** outputs for Inspections, Daily Logs, and RFIs.
- `prompts/` — Example user prompts and assistant responses (copy/paste during interviews).
- `sops/` — Micro-guides: *How to Run an Inspection*, *Daily Log in 3 Steps*, *RFI Flow*.
- `assets/diagram.png` — Simple flow diagram of the user experience.
- `scripts/loom_script.txt` — A 60–90s demo script for a quick walkthrough video.
- `metrics/metrics_plan.md` — Adoption and impact metrics worth tracking in a pilot.

---

## 🚀 How to Run the Local Demo (No APIs)
Requirements: Python 3.10+

```bash
cd app
pip install -r requirements.txt
streamlit run app.py
```
Then open the URL Streamlit prints (usually http://localhost:8501).

> This demo uses **canned responses** from `/data` to simulate the assistant.
> Swap the JSON templates or extend the logic to fit your project types.

---

## 🧠 Example User Flow
1. Field user says: “Create a safety inspection for **Main Street Bridge**. 12 workers, no incidents, attach 3 photos.”
2. Assistant: “Let’s do it — confirm project, labor count, incidents, and attachments.”
3. Output: Structured **inspection JSON** ready to push to Procore (simulated).

See `data/inspection_example.json` for a concrete output.

---

## 📈 Pilot Metrics (What We’ll Measure)
- **Onboarding time** for new users (target: -50%)
- **Template adoption rate** (target: +30%)
- **Manual entry errors** (target: -25%)
- **Submission cycle time** for inspections/logs (target: -30%)

More detail in `metrics/metrics_plan.md`.

---

## 🔒 Notes
- This is a **mock**, designed for interviews and portfolio review. No proprietary data.
- When ready, replace stubs with live integrations (Procore API, Power BI, AWS Lambda).

# Enhancements Aligned to Haugland Job Post
- **Field Mode**: minimal inputs for onsite use.
- **Template Builder**: standardize Action Plans & Inspections; reusable JSON.
- **Adoption Dashboard**: pilot KPIs (usage, time saved, SOP views, sentiment).
- **Playbook**: special missions, adoption tactics, AI enablement.
- **Future Integrations**: BIM/Drone CV, Fleet PM analytics, Finance variance in Power BI, Safety incident modeling.

## Docker
docker run -p 8501:8501 ghcr.io/shamikae/procore-ai-field-assistant/procore-ai-field-assistant:latest 

