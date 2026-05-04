# Research Roadmap

This roadmap explains how I would continue the triangular / moire benchmark line.

## 1. Track A: Triangular `nu=1/3` `t-V`

The `nu=1/3` nearest-neighbor triangular `t-V` model is a sanity benchmark for charge order.

The next step is not to make the ansatz larger first. The next step is to close a small, exact-sum benchmark:

- ED energy and charge diagnostics;
- exact-sum NQS where possible;
- sampled VMC replay;
- branch-locking checks;
- comparison between train-best and replay values.

This line is useful because the expected charge-order pattern is simple enough to diagnose, but still hard enough to expose sampler and branch problems.

## 2. Track B: Moire `nu=2/3` `t-V1-V2-V3`

The moire line should proceed in three stages.

First, keep the ED screening table conservative. The current public snapshot only supports a finite-cluster ridge candidate: enhanced `S_c(K)` and `m_3s`, with finite kinetic energy.

Second, reproduce the selected ridge and control points with exact-sum NQS on smaller clusters. This is the key gate. If NQS cannot reproduce ED where ED is available, there is no reason to trust sampled VMC on larger clusters.

Third, if the small benchmark closes, move to sampled VMC on larger clusters with strict replay. The report should separate:

- train-best energy;
- strict replay energy;
- charge structure factor;
- three-sublattice imbalance;
- kinetic channels;
- boundary/twist checks;
- claim label.

## 3. What Would Count as Progress

Good progress would be:

- NQS reproduces ED on several small ridge/control points;
- replay does not destroy the charge diagnostics;
- kinetic channels remain finite rather than collapsing into a frozen crystal;
- ridge/control separation survives shape or boundary checks;
- the public claim remains finite-size cautious.

Bad progress would be:

- only showing a lower training energy;
- reporting a pinball phase from one cluster;
- ignoring a failed control point;
- using a screening score as an order parameter.

## 4. Why This Line Is Useful

This project is a bridge between simple charge-order benchmarks and harder moire-inspired problems.

It lets me test whether NQS can handle a situation where the desired state is neither a simple liquid nor a fully frozen charge crystal. That is exactly the kind of place where neural wave functions may be useful, but only if the benchmark is strict.
