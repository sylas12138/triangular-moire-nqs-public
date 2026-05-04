# Triangular t-V and Moire Pinball NQS Benchmarks

Public research portfolio for triangular-lattice spinless fermion benchmarks, moire-inspired extended Hubbard models, and NQS/VMC method development.

This repository summarizes two related project lines:

1. `nu=1/3` triangular nearest-neighbor `t-V` charge-order / generalized-Wigner-crystal benchmark.
2. `nu=2/3` triangular moire `t-V1-V2-V3` ED/NQS benchmark for pinball-like partially itinerant charge-order candidates.

The public version includes model descriptions, benchmark logic, diagnostic definitions, and lightweight code snippets. It does **not** include raw result trees, remote-cluster scripts, checkpoint files, detailed experiment logs, private failure ledgers, or agent instructions.

## 1. Why This Project?

Triangular-lattice correlated fermion models are useful for studying:

- geometric frustration;
- charge ordering and generalized Wigner crystals;
- first-order or multi-basin optimization landscapes;
- moire flat-band inspired effective models;
- partially itinerant charge order, often discussed in pinball-liquid language.

For NQS/VMC, these systems expose a key difficulty: a wavefunction may find a low-energy basin but fail under strict replay, sector diagnostics, or finite-size checks. Therefore the project uses ED benchmark and observable audit before scaling NQS.

## 2. Track A: `nu=1/3` triangular `t-V`

The nearest-neighbor triangular `t-V` line serves as a GWC / charge-order sanity benchmark.

Main questions:

- Can NQS represent three-sublattice charge order?
- Does sampled VMC preserve the sector found during training?
- Are train-best checkpoints overly optimistic?
- Which ansatz structures reduce branch locking and selector bias?

Publicly documented ansatz ideas include:

- branch-conditioned mixture of experts;
- physically low-dimensional branch gates;
- branch-specific Jastrow / backflow;
- exact-sum small-cluster prototypes before large sampled VMC.

## 3. Track B: `nu=2/3` moire `t-V1-V2-V3`

The moire-inspired line studies triangular extended Hubbard models with further-neighbor interactions. The target is not to immediately claim a thermodynamic pinball phase, but to find finite-cluster windows where charge modulation is enhanced while kinetic energy remains finite.

Diagnostics include:

- charge structure factor `S_c(K)`;
- three-sublattice density imbalance;
- charge gap and low-lying spectrum;
- bond-resolved kinetic channels;
- twist / boundary / shape audits;
- NQS vs ED consistency on small clusters.

## 4. Safe Claim Boundary

Safe public claim:

> This project builds ED/NQS benchmark logic for triangular-lattice charge-order and moire pinball-candidate problems, with explicit finite-size and mechanism audits.

Not claimed here:

- a final thermodynamic pinball phase;
- a complete phase diagram;
- NQS superiority over ED/QMC/tensor-network methods;
- raw unpublished result tables or private experiment logs.

## 5. Repository Layout

```text
docs/
  triangular_tv_benchmark.md       nu=1/3 triangular t-V benchmark logic
  moire_pinball_benchmark.md       nu=2/3 moire t-V1-V2-V3 benchmark logic
  public_ed_snapshot.md            small public ED screening snapshot
  finite_size_claim_boundary.md    what can and cannot be claimed
  nqs_ansatz_notes.md              public ansatz design notes
  application_project_summary.md   Chinese application-ready project description
src/triangular_moire_public/
  charge_features.py               lightweight feature helpers
examples/
  charge_feature_demo.py           minimal demo
```

## 6. Notes for Prospective Advisors

The most useful entry points are:

- [public ED snapshot](docs/public_ed_snapshot.md): a small source-backed table from the moire pinball-candidate screening line;
- [finite-size claim boundary](docs/finite_size_claim_boundary.md): why I call the signal a ridge candidate, not a finished phase claim;
- [triangular t-V benchmark](docs/triangular_tv_benchmark.md): the `nu=1/3` generalized-Wigner-crystal sanity line;
- [moire benchmark](docs/moire_pinball_benchmark.md): the `nu=2/3` extended Hubbard / pinball-like candidate line.

This repository is meant to show how I move from ED screening to NQS benchmark design. It deliberately does not publish raw run trees or ongoing private experiment logs.
