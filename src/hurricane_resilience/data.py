"""Data loading and IBTrACS/event-node preprocessing helpers."""

from pathlib import Path
import numpy as np
import pandas as pd

from .paths import PROJECT_ROOT


def read_csv(path: str | Path, **kwargs) -> pd.DataFrame:
    path = Path(path)
    resolved = path if path.is_absolute() else PROJECT_ROOT / path
    if not resolved.is_file():
        raise FileNotFoundError(f"Data file not found: {resolved}")
    return pd.read_csv(resolved, **kwargs)


def haversine_km(lat1, lon1, lat2, lon2):
    """Great-circle distance in kilometres; accepts scalars or arrays."""
    lat1, lon1, lat2, lon2 = map(np.radians, (lat1, lon1, lat2, lon2))
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    return 6371.0088 * 2 * np.arcsin(np.sqrt(a))


def load_event_node_data(path: str | Path = "storm_node_dataset_14nodes_200km_50kt.csv") -> pd.DataFrame:
    df = read_csv(path)
    if "node_id" not in df.columns:
        raise ValueError("Event-node data missing column: node_id")
    if not {"SID", "storm_id"}.intersection(df.columns):
        raise ValueError("Event-node data must contain SID or storm_id")
    return df


def read_ibtracs(path: str | Path, **kwargs) -> pd.DataFrame:
    """Read a user-downloaded IBTrACS CSV without bundling it in the repository."""
    defaults = {"low_memory": False}
    defaults.update(kwargs)
    return read_csv(path, **defaults)
