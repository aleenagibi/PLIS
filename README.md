# PLIS — Personal Learning Intelligence System

> An AI-powered study coach that tracks what you learn, tests whether you actually learned it, and recommends what to study next.

---

## Problem Statement

Most students have no honest way of knowing what they actually retain versus what they simply think they understand. Self-reported confidence is unreliable — you can feel certain about a topic and still fail to apply it when it matters.

PLIS solves this by introducing an honesty layer into the study process. You log a concept, rate your confidence, and the system immediately challenges that rating with a targeted quiz. Your actual score updates your confidence automatically. Over time, PLIS builds an accurate picture of your real skill map and uses it to recommend what you should focus on next — not what feels comfortable, but what the data says you actually need.

---

## How It Works

1. **Log** — Enter a concept you studied and rate your confidence from 1 to 5
2. **Get Tested** — The AI generates 3 targeted questions based on that concept
3. **Update** — Your real quiz score automatically adjusts your confidence rating
4. **Visualize** — Your skill radar chart updates to reflect your honest knowledge map
5. **Get Recommended** — The ML engine analyzes your gaps and tells you what to study next

---

## Features

- 📝 Concept logging with self-rated confidence scores
- 🧠 AI-generated quizzes that test real understanding, not just recall
- 📊 Skill radar chart showing honest knowledge across DS/ML domains
- 🔁 Automatic confidence correction based on quiz performance
- 🤖 ML-powered study recommendations based on gap analysis
- 📅 Study streak heatmap showing consistency over time
- 🔗 Shareable public profile URL to showcase learning progress

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React, Recharts |
| Backend | Python, FastAPI |
| Machine Learning | Scikit-learn |
| AI / Quiz Engine | LLM API (Anthropic Claude) |
| Version Control | Git, GitHub |
| Deployment | Hugging Face Spaces |

---

## Project Modules

| Module | Description | Status |
|---|---|---|
| Module 1 — Knowledge Tracker | Python CLI to log concepts and confidence to a local JSON file | 🔄 In Progress |
| Module 2 — Dashboard | React frontend + FastAPI backend with skill radar visualization | ⏳ Planned |
| Module 3 — ML Recommender | Scikit-learn model that recommends what to study next | ⏳ Planned |
| Module 4 — AI Quiz Engine | LLM-generated quizzes with automatic confidence correction | ⏳ Planned |

---

## Project Status

🚧 **Actively being built** — Started March 2026

This project is being developed over 5 months as a hands-on approach to apply Python, Machine Learning, and AI integration through real, self-driven building.

Follow the commit history to see the full learning journey.

---

## Author

**Aleena Gibi**
[GitHub](https://github.com/aleenagibi) • [LinkedIn](https://www.linkedin.com/in/aleenagibi2005)

---

*Built to learn. Built to be honest about learning.*
