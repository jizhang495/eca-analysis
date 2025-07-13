"""High level routines for analysing AC actuation data."""

from pathlib import Path
import pandas as pd
from typing import Tuple

from .utils import (
    peakfinder,
    extract_columns,
    extract_and_process_csv,
    plot_V_I_def,
    plot_V_I_Q_def,
    average,
    sd,
    sds,
)


def load_iv_def(iv_file: Path, def_file: Path) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Load IV and deflection data from files."""
    df_iv = extract_columns(str(iv_file))
    df_def = extract_and_process_csv(str(def_file))
    return df_iv, df_def


__all__ = [
    "load_iv_def",
    "peakfinder",
    "plot_V_I_def",
    "plot_V_I_Q_def",
    "average",
    "sd",
    "sds",
]
