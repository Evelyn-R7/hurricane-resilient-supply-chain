#!/usr/bin/env python3
"""Lightweight validation for the public GitHub repository.

The script intentionally does not execute notebook cells or require Gurobi.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "DATA_SOURCES.md",
    "REPRODUCIBILITY.md",
    "requirements.txt",
    ".gitignore",
    "01_data_and_ml_pipeline.ipynb",
    "02_optimization_and_evaluation.ipynb",
    "03_robustness_and_sensitivity.ipynb",
    "04_interpretable_baselines_and_scenario_checks.ipynb",
    "results/figures/full464_cost_cvar_tradeoff.png",
    "results/tables/conference_full464_summary.csv",
]

FORBIDDEN_FILES = [
    "ibtracs_NA.csv",
]

# Detect common local absolute paths while avoiding URL schemes and escaped examples.
WINDOWS_ABS = re.compile(r"(?i)(?<![A-Za-z0-9])(?:C|D|E|F):[\\/]")
UNIX_HOME = re.compile(r"/(?:Users|home)/[^/\s]+/")


def fail(message: str) -> None:
    print(f"[FAIL] {message}")


def ok(message: str) -> None:
    print(f"[ OK ] {message}")


def main() -> int:
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if path.exists():
            ok(f"Required file present: {rel}")
        else:
            errors.append(f"Missing required file: {rel}")
            fail(errors[-1])

    for rel in FORBIDDEN_FILES:
        path = ROOT / rel
        if path.exists():
            errors.append(f"Forbidden raw file is present: {rel}")
            fail(errors[-1])
        else:
            ok(f"Forbidden raw file absent: {rel}")

    notebooks = sorted(ROOT.glob("*.ipynb"))
    for notebook_path in notebooks:
        try:
            notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"Invalid notebook JSON: {notebook_path.name}: {exc}")
            fail(errors[-1])
            continue

        code_cells = 0
        for index, cell in enumerate(notebook.get("cells", []), start=1):
            if cell.get("cell_type") != "code":
                continue
            code_cells += 1
            source = cell.get("source", "")
            if isinstance(source, list):
                source = "".join(source)
            # Notebook magics and shell commands are valid in Jupyter but not Python AST.
            filtered_lines = []
            for line in source.splitlines():
                stripped = line.lstrip()
                if stripped.startswith(("%", "!")):
                    filtered_lines.append("pass  # notebook magic or shell command")
                else:
                    filtered_lines.append(line)
            filtered = "\n".join(filtered_lines)
            try:
                compile(filtered, f"{notebook_path.name}:cell-{index}", "exec")
            except SyntaxError as exc:
                errors.append(
                    f"Python syntax error in {notebook_path.name}, code cell {index}: {exc}"
                )
                fail(errors[-1])
        if not any(err.startswith(f"Python syntax error in {notebook_path.name}") for err in errors):
            ok(f"Notebook JSON and code syntax valid: {notebook_path.name} ({code_cells} code cells)")

    text_suffixes = {".md", ".txt", ".py", ".yml", ".yaml", ".json", ".cff"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in text_suffixes:
            continue
        if ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        # CODEX instructions deliberately show generic git commands but should not
        # contain a real local absolute path.
        if WINDOWS_ABS.search(text) or UNIX_HOME.search(text):
            rel = path.relative_to(ROOT)
            errors.append(f"Possible local absolute path found in: {rel}")
            fail(errors[-1])

    if errors:
        print(f"\nValidation failed with {len(errors)} issue(s).")
        return 1

    print("\nRepository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
