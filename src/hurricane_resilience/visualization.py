"""Consistent project-relative figure output."""

from pathlib import Path
from matplotlib.figure import Figure
from .paths import FIGURES_DIR


def save_figure(fig: Figure, filename: str, *, dpi: int = 300, directory: Path = FIGURES_DIR) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / filename
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
    return path
