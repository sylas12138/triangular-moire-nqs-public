# Public ED Snapshot: Moire Pinball-Candidate Screening

This page gives a small public snapshot of the `nu=2/3` triangular moire `t-V1-V2-V3` ED screening line.

The goal is not to claim a thermodynamic pinball phase. The goal is to show the kind of finite-cluster evidence used to select NQS benchmark targets.

## Screening Setup

The private workspace scanned a finite triangular extended Hubbard model with interaction parameters `V1`, `V2`, and `V3`. The public snapshot reports a small subset of derived ED diagnostics:

- energy per site `E/N`;
- charge structure factor `S_c(K)`;
- three-sublattice density imbalance `m_3s`;
- kinetic energy per site `K/N`;
- a screening score used only for ranking candidates.

The score is not a phase diagnostic. It is a heuristic used to find rows where charge modulation is visible while kinetic energy remains finite.

## Top Public Screening Rows

These rows are copied from a public-safe analysis summary. They are enough to show the benchmark target without releasing the full private run tree.

| `V1` | `V2` | `V3` | `E/N` | `S_c(K)` | `m_3s` | `K/N` | screening score | public label |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 3.000 | 0.000 | 1.000 | 3.953357 | 1.048116 | 0.600181 | -0.464893 | 0.487262 | metal_candidate |
| 3.000 | 0.000 | 0.750 | 3.693171 | 1.030894 | 0.594984 | -0.472458 | 0.487054 | metal_candidate |
| 3.250 | 0.000 | 0.750 | 3.974634 | 1.060937 | 0.604773 | -0.457932 | 0.485837 | metal_candidate |
| 3.250 | 0.100 | 1.000 | 4.392112 | 1.049658 | 0.600420 | -0.462719 | 0.485697 | metal_candidate |
| 3.250 | 0.000 | 0.500 | 3.714200 | 1.043046 | 0.599394 | -0.465377 | 0.485409 | metal_candidate |
| 3.250 | 0.100 | 0.750 | 4.131921 | 1.031887 | 0.595037 | -0.470396 | 0.485395 | metal_candidate |

The label `metal_candidate` is intentionally cautious. It means the finite-cluster row keeps finite kinetic energy while showing enhanced charge modulation. It does not mean the thermodynamic state is a metal, and it does not prove a pinball liquid.

## Ridge vs Control Summary

| group | `n` | charge gap | `S_c(K)` | `m_3s` | `K/N` |
|---|---:|---:|---:|---:|---:|
| ridge_top | 6 | 1.086 - 1.457 | 1.031 - 1.061 | 0.595 - 0.605 | -0.472 - -0.458 |
| liquid_control | 3 | 0.652 - 0.783 | 0.264 - 0.276 | 0.282 - 0.289 | -0.661 - -0.644 |

The public interpretation is:

- the high-score ridge has stronger `S_c(K)` and `m_3s` than the liquid controls;
- the ridge retains finite kinetic energy;
- finite-size shape checks were used in the private workspace before choosing the row as a target;
- the result is still a candidate region, not a phase claim.

## Why This Matters for NQS

These ED rows define a controlled target for NQS/VMC:

1. On small clusters, can NQS reproduce the ED energy and charge diagnostics?
2. Does strict replay preserve the charge pattern found during training?
3. Does the ansatz collapse to a frozen charge crystal, or can it retain kinetic channels?
4. Does the same workflow distinguish a real finite-cluster signal from a branch or boundary artifact?

This is the reason I use the moire line as a benchmark: it forces the NQS method to handle charge order and itinerancy at the same time.
