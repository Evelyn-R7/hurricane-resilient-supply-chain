"""CVaR and Pareto evaluation shared by optimization notebooks."""

import numpy as np
import pandas as pd
from .scenarios import validate_scenario_weights


def weighted_cvar(losses, weights, alpha: float = 0.90) -> tuple[float, float]:
    """Return the discrete weighted CVaR and its minimizing VaR threshold."""
    losses = np.asarray(losses, dtype=float)
    weights = validate_scenario_weights(weights)
    if losses.shape != weights.shape:
        raise ValueError("Losses and weights must have the same shape")
    if not 0 <= alpha < 1:
        raise ValueError("alpha must satisfy 0 <= alpha < 1")
    candidates = np.unique(losses)
    values = [eta + np.sum(weights * np.maximum(losses - eta, 0.0)) / (1.0 - alpha) for eta in candidates]
    best = int(np.argmin(values))
    return float(values[best]), float(candidates[best])


def extract_nondominated(df: pd.DataFrame, cost_col: str, risk_col: str, tol: float = 1e-6) -> pd.DataFrame:
    temp = df.dropna(subset=[cost_col, risk_col]).copy().reset_index(drop=True)
    keep = []
    for i, row in temp.iterrows():
        dominated = any((other[cost_col] <= row[cost_col] + tol and other[risk_col] <= row[risk_col] + tol)
                        and (other[cost_col] < row[cost_col] - tol or other[risk_col] < row[risk_col] - tol)
                        for j, other in temp.iterrows() if i != j)
        keep.append(not dominated)
    return temp.loc[keep].sort_values([risk_col, cost_col]).reset_index(drop=True)
