# Moire Pinball Benchmark

## Model Class

This line studies triangular moire-inspired spinless fermion models with further-neighbor interactions:

```text
H = -t sum_<ij> (c_i^dagger c_j + h.c.)
    + V1 sum_<ij> n_i n_j
    + V2 sum_<<ij>> n_i n_j
    + V3 sum_<<<ij>>> n_i n_j
```

The target regime is `nu=2/3`, where one can search for charge-order enhanced but still partially itinerant finite-cluster states.

## Diagnostic Logic

A pinball-like candidate should not be identified by charge modulation alone. The benchmark therefore checks:

- `S_c(K)` enhancement;
- three-sublattice density imbalance;
- finite kinetic energy;
- charge gap and neutral spectrum;
- twist and shape robustness;
- whether bond-resolved kinetic channels support a partially itinerant mechanism.

## Claim Boundary

The safe public wording is:

> finite-cluster ridge candidate / partially itinerant charge-order candidate.

The following wording is intentionally avoided:

> thermodynamic pinball phase discovered.

That stronger claim would require larger-size scaling, clearer mechanism observables, and NQS/VMC or other many-body checks beyond the finite-cluster ED ridge.

