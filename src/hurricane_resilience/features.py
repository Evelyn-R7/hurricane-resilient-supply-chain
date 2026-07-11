"""Feature definitions used by the predictive risk models."""

import pandas as pd

IDENTIFIER_COLUMNS = ("storm_id", "node_id")


def split_features_target(df: pd.DataFrame, target: str, features: list[str]):
    missing = set([target, *features]).difference(df.columns)
    if missing:
        raise ValueError(f"Missing modeling columns: {sorted(missing)}")
    return df.loc[:, features].copy(), df[target].astype(int).copy()


def add_storm_summary_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add leakage-safe per-storm summaries from columns already present."""
    out = df.copy()
    if {"storm_id", "max_wind"}.issubset(out.columns):
        grouped = out.groupby("storm_id")["max_wind"]
        out["storm_max_wind"] = grouped.transform("max")
        out["storm_mean_wind"] = grouped.transform("mean")
    return out
