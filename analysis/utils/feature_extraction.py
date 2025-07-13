import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from typing import Tuple, Sequence


def peakfinder(x: str, y: str, dataframe: pd.DataFrame, *, height: float = 0.0, distance: int = 1) -> Tuple[np.ndarray, Sequence[float], np.ndarray, Sequence[float], np.ndarray, np.ndarray]:
    """Locate peaks and troughs in ``y`` within ``dataframe``.

    Parameters
    ----------
    x:
        Column name representing the x-axis (typically time).
    y:
        Column name of the signal to analyse.
    dataframe:
        Data set containing ``x`` and ``y`` columns.
    height:
        Minimum peak height for detection.
    distance:
        Minimum number of samples between neighbouring peaks.

    Returns
    -------
    Tuple containing peak indices, peak times, trough indices, trough times,
    x-values and y-values used for analysis.
    """
    xdata = np.asarray(dataframe[x])
    ydata = np.asarray(dataframe[y])

    peak_indices, _ = find_peaks(ydata, height=height, distance=distance)
    trough_indices, _ = find_peaks(-ydata, height=-height, distance=distance)

    peak_times = xdata[peak_indices]
    trough_times = xdata[trough_indices]

    return peak_indices, peak_times, trough_indices, trough_times, xdata, ydata
