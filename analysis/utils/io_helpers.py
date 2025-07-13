from __future__ import annotations

import os
import numpy as np
import pandas as pd
from typing import Tuple


def extract_columns(file_path: str) -> pd.DataFrame:
    """Load a tab-separated text file and return time, voltage and current columns.

    Parameters
    ----------
    file_path:
        Path to the text file.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing ``ti``, ``V`` and ``I`` columns.
    """
    df = pd.read_csv(file_path, sep="\t", header=None)
    extracted = df.iloc[:, [0, 2, 3]].copy()
    extracted.columns = ["ti", "V", "I"]
    return extracted


def extract_and_process_csv(file_path: str) -> pd.DataFrame:
    """Load tracking data (time, x/px, y/px) and compute angle column."""
    df = pd.read_csv(file_path)
    extracted = df.iloc[:, [0, 1, 2]].copy()
    extracted.columns = ["td", "x/px", "y/px"]
    extracted["d"] = np.arctan2(extracted["y/px"], extracted["x/px"])
    return extracted


def get_df(folder_IV_path: str, folder_def_path: str, startwith: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Return IV and deflection data for a given test prefix."""
    for filename1 in os.listdir(folder_def_path):
        if filename1.startswith(startwith):
            filedef = os.path.join(folder_def_path, filename1)
            break
    else:
        raise FileNotFoundError(startwith)

    for filename2 in os.listdir(folder_IV_path):
        if filename2.startswith(filename1[:4]):
            fileIV = os.path.join(folder_IV_path, filename2)
            break
    else:
        raise FileNotFoundError(filename1[:4])

    df1 = pd.read_csv(fileIV, sep="\t", header=None)
    df2 = pd.read_csv(filedef, sep=",", header=None)
    df2[3] = np.arctan2(df2[2], df2[1])
    return df1, df2


def read(df1: pd.DataFrame, df2: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Convert raw data frames returned by :func:`get_df` into numpy arrays."""
    ti = df1[0].to_numpy()
    I = df1[2].to_numpy()
    V = df1[3].to_numpy()
    td = df2[0].to_numpy()
    d = df2[3].to_numpy()
    return ti, I, V, td, d
