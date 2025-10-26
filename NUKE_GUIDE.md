# # 🧨 Nuke Guide — The Arsenal

Welcome to the **Nuke Arsenal** — a curated set of nine transformation prompts designed to turn everyday code into production‑ready, maintainable, and scalable systems.  

Each “nuke” is a specialized refactoring strategy: some focus on readability, others on performance, testability, or cost efficiency. Together, they form a repeatable toolkit you and your team can rely on for consistent improvements.  

This guide is your quick‑reference playbook:
- **Full prompts**: Copy‑paste ready for the Flask dashboard or Copilot Chat.  
- **Example usage**: How to apply each nuke in practice.  
- **Tips**: Best practices for large files, diffs, and validation.  

Think of it as your **field manual** — whether you’re onboarding a teammate, cleaning up legacy code, or stress‑testing for scale, there’s a nuke here to fit the mission.


Onboarding
1. Copy .env.example to .env and add your key.  
2. Run flask run.  
3. Upload a file, pick a nuke, and review the AI output.

---

## 1) vibe-refine
Full prompt
```
Vibe-refine this code: Prune bulk for compactness (DRY it up), enforce logical flow (one responsibility per function), boost maintainability (modular + types), and harden against errors (guards + tests). Provide a concise patch or diff, explain each change briefly, and include unit tests for any behavioral changes.
```
Example usage
- Dashboard: select "vibe-refine", submit your file.  
- Copilot Chat: paste the prompt, then paste the file contents and request a diff.

---

## 2) perf-audit
Full prompt
```
Perf-audit this beast: Identify hotspots, measure complexity and bottlenecks, suggest targeted micro- and macro-optimizations (algorithmic, data-structure, I/O, concurrency), provide before/after complexity estimates, minimal safe code changes with benchmarks or cost estimates, and note any trade-offs.
```
Example usage
- Dashboard: choose "perf-audit" and run; read AI notes for hotspots.  
- Copilot Chat: paste prompt + file and ask for specific micro-benchmarks.

---

## 3) readability
Full prompt
```
Readability polish: Improve naming, break up long functions, simplify conditionals and control flow, add or improve docstrings and inline clarifying comments, and reformat for consistent style. Produce minimal diffs and a short rationale for each change that affects comprehension.
```
Example usage
- Dashboard: pick "readability" to get a human-friendly refactor.  
- Copilot Chat: paste prompt + file, ask for a short rationale for each change.

---

## 4) testability
Full prompt
```
Testability boost: Add focused unit tests and fixtures (pytest), isolate side effects, introduce seams or small refactors to make code injection-friendly for tests, assert edge cases and guard behavior, and provide commands to run the new tests. Prefer small, reviewable changes.
```
Example usage
- Dashboard: "testability" will suggest tests and small refactors.  
- Copilot Chat: paste prompt + file, request pytest files and run commands.

---

## 5) wildcard
Full prompt
```
Wildcard nuke: Perform a pragmatic, conservative sweep for low-effort high-value improvements across the repo — remove obvious dead code, consolidate duplicates, add basic guards, and provide a short prioritized list of remaining deeper issues. Include diffs for the quick wins.
```
Example usage
- Dashboard: run "wildcard" for general quick wins.  
- Copilot Chat: paste prompt + multiple file snippets and ask for prioritized list.

---

## 6) scale-nuke
Full prompt
```
Scale-nuke: Prepare the code for higher concurrency and throughput. Identify blocking points, propose concurrency models (async, thread pool, worker queues), recommend data-sharding or batching strategies, and include minimal code changes or adapters to enable scaling while noting trade-offs and failure modes.
```
Example usage
- Dashboard: choose "scale-nuke" to get scaling recommendations.  
- Copilot Chat: paste prompt + hotspots and ask for a migration plan.

---

## 7) memory-melt
Full prompt
```
Memory-melt: Reduce memory pressure and leaks. Identify heavy allocations, long-lived caches, and retention patterns; propose streaming, generators, or chunked processing alternatives; estimate memory/throughput improvements and include small, safe refactors with benchmarks or cost estimates.
```
Example usage
- Dashboard: run "memory-melt" to find memory issues and fixes.  
- Copilot Chat: paste prompt + offending module and request streaming refactor.

---

## 8) porta-blast
Full prompt
```
Porta-blast: Make the code portable and package-ready. Normalize CLI/help text, add installation notes, ensure cross-platform path/encoding handling, add or update packaging metadata (pyproject/entry points), and provide a checklist for publishing and reproducible builds.
```
Example usage
- Dashboard: pick "porta-blast" to prep for packaging.  
- Copilot Chat: paste prompt + project metadata and ask for pyproject changes.

---

## 9) eco-nuke
Full prompt
```
Eco-nuke: Optimize for efficiency and operational cost. Suggest lower-power or lower-cost alternatives (reduced polling, batching, caching), quantify expected savings, prefer simpler algorithms with similar correctness, and include only conservative patches that keep behavior intact while lowering resource usage.
```
Example usage
- Dashboard: run "eco-nuke" for cost/efficiency suggestions.  
- Copilot Chat: paste prompt + runtime metrics and request estimated savings.

---

How to use from the Flask dashboard
- Start the app (flask run).  
- In the web UI: enter the file path (or paste filename if your environment exposes files), select the desired nuke from the dropdown, and click "Run Nuke".  
- The results panel will show the Prompt, Code Preview, and the AI Refactor Output side-by-side.

How to use with Copilot Chat
1. Open Copilot Chat.  
2. Paste one of the full prompts above.  
3. Paste the target file contents after the prompt (or attach where supported).  
4. Ask for a patch/diff, tests, or a step-by-step migration depending on the nuke.

Tips
- For large files: prefer pasting a focused excerpt or the top ~200 lines; include a short note about the file's role.  
- When expecting diffs, request "apply minimal changes" or "show a unified diff" in the same message to get patch-style output.  
- Use the "vibe-refine" nuke for small cleanup, and "wildcard" for broad conservative improvements.