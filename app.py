from dotenv import load_dotenv
import os
import google.generativeai as genai
import difflib

# Load environment and configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
GENAI_MODEL = os.getenv("GENAI_MODEL", "models/gemini-2.5-flash")

# Instantiate the GenerativeModel once at module load for reuse across requests
try:
    model = genai.GenerativeModel(GENAI_MODEL)
except Exception:
    # Fallback: ensure module import doesn't fail hard during import-time in dev
    model = None

# Ensure key present for clearer error messages early
if not os.getenv("GOOGLE_API_KEY"):
    raise RuntimeError(
        "Missing GOOGLE_API_KEY in environment. Create a .env file with "
        "GOOGLE_API_KEY=<your_key> at the repository root."
    )

from flask import Flask, render_template, request
from tools import nuke_agent

app = Flask(__name__)

def run_with_gemini(prompt: str) -> str:
    """Call the pre-created GenerativeModel.generate_content(prompt) and return response.text or an error string."""
    if model is None:
        return "AI error: model not initialized"
    try:
        response = model.generate_content(prompt)
        # Prefer .text per expected response shape
        return getattr(response, "text", str(response))
    except Exception as exc:
        return f"AI error: {exc}"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        filename = request.form.get("filename", "utils.py").strip() or "utils.py"
        nuke = request.form.get("nuke", "").strip()
        try:
            result = nuke_agent.run_nuke(filename, nuke)
            # Call Gemini with the preview and store the output
            result["ai_output"] = run_with_gemini(result.get("preview", ""))

            # Generate unified diff between original preview and AI refactor output
            original = str(result.get("preview", "")).splitlines()
            ai_out = str(result.get("ai_output", "")).splitlines()
            diff = difflib.unified_diff(
                original,
                ai_out,
                fromfile="original",
                tofile="ai_refactor",
                lineterm=""
            )
            result["diff"] = "\n".join(diff)

        except Exception as exc:
            # Ensure diff key exists even on error for template stability
            result = {"error": str(exc), "diff": ""}
    return render_template("index.html", result=result, nukes=nuke_agent.NUKES.keys())

if __name__ == "__main__":
    app.run(debug=True)
