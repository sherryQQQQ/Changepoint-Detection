# Change-Point Detection and Regime-Switching for Time-Series Risk Monitoring

A practical literature review connecting structural breaks, sequential detection, recurring latent states and quantitative risk.

**Read the [full English review](review.md).** It follows 15 sections, from terminology and mathematical formulations to financial failure modes and method selection.

**Status:** literature review and experiment design completed; benchmark implementation and empirical results are not included. Literature search cutoff: 2026-09-16. Editorial checks: 2026-09-18. The search is bounded and documented, not an exhaustive database review.

## What this repository explains

- Why a change point, structural break, regime shift and latent regime are different objects.
- BOCPD run-length inference, hazard and observation priors, conjugate updates and alarm conventions.
- PELT, dynamic programming and binary segmentation: objectives, computational conditions and penalties.
- CUSUM, Page–Hinkley, HMMs, Markov switching, HSMMs, threshold and smooth-transition models.
- Kernel, robust Bayesian and representation-learning approaches.
- Why stale marks, empty books and binding price limits can make observed volatility fall while economic risk remains high.

## Reading map

| File | Purpose |
|---|---|
| [Review](review.md) | Main exposition, comparison table, risk applications and interview takeaways |
| [Annotated references](references.md) | 34 research/technical sources and 4 official sources; contributions and supporting sections |
| [BibTeX](references.bib) / [source records](sources.json) | Reusable citations and structured metadata |
| [Search protocol](search-protocol.md) | Queries, selection decisions and evidence limitations |
| [Experiment protocol](experiment-protocol.md) | Shared synthetic benchmark; VIX experiment; futures extension |
| [Repository plan](repository-plan.md) | Future Python layout, README sections and eight figure specifications |
| [Verification script](verify_review.py) | Selected algebra and local document checks; not a benchmark |
| [Earlier Chinese overview](survey.zh-CN.md) | Shorter background draft; the English review is the expanded version |

## Three distinctions to keep in view

**Segmentation versus state reuse.** Low–high–low behavior can have two boundaries, three chronological segments and only two recurring states.

**Historical reconstruction versus live decisions.** An offline partition or smoothed state path uses information a live system did not have. Parameter fitting and feature construction must also respect the clock.

**Measured variability versus economic exposure.** Repeated stale prices can produce zero observed returns without making liquidation safer. Data-quality and execution conditions belong in the monitoring design.

## Suggested reading route

Start with Truong et al. (2020) for offline taxonomy, Casini–Perron (2018) for structural inference, Adams–MacKay (2007) for BOCPD, Killick et al. (2012) for PELT, Xie et al. (2021) for sequential objectives, and Rabiner (1989)/Hamilton (1989) for latent states. Then read Ang–Timmermann (2012) for finance and Xu et al. (2025) for deep-learning coverage. Links and publication details are in the [bibliography](references.md).

## Proposed experiments

The design compares BOCPD, PELT, CUSUM and HMM on identical synthetic observations, while separating retrospective boundaries, causal alarms and prediction. Scenarios include mean/variance shifts, recurrence, novel states, outliers, dependence changes and frozen observations.

A second design uses official daily VIX history with chronological training/validation/test periods. A contract-level futures extension requires appropriate intraday data and market-status fields. No performance ranking or trading-profit claim is made.

## Local verification

Run the following from this directory with Python 3; it uses only the standard library:

~~~bash
python3 verify_review.py
~~~

The script checks reference consistency, local links, the 15-section structure, conjugate-update identities, the constant-hazard reset property, and a small dynamic-programming/brute-force agreement check. It does not validate all methods, remote link availability or empirical risk effectiveness.

## Scope and contributions

This is an educational research synthesis. Mathematical guarantees remain conditional on their original assumptions. Proposed tuning grids and operating rules are clearly marked as design choices. For new literature, record the primary source, exact version, assumptions, information set, computational conditions and practical failure modes.

Keep benchmark results separate from proposals; record data provenance, causal fitting windows and uncertainty before adding results. Third-party papers and datasets retain their own rights.
