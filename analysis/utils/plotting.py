from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple, Sequence


def plot_V_I_def(ti: Sequence[float], I: Sequence[float], V: Sequence[float], td: Sequence[float], d: Sequence[float]) -> Tuple[plt.Figure, Tuple[plt.Axes, plt.Axes, plt.Axes]]:
    """Create a three panel plot of voltage, current and deflection."""
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(20, 8), sharex=True, gridspec_kw=dict(height_ratios=[2, 3, 3]))
    ax1.plot(ti, V, color='tab:orange', lw=1)
    ax1.set_ylabel('$V$/V', color='black')
    ax2.plot(ti, I, color='blue', lw=1)
    ax2.set_ylabel('$I$/mA', color='black')
    ax3.plot(td, d, color='green', lw=1)
    ax3.set(xlabel='Time/s', ylabel=r'$\\theta$/rad')
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    ax1.axhline(y=0, color='#999999', linestyle='--')
    ax2.axhline(y=0, color='#999999', linestyle='--')
    ax3.axhline(y=0, color='#999999', linestyle='--')
    for ax in (ax1, ax2, ax3):
        ax.tick_params(direction='out', length=5, width=1, colors='black')
    plt.subplots_adjust(hspace=.0)
    return fig, (ax1, ax2, ax3)


def scatter_V_I_def(ti: Sequence[float], I: Sequence[float], V: Sequence[float], td: Sequence[float], d: Sequence[float]) -> Tuple[plt.Figure, Tuple[plt.Axes, plt.Axes, plt.Axes]]:
    """Scatter plot variant of :func:`plot_V_I_def`."""
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 7), sharex=True, gridspec_kw=dict(height_ratios=[2, 3, 3]))
    ax1.scatter(ti, V, color='tab:orange', s=10, alpha=0.3, facecolors='none', edgecolors='tab:orange')
    ax1.set_ylabel('$V$/V', color='black')
    ax2.scatter(ti, I, color='blue', s=10, alpha=0.3, facecolors='none', edgecolors='blue')
    ax2.set_ylabel('$I$/mA', color='black')
    ax3.scatter(td, d, color='green', s=10, alpha=0.3, facecolors='none', edgecolors='green')
    ax3.set(xlabel='Time/s', ylabel=r'$\\theta$/rad')
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    ax1.axhline(y=0, color='#999999', linestyle='--')
    ax2.axhline(y=0, color='#999999', linestyle='--')
    ax3.axhline(y=0, color='#999999', linestyle='--')
    for ax in (ax1, ax2, ax3):
        ax.tick_params(direction='out', length=5, width=1, colors='black')
    plt.subplots_adjust(hspace=.0)
    return fig, (ax1, ax2, ax3)


def plot_V_I_Q_def(ti: Sequence[float], I: Sequence[float], V: Sequence[float], td: Sequence[float], d: Sequence[float]) -> Tuple[plt.Figure, Tuple[plt.Axes, plt.Axes, plt.Axes, plt.Axes], np.ndarray]:
    """Plot voltage, current, accumulated charge and deflection."""
    import scipy.integrate as sp
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(20, 8), sharex=True, gridspec_kw=dict(height_ratios=[2, 3, 3, 3]))
    ax1.plot(ti, V, color='tab:orange', lw=1)
    ax1.set_ylabel('$V$/V', color='black')
    ax2.plot(ti, I, color='blue', lw=1)
    ax2.set_ylabel('$I$/mA', color='black')
    Q = sp.cumulative_trapezoid(I, ti, initial=0)
    ax3.plot(ti, Q, color='tab:blue', lw=1)
    ax3.axhline(y=0, color='#999999', linestyle='--')
    ax3.set_ylabel(r'$Q_{fit}$/mC', color='black')
    ax4.plot(td, d, color='green', lw=1)
    ax4.set(xlabel='Time/s', ylabel=r'$\\theta$/rad')
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    ax1.axhline(y=0, color='#999999', linestyle='--')
    ax2.axhline(y=0, color='#999999', linestyle='--')
    ax4.axhline(y=d[3] if len(d) > 3 else d[-1], color='#999999', linestyle='--')
    for ax in (ax1, ax2, ax3, ax4):
        ax.tick_params(direction='out', length=5, width=1, colors='black')
    plt.subplots_adjust(hspace=.0)
    return fig, (ax1, ax2, ax3, ax4), Q
