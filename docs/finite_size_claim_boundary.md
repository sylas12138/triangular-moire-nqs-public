# Finite-Size Claim Boundary

This document explains why the public repository uses cautious language such as `ridge candidate` and `pinball-like candidate`.

## What Can Be Said

For the `nu=2/3` moire `t-V1-V2-V3` line, the finite-cluster ED scan found a ridge where:

- `S_c(K)` is enhanced relative to liquid controls;
- three-sublattice imbalance `m_3s` is enhanced;
- the charge gap is larger than in nearby control points;
- kinetic energy per site remains finite;
- shape checks did not immediately erase the signal.

That is enough to motivate an NQS benchmark target.

It is not enough to claim a thermodynamic pinball phase.

## Why Not Call It a Phase?

There are several reasons.

First, the strongest evidence is still finite-cluster ED. Finite clusters can show robust-looking ridges that move, weaken, or disappear with system size, boundary condition, or aspect ratio.

Second, the screening score was designed for ranking candidates. It is not an order parameter and not a phase diagnostic.

Third, a pinball interpretation needs more than charge modulation. It should show a stable pattern where one sublattice is relatively pinned while the remaining network keeps coherent mobile channels. The current public snapshot does not close that mechanism.

Fourth, ED and NQS must agree before the NQS result can be used for larger clusters. If NQS fails on small ED-sized clusters, the method is not yet a trustworthy scaling tool.

## Working Vocabulary

I use the following vocabulary deliberately:

- `charge-order ridge`: finite-cluster enhancement in charge diagnostics;
- `partially itinerant charge-order candidate`: charge modulation plus finite kinetic energy;
- `pinball-like candidate`: qualitative similarity to a pinball picture, still awaiting mechanism closure;
- `pinball phase`: reserved for a much stronger thermodynamic and mechanism claim.

## What Would Strengthen the Claim

The claim would become stronger with:

- larger ED or alternative exact checks where possible;
- twist and boundary-condition audits;
- consistent bond-resolved kinetic channels;
- NQS reproduction of ED on small clusters;
- strict replay of sampled VMC on larger clusters;
- finite-size trend rather than one cluster size.

Until then, this repository presents the moire line as a benchmark and screening problem, not as a completed phase discovery.
