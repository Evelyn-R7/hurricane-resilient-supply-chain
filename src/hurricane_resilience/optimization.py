"""Gurobi integration points for the two-stage CVaR model.

The complete approved algebra remains visible in Notebook 02 while its large global
state is incrementally converted to explicit parameter objects. Importing this module
never requires Gurobi; solving does.
"""

from dataclasses import dataclass
from typing import Mapping, Sequence


@dataclass(frozen=True)
class OptimizationSettings:
    alpha: float = 0.90
    time_limit: float | None = None
    mip_gap: float | None = None


def require_gurobi():
    try:
        import gurobipy as gp
        from gurobipy import GRB
    except ImportError as exc:
        raise RuntimeError("Install gurobipy and activate a valid Gurobi license to solve models") from exc
    return gp, GRB


def validate_optimization_inputs(scenarios: Sequence, scenario_weights: Mapping) -> None:
    missing = set(scenarios).difference(scenario_weights)
    if missing:
        raise ValueError(f"Missing weights for scenarios: {sorted(missing)}")
    total = sum(float(scenario_weights[s]) for s in scenarios)
    if abs(total - 1.0) > 1e-9:
        raise ValueError(f"Scenario weights must sum to one; got {total}")
