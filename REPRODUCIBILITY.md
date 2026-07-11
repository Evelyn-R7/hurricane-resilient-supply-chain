# Reproduction notes

## Full result workflow

1. `notebooks/01_data_and_ml_pipeline.ipynb`
2. Phases 1–2 of `notebooks/04_interpretable_baselines_and_scenario_checks.ipynb`
3. `notebooks/02_optimization_and_evaluation.ipynb`
4. `notebooks/03_robustness_and_sensitivity.ipynb`

The apparent 01 → 04 → 02 order is intentional: Notebook 04 creates the engineered-logistic and coastal/inland risk matrices consumed by the conference-extension cells at the end of Notebook 02.

## Solver-free inspection

The curated tables and figures under `results/` can be inspected without Gurobi. Notebook 04 Phases 1–2 are also Gurobi-free.

Run the solver-free repository checks from the command line with:

```bash
python scripts/run_full_pipeline.py
python -m unittest discover -s tests
```

## Full recomputation

Set `FORCE_RECOMPUTE = True` in Notebook 02 only after confirming that Gurobi is installed and licensed. The saved outputs are useful for verifying that a new run remains numerically consistent.
