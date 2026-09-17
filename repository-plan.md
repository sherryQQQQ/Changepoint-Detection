# Repository and visualization plan

Suggested repository name: changepoints-regimes-risk.

## Present deliverables

~~~text
README.md                   Public entry point and reading map
review.md                   English review with the requested 15 sections
references.md               Annotated literature and operational sources
references.bib              BibTeX records
sources.json                Machine-readable reference metadata
search-protocol.md          Search, screening and evidence limitations
experiment-protocol.md      Synthetic and finance experiment specifications
repository-plan.md          This roadmap
verify_review.py            Small algebra and document-consistency audit
survey.zh-CN.md              Earlier Chinese overview, retained for reference
benchmark-plan.md            Earlier Chinese experiment sketch, superseded
~~~

## Proposed additions after implementation

~~~text
configs/
  synthetic.yaml
  vix.yaml
src/risk_monitoring/
  data.py
  bocpd.py
  cusum.py
  segmentation.py
  latent_states.py
  metrics.py
scripts/
  run_synthetic.py
  fetch_vix.py
  run_finance.py
  make_figures.py
tests/
  test_posterior_and_updates.py
  test_segmentation_optimum.py
  test_no_future_leakage.py
  test_event_matching.py
data/
  README.md
  manifests/
results/
  metrics/
  figures/
notebooks/
  01_concepts.ipynb
  02_synthetic_results.ipynb
  03_finance_case_study.ipynb
pyproject.toml
<resolved dependency lock>
~~~

The paths in this second tree are proposals, not existing runnable artifacts. Add a license appropriate for original text/code when publishing; third-party paper and data rights remain separate.

## Suggested README sections

Purpose; what is and is not a regime; reading map; key distinctions; evidence/search status; quick start once runnable code exists; experiment information sets; results with uncertainty once measured; failure cases; data provenance; citation/contribution guidance; limitations.

## Figures to create

| Figure | Panels / encoding | What it should teach |
|---|---|---|
| Boundaries versus reusable states | Same low–high–low signal with three segment labels and two state labels | Boundary count and state count differ |
| BOCPD posterior heatmap | Run length vs time, predictive score and separate alarm trace | Uncertainty and time-indexing; show the constant reset-mass property |
| Prior sensitivity | Grid of expected duration and prior scale with delay/miss/false-alert metrics | Hazard cannot repair all likelihood misspecification |
| Penalty path | Boundary locations across log penalty and objective/segment count | Sensitivity and over/under-segmentation |
| Filtering versus smoothing | HMM probabilities using identical fixed parameters | Future information changes retrospective interpretation |
| Detection tradeoff | Delay versus null alert rate; include detection fraction | A single F1 score is insufficient |
| Frozen marks, rising exposure risk | Latent simulated price, recorded price, depth, quote age and observed variance | Quiet measurements can coexist with deteriorating observability |
| Finance event timeline | Log VIX, causal probabilities, alerts, descriptive event annotations | No backdated signals; events are not perfect labels |

Use consistent state colors after explicit label alignment. Shade unavailable observations distinctly from low values. Distinguish event date, estimated boundary date and alarm date. Plot Monte Carlo uncertainty for simulations; do not use smoothed probabilities on figures titled “real time.”

## Monitoring architecture (proposed)

~~~mermaid
flowchart TD
    A[Timestamped market and system observations] --> B[Freshness and market-status checks]
    B --> C[Valid causal features]
    B --> D[Data-quality or market-access alert]
    C --> E[Change detector]
    C --> F[Recurring-state filter]
    E --> G[Calibrated evidence and uncertainty]
    F --> G
    G --> H[Risk decision with exposure and execution constraints]
    D --> H
    H --> I[Logged action and later evaluation]
~~~

This diagram is a repository design recommendation, not a validated trading or risk-control system.
