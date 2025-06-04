from typing import Sequence


def linprop(x: Sequence[float], k: float) -> Sequence[float]:
    """Simple linear model ``y = k * x`` used for curve fitting."""
    return [k * xi for xi in x]
