# 🧑‍🚀 Nuke Agent Lab

An experimental **AI‑powered refactoring agent** with a Flask dashboard, Gemini integration, and unified diff output.  
It lets you select a file, choose a “nuke” (refactor strategy), and preview both the AI’s refactor and a unified diff against the original code.  
The project is evolving toward **live AI agents** that can run continuously, expose APIs, and integrate into developer workflows.

---

## ✨ Features
- **File + Nuke selection**: Choose a target file (defaults to `utils.py`) and a refactor strategy.
- **Gemini integration**: Uses Google’s Gemini model to generate refactored code.
- **Diff view**: Unified diff with green/red highlights for additions and deletions.
- **Web dashboard**: Simple Flask UI for triggering and reviewing nukes.
- **Extensible nukes**: Strategies defined in `tools/nuke_agent.py` can be expanded.
- **Planned live agents**: Continuous monitoring, API endpoints, and CI/CD integration.

---

## 🚀 Quickstart

### Prerequisites
- Python 3.10+
- A valid Google Gemini API key

### Setup
```bash
git clone https://github.com/your-org/nuke-agent-lab.git
cd nuke-agent-lab
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file at the repo root:
```
GOOGLE_API_KEY=your_api_key_here
GENAI_MODEL=models/gemini-2.5-flash
```

### Run
```bash
flask run --host=0.0.0.0 --port=5000
```

Open the URL shown in your terminal (e.g. `https://<workspace>-5000.app.github.dev`).

---

## 🧪 Usage
1. Select a file (defaults to `utils.py`).
2. Pick a nuke strategy (e.g. `vibe-refine`, `testability`).
3. Click **Run Nuke**.
4. Review:
   - **Prompt**: What was sent to Gemini
   - **Preview**: Original code
   - **AI Refactor Output**: Gemini’s suggestion
   - **Diff View**: Unified diff with colored highlights

---

## 📡 Live AI Agents (Planned)

We’re extending the lab to support **live agents** — autonomous processes that can be deployed alongside the dashboard or integrated into other environments. These agents will:

- **Run continuously**: Monitor codebases, PRs, or logs and trigger nukes automatically.  
- **Expose APIs**: Allow external tools (CI/CD, Slack bots, VS Code extensions) to call into the agent.  
- **Collaborate**: Multiple agents can specialize (e.g., one for testability, one for security, one for readability).  
- **Stream results**: Provide partial diffs or commentary in real time.  
- **Integrate with workflows**: Deploy as GitHub Actions, serverless functions, or background workers.

---

## 🔄 System Flow

```text
 Developer
     │
     ▼
 ┌───────────────┐
 │  Dashboard /  │
 │   CLI / API   │
 └───────────────┘
     │
     ▼
 ┌───────────────┐
 │   Live Agent  │  (specialized nukes: testability, readability, security…)
 └───────────────┘
     │
     ▼
 ┌───────────────┐
 │   Gemini AI   │  (generate refactor output)
 └───────────────┘
     │
     ▼
 ┌───────────────┐
 │   Diff View   │  (original vs AI refactor, color‑highlighted)
 └───────────────┘
     │
     ▼
 Feedback to Developer
```

---

## 📈 Roadmap
- [x] Flask dashboard with diff view  
- [x] Default file selection (`utils.py`)  
- [x] Colored diff highlighting  
- [ ] Live AI agents for continuous monitoring and API integration  
- [ ] GitHub Action for automated PR refactors  
- [ ] VS Code extension for inline nukes  
- [ ] Slack/Teams bot trigger  

---

## 🤝 Contributing
PRs welcome! Please open an issue first to discuss major changes.

---

## 📜 License
MIT
