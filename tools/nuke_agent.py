from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Dict, Any

NUKES: Dict[str, str] = {
    "vibe-refine": """Vibe-refine this code: Prune bulk for compactness (DRY it up), enforce logical flow (one responsibility per function), boost maintainability (modular + types), and harden against errors (guards + tests). Provide a concise patch or diff, explain each change briefly, and include unit tests for any behavioral changes.""",

    "perf-audit": """Perf-audit this beast: Identify hotspots, measure complexity and bottlenecks, suggest targeted micro- and macro-optimizations (algorithmic, data-structure, I/O, concurrency), provide before/after complexity estimates, minimal safe code changes with benchmarks or cost estimates, and note any trade-offs.""",

    "readability": """Readability polish: Improve naming, break up long functions, simplify conditionals and control flow, add or improve docstrings and inline clarifying comments, and reformat for consistent style. Produce minimal diffs and a short rationale for each change that affects comprehension.""",

    "testability": """Testability boost: Add focused unit tests and fixtures (pytest), isolate side effects, introduce seams or small refactors to make code injection-friendly for tests, assert edge cases and guard behavior, and provide commands to run the new tests. Prefer small, reviewable changes.""",

    "wildcard": """Wildcard nuke: Perform a pragmatic, conservative sweep for low-effort high-value improvements across the repo — remove obvious dead code, consolidate duplicates, add basic guards, and provide a short prioritized list of remaining deeper issues. Include diffs for the quick wins.""",

    "scale-nuke": """Scale-nuke: Prepare the code for higher concurrency and throughput. Identify blocking points, propose concurrency models (async, thread pool, worker queues), recommend data-sharding or batching strategies, and include minimal code changes or adapters to enable scaling while noting trade-offs and failure modes.""",

    "memory-melt": """Memory-melt: Reduce memory pressure and leaks. Identify heavy allocations, long-lived caches, and retention patterns; propose streaming, generators, or chunked processing alternatives; estimate memory/throughput improvements and include small, safe refactors with benchmarks or cost estimates.""",

    "porta-blast": """Porta-blast: Make the code portable and package-ready. Normalize CLI/help text, add installation notes, ensure cross-platform path/encoding handling, add or update packaging metadata (pyproject/entry points), and provide a checklist for publishing and reproducible builds.""",

    "eco-nuke": """Eco-nuke: Optimize for efficiency and operational cost. Suggest lower-power or lower-cost alternatives (reduced polling, batching, caching), quantify expected savings, prefer simpler algorithms with similar correctness, and include only conservative patches that keep behavior intact while lowering resource usage.""",
}


def load_code(path: Path | str) -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")
    if not p.is_file():
        raise ValueError(f"Not a regular file: {p}")
    try:
        return p.read_text(encoding="utf-8")
    except Exception as exc:
        raise RuntimeError(f"Failed to read {p}: {exc}") from exc


def get_nuke_prompt(nuke: str) -> str:
    if not isinstance(nuke, str) or not nuke.strip():
        raise ValueError("nuke must be a non-empty string")
    return NUKES.get(nuke, f"Unknown nuke: {nuke}")


def prepare_preview(code: str, length: int = 200) -> str:
    if not isinstance(code, str):
        raise ValueError("code must be a string")
    snippet = code[:length]
    return snippet + ("..." if len(code) > length else "")


def run_nuke(file: Path | str, nuke: str) -> Dict[str, Any]:
    code = load_code(file)
    prompt = get_nuke_prompt(nuke)
    preview = prepare_preview(code)
    return {
        "file": str(Path(file)),
        "nuke": nuke,
        "prompt": prompt,
        "preview": preview,
        "code_len": len(code),
    }


def _print_result(result: Dict[str, Any]) -> None:
    print(f"Running {result['nuke']} on {result['file']}")
    print("--- Code Preview ---")
    print(result["preview"])
    print("--- Prompt ---")
    print(result["prompt"])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="nuke_agent")
    parser.add_argument("--file", required=True)
    parser.add_argument("--nuke", required=True)
    args = parser.parse_args(argv)
    try:
        result = run_nuke(args.file, args.nuke)
        _print_result(result)
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
