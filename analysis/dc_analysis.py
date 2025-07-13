"""High level routines for analysing DC actuation data."""

from pathlib import Path
import pandas as pd
from typing import Tuple

from .utils import (
    get_df,
    read,
    plot_V_I_Q_def,
    average,
    sd,
    sds,
)


def load_experiment(folder_iv: Path, folder_def: Path, prefix: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Load a pair of IV/deflection files starting with ``prefix``."""
    return get_df(str(folder_iv), str(folder_def), prefix)


__all__ = [
    "load_experiment",
    "read",
    "plot_V_I_Q_def",
    "average",
    "sd",
    "sds",
]
