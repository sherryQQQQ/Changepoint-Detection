# Reproducible experiments: design, not results

This document proposes a small Python benchmark and a finance experiment. Code, dependency locks, downloaded data and numerical results are **not yet included**. It supersedes the earlier Chinese benchmark sketch.

## 1. Shared synthetic benchmark

### Research questions

Does uncertainty over recent boundaries help online adaptation? When does a recurring-state model benefit from parameter sharing? How do detectors behave when changes affect variance rather than mean, or when observations become stale?

Use exactly the same generated observations for BOCPD, PELT, CUSUM and HMM. Preserve each method's legitimate information set. A shared dataset does not make their objectives interchangeable.

### Data-generating cases

For each case use T=2,000 and 50 test seeds (1000–1049). Separate training/calibration seeds (0–99) from test seeds. Boundary convention: 400 means the old segment ends at observation 400.

| Case | Specification | Truth and target |
|---|---|---|
| Null | iid N(0,1) | No change; measure false alerts and spurious segments |
| Recurrent mean | Equal 400-point blocks with means 0,2,0,2,0; SD 1 | Four boundaries and two reusable states |
| Novel mean | Equal blocks with means 0,1,2,3,4; SD 1 | Four boundaries; a fixed two-state model is misspecified |
| Recurrent variance | Zero mean; SDs 1,3,1,3,1 | Four variance boundaries and two states |
| Markov recurrence | Means 0,2; SD 1; transition diagonal 0.98 | Random state durations; each actual state switch is a boundary |
| Dependence change | Stationary-unit-variance AR(1), phi changes 0 to 0.7 halfway, innovation SD sqrt(1-phi²) | Dependence target; marginal mean/variance detectors should not be expected to succeed |
| Contamination | Null plus independent 1% signed impulses of size 8 | Anomalies, not persistent regime changes |
| Gradual drift | Mean increases linearly from 0 to 2; SD 1 | No uniquely defined abrupt boundary |
| Stale-price stress | Latent random-walk increments change SD 1 to 3 at t=800; recorded price frozen at t=800–1000, then refreshed | Distinguish latent risk, observable freeze and reopening jump |

For AR(1), discard a burn-in and generate each step with the specified current coefficient. For stale stress, distribute the latent path and observation mask in separate truth files: detectors see only recorded observations plus explicitly permitted quality flags. Do not call delay to an unobservable latent event a pure statistical failure.

### Implementations to build

Suggested libraries: NumPy/SciPy, pandas, matplotlib, ruptures and hmmlearn, with exact versions locked after implementation is tested. Package choices are a development proposal, not a claim that installed versions/API calls have been verified.

| Method | Mean case | Variance case | Outputs to save |
|---|---|---|---|
| BOCPD | Normal–Inverse-Gamma predictive, exact support for baseline | Same model allowing mean/variance changes; also a fixed-zero-mean scale variant | Full run-length posterior, predictive density, recent-run score, alarms |
| PELT | SSE cost with documented units | Gaussian scale cost with minimum segment size and variance floor | Boundary list, objective, candidate-grid settings |
| CUSUM | Separate upward/downward Gaussian mean alternatives | Upward/downward Gaussian variance alternatives | Score paths, crossing times, reset states |
| HMM | Gaussian emissions with switching means | State-specific variance | Historical filtered probabilities, offline smoothed probabilities in a separate file, likelihood and fit diagnostics |

For known-zero-mean variance monitoring, use the log-likelihood increment

$$
\ell_t=\log(\sigma_0/\sigma_1)
+\frac{y_t^2}{2}\left(\sigma_0^{-2}-\sigma_1^{-2}\right).
$$

State which parameters are oracle-known versus estimated. The main benchmark estimates from separate training data; an oracle sensitivity panel may use true parameters but must be labeled. Do not quietly give CUSUM the exact test change size.

### Tuning and alarm definitions

- BOCPD: L=1/h in {50,100,250,500,1000}; kappa0 in {0.01,0.1,1}; alpha0 in {2,5}, with beta0 tied to training scale. Validate posterior predictive behavior. Use w=10 and recent-run score sum of p(r_t=r) for r=1..w under the review's indexing. Suppress the first 50 observations and impose a 20-observation cooldown. Tune score threshold without test labels. Report sensitivity to w and cooldown.
- PELT: training-standardized SSE penalties c log(T), c in {0.5,1,2,4,8,16}, explicitly treated as an empirical grid rather than a universal BIC; minimum length in {10,20,50}; full-resolution split grid for the baseline. Calibrate scale-cost penalties separately.
- CUSUM: mean-shift targets {0.5,1,2} training SDs; variance ratios {1.5,2,3}. Jointly calibrate both directions to the same **combined** alert budget. Reset the statistic to zero after alarm; keep the training baseline fixed in the main experiment.
- HMM: M in {1,2,3,4}, 10 training initializations, prespecified variance floor. Choose on separate chronological validation predictive score and document failed fits. Match state identities across refits using fitted parameters, never future truth. For a live transition alarm, require an alternative state's filtered probability above a calibrated threshold for 5 observations; do not compare an arbitrary state index across refits.

Use a finite-horizon primary null target, for example 5% probability of at least one alert over 2,000 post-warmup observations. This is a **design choice**, not an estimated average run length. Tune on an independent bank of at least 500 null sequences with prespecified dependence variants; report a binomial uncertainty interval and unattained targets. Keep warmup/cooldown fixed across tuning. If also reporting ARL, use long simulations and handle right-censoring explicitly; do not invert the finite-horizon probability to claim an ARL.

### Separate evaluation tracks

**Track A — retrospective boundaries.** Full-sample PELT, offline HMM decoding and archived BOCPD/online alarm outputs can all be visualized. For causal detectors, save both alert time and estimated boundary; do not backdate the alert. Apply maximum-cardinality one-to-one matching within ±10 observations, then minimize total localization error among matched pairs; repeat with ±5 and ±20. Report precision, recall, F1, matched location error and unmatched counts. Do not compute boundary accuracy for gradual drift.

**Track B — online alerting.** Compare BOCPD, CUSUM and historically fitted HMM at calibrated null alert budgets. Offline PELT is explicitly excluded from a live-delay ranking. An optional PELT-prefix variant reruns every 20 observations and requires a boundary to persist over two runs before alerting; measure computation and the incurred confirmation delay, and calibrate it as a separate procedure.

Match each true event to at most one alarm in the following prespecified 100-observation detection window, truncated at the next event. Report misses, pre-change alerts, duplicate alert burden and delay conditional on detection. Report the detection fraction alongside conditional delay so silent detectors cannot look fast by dropping misses.

**Track C — prediction and state recovery.** Compare prequential predictive log score to static and rolling Gaussian baselines. PELT needs an explicit causal forecasting wrapper before it enters this track. State ARI applies only to models producing reusable state labels and cases with that truth. Report fit time, update latency, memory, convergence failures and sensitivity across seeds, not just average F1.

Use paired differences across common test seeds with Monte Carlo uncertainty. Do not report test-set winners until all tuning choices are frozen.

### Minimum correctness checks for future code

1. BOCPD probabilities normalize; constant-hazard reset mass matches h under the documented convention; log-space calculations remain finite on stress inputs.
2. NIG sequential updates equal batch sufficient-statistic updates; predictive scale is distinguished from variance.
3. PELT agrees with exhaustive enumeration or unpruned DP on short sequences under identical constraints/costs.
4. Online outputs for a prefix are unchanged when future observations are appended.
5. Filtering and smoothing are separate; state-label permutations do not change label-invariant scores.
6. Matching never assigns one alarm to multiple truth boundaries.
7. Missing/stale observations and nonpositive futures prices follow explicit transformation policies.

These checks concern the future benchmark; no completed benchmark run is claimed. A separate small algebra audit accompanies the review.

## 2. Finance-oriented experiment

### Public-data route: VIX monitoring

Use [Cboe's historical VIX data](https://www.cboe.com/tradable_products/vix/vix_historical_data) over 2004-01-01 through 2025-12-31. Record source URL, retrieval timestamp, SHA-256, date range and applicable data-use terms. A live download can later change; keep a manifest and do not claim identical reproduction without an identical input snapshot. VIX is an implied-volatility index, not realized volatility and not an investable futures return.

Precommit training 2004–2014, validation 2015–2018, test 2019–2025. Begin with log VIX after positivity checks. Compare:

1. Raw log-level modeling with a dependence-aware likelihood or switching AR.
2. A training-fitted AR baseline and monitoring of its one-step innovations.
3. An expanding historical refit variant, scheduled monthly, with its own calibration.

The variants target different changes. An adaptive baseline may absorb a level shift, so do not equate all detected boundaries. Nontrading dates are absent, not forward-filled. A signal using today's close becomes available only after that observation's release.

Use PELT retrospectively, BOCPD/CUSUM for sequential innovation monitoring, and a historically fitted HMM or switching AR for recurring dynamics. Report causal predictive scores, alert frequency by year, sensitivity and alignment with externally recorded events **as descriptive case studies**. Crisis dates are not objective CPD ground truth and must not choose thresholds. Daily data cannot validate millisecond latency or order-book observability.

For a VaR extension, add a properly sourced return/loss series and an independently specified forecasting model. VIX alone does not supply the loss observations needed to backtest portfolio VaR.

### Optional futures extension

Use licensed contract-level intraday prices and quotes for one liquid futures family. Required fields: contract identifier, exchange and receipt timestamps, trade price/size, executable best bid/ask and depth, session status, limit/halt flags, expiry and roll metadata. Save exactly which fields existed at each decision time.

Analyze fixed contracts first; evaluate a continuous series only with a documented causal roll rule. Keep roll/expiry/session changes as annotations. For contracts that may trade nonpositive, use dollar P&L or a defensible alternative rather than silently dropping observations that invalidate logs.

Compare returns-only detection with returns-plus-spread/depth/quote-age inputs during ordinary and stressed windows. Add controlled stale-feed and empty-book simulations, explicitly distinguished from observed historical events. Evaluate time to operational escalation, alert burden and predictive deterioration; do not claim trading profitability from regime separation.

Data availability limits this extension: public daily settlements cannot establish intraday liquidity depletion. The [May 6 report](https://www.sec.gov/news/studies/2010/marketevents-report.pdf) and [WTI report](https://www.cftc.gov/media/5296/InterimStaffReportNYMEX_WTICrudeOil/download) provide case-study context, not the required tick dataset.
