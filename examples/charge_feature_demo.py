"""Minimal demo for triangular charge-order features."""

from __future__ import annotations

import numpy as np

from triangular_moire_public import normalized_sublattice_densities, sublattice_contrast


def main() -> None:
    counts = np.array([7, 5, 4])
    sites_per_sublattice = 8
    print("densities:", normalized_sublattice_densities(counts, sites_per_sublattice))
    print("contrast:", f"{sublattice_contrast(counts, sites_per_sublattice):.6f}")


if __name__ == "__main__":
    main()

