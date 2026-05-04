# Public NQS Ansatz Notes

## Why Not Directly Scale?

For triangular charge-order problems, small-cluster exact or ED benchmarks are necessary before large sampled VMC. The reason is that a sampled trajectory can appear to find a low-energy state while failing under replay or sector-resolved diagnostics.

## Design Principles

1. Use physical branch features, not only larger networks.
2. Separate charge-order branch selection from within-branch amplitude accuracy.
3. Test exact-sum prototypes on small clusters before submitting large sampled jobs.
4. Report train-best and strict replay separately.
5. Treat finite-size ED as a benchmark, not as a thermodynamic phase proof.

## Candidate Feature Set

For a triangular lattice split into three sublattices, useful public features include:

- sublattice occupation vector `(n0, n1, n2)`;
- normalized imbalance from uniform filling;
- max-min sublattice density contrast;
- charge-order feature at `K`;
- simple domain-wall or branch-purity proxies.

