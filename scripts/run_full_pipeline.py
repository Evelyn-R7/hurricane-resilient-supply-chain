"""Run the repository's main reproducible, non-destructive pipeline checks.

By default this validates published inputs and outputs without recomputing approved
research results. Pass --execute-notebooks to run the notebooks in order; Gurobi
notebooks still require a valid installation and license.
"""

from __future__ import annotations
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = [
    "01_data_and_ml_pipeline.ipynb",
    "02_optimization_and_evaluation.ipynb",
    "03_robustness_and_sensitivity.ipynb",
    "04_interpretable_baselines_and_scenario_checks.ipynb",
]


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute-notebooks", action="store_true")
    parser.add_argument("--allow-gurobi", action="store_true",
                        help="Acknowledge that optimization notebooks may invoke licensed Gurobi solves")
    args = parser.parse_args()
    run([sys.executable, "scripts/validate_repository.py"])
    if args.execute_notebooks:
        if not args.allow_gurobi:
            parser.error("--execute-notebooks requires --allow-gurobi")
        for name in NOTEBOOKS:
            run([sys.executable, "-m", "jupyter", "nbconvert", "--execute", "--inplace",
                 str(ROOT / "notebooks" / name)])
    else:
        print("Published inputs/results validated; notebooks were not recomputed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
