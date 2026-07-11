"""Scenario construction, reduction, and weight validation."""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


def validate_scenario_weights(weights, *, atol: float = 1e-9) -> np.ndarray:
    values = np.asarray(weights, dtype=float)
    if values.ndim != 1 or values.size == 0 or not np.isfinite(values).all():
        raise ValueError("Scenario weights must be a finite, non-empty vector")
    if (values < 0).any():
        raise ValueError("Scenario weights cannot be negative")
    if not np.isclose(values.sum(), 1.0, atol=atol):
        raise ValueError(f"Scenario weights must sum to one; got {values.sum():.12g}")
    return values


def normalize_scenario_weights(weights) -> np.ndarray:
    values = np.asarray(weights, dtype=float)
    if (values < 0).any() or not np.isfinite(values).all() or values.sum() <= 0:
        raise ValueError("Cannot normalize invalid scenario weights")
    return values / values.sum()


def kmeans_reduce(matrix: pd.DataFrame, n_clusters: int, *, random_state: int = 42, n_init: int = 50):
    model = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init)
    labels = model.fit_predict(matrix.to_numpy(dtype=float))
    representatives = []
    for cluster in range(n_clusters):
        indices = np.flatnonzero(labels == cluster)
        distances = np.linalg.norm(matrix.iloc[indices].to_numpy() - model.cluster_centers_[cluster], axis=1)
        representatives.append(matrix.index[indices[np.argmin(distances)]])
    weights = normalize_scenario_weights(np.bincount(labels, minlength=n_clusters))
    return representatives, weights, labels
