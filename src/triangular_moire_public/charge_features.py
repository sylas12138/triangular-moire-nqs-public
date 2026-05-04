"""Lightweight public helpers for triangular sublattice charge features."""

from __future__ import annotations

import numpy as np


def normalized_sublattice_densities(counts: np.ndarray, sites_per_sublattice: int) -> np.ndarray:
    """Return three normalized sublattice densities."""
    counts = np.asarray(counts, dtype=float)
    if counts.shape != (3,):
        raise ValueError("counts must contain three sublattice occupations")
    if sites_per_sublattice <= 0:
        raise ValueError("sites_per_sublattice must be positive")
    return counts / sites_per_sublattice


def sublattice_contrast(counts: np.ndarray, sites_per_sublattice: int) -> float:
    """Return max-min contrast of normalized three-sublattice densities."""
    densities = normalized_sublattice_densities(counts, sites_per_sublattice)
    return float(np.max(densities) - np.min(densities))

