import numpy as np
from typing import Sequence


def average(values: Sequence[float]) -> float:
    """Return the arithmetic mean of ``values``.

    Parameters
    ----------
    values:
        Sequence of numeric values.

    Returns
    -------
    float
        Arithmetic mean of the numbers.
    """
    return float(np.mean(values))


def sd(values: Sequence[float]) -> float:
    """Return the population standard deviation of ``values``."""
    return float(np.std(values, ddof=0))


def sds(values: Sequence[float]) -> float:
    """Return the sample standard deviation of ``values``."""
    return float(np.std(values, ddof=1))
