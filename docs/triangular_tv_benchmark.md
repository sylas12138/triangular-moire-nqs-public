# `nu=1/3` Triangular t-V Benchmark

## Model

The basic model is a spinless fermion nearest-neighbor `t-V` Hamiltonian on a triangular lattice:

```text
H = -t sum_<ij> (c_i^dagger c_j + h.c.) + V sum_<ij> n_i n_j
```

At `nu=1/3`, strong repulsion favors three-sublattice charge ordering. This makes the model a useful finite-cluster benchmark for NQS ansatz design and sampled VMC diagnostics.

## NQS/VMC Difficulty

The key difficulty is not just representing charge order. The harder problem is ensuring that the trained NQS state remains stable under replay and does not rely on selector optimism or short-lived training artifacts.

Public failure axes:

- train-best can be more optimistic than replay;
- branch / sector occupation can drift;
- sampled VMC can overweight a sector;
- strict observables can recover order while energy remains off;
- adding seeds or replay alone is not a structural solution.

## Ansatz Direction

The public ansatz concept is a branch-conditioned mixture of experts:

```text
psi(x) = sum_b softmax(g_b(x) + a_b) psi_b(x)
```

where each `b` labels a three-sublattice charge-order branch. The gate `g_b(x)` should use physical low-dimensional features such as sublattice density differences and `K`-point charge features, rather than an unconstrained black-box classifier.

