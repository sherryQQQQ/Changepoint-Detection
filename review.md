# Change-Point Detection and Regime-Switching for Time-Series Risk Monitoring

**A structured literature review and practical research guide.** Search cutoff: 2026-09-16. Intended audience: statistics/ML practitioners and quantitative finance/risk interview candidates.

This review uses a documented, systematic search-and-screening procedure, with a scoped narrative synthesis rather than a meta-analysis. It is not an exhaustive database review or a claim of independent replication. The [search protocol](search-protocol.md) records coverage, source-access limitations and selection decisions. Proposed experiments and operational recommendations are explicitly distinguished from published results.

## 1. Introduction

Risk monitoring asks several different questions: has a distribution changed, has a forecasting relationship broken, which recurring environment is active, and should an alert trigger action now? A useful model must match the question, the available information and the consequences of a false alarm. The econometric, segmentation and sequential-detection literatures emphasize different parts of this problem. [Structural-break review](https://arxiv.org/abs/1805.03807); [offline CPD review](https://doi.org/10.1016/j.sigpro.2019.107299); [sequential review](https://arxiv.org/abs/2104.04186).

The organizing principle of this review is **boundaries versus reusable states versus actions**. A boundary need not introduce a previously unseen state; a latent state need not indicate a new structural break; a model transition need not warrant the same risk action as a failed market-data feed.

Notation: \(T\) observations, \(K\) change points, \(M\) latent states, \(d\) features, and \(\mathcal F_t\) information actually available by time \(t\). A boundary \(\tau\) is the last observation of the old segment; the new segment starts at \(\tau+1\). Computational costs below assume fixed feature dimension and constant-time segment-cost evaluation unless otherwise stated.

## 2. Terminology: Change Points vs Structural Breaks vs Regimes

| Term | Meaning used here | What it does not establish |
|---|---|---|
| Change point | Time at which a specified data-generating property changes | A cause, a recurring state identity, or necessarily a large loss |
| Structural break | Instability of model parameters or relationships, such as regression coefficients or an error covariance | That every visible price jump changes the economic relationship |
| Regime shift | A transition between substantively distinct patterns; a modeling or domain description requiring an operational definition | A unique statistical estimand without specifying the model |
| Latent regime | An unobserved state with state-specific behavior, inferred probabilistically | An independently observed economic fact or a guaranteed future pattern |

These are working definitions consistent with the different emphases of [Casini–Perron](https://arxiv.org/abs/1805.03807) and [Hamilton](https://www.nber.org/papers/w21863). Terminology varies across fields.

Consider low–high–low variance. CPD can identify two boundaries while fitting three independent segments. A two-state HMM can share parameters between the first and third periods. A one-period outlier may be an anomaly without persistent change. A regression slope can break while the unconditional mean barely changes. None of these observations alone identifies a causal mechanism.

A homogeneous HMM can switch states while its transition matrix and emissions remain fixed: its **state** changes, but the parameters of the overall model do not. Conversely, its transition matrix can itself suffer a structural break. This distinction is central to model-risk monitoring.

Offline methods use \(y_{1:T}\); online procedures at \(t\) use only \(\mathcal F_t\). Running an offline algorithm repeatedly on prefixes does not supply sequential false-alarm guarantees. Likewise, an HMM with parameters estimated using the full sample leaks future information even if its reported probabilities are called “filtered.”

## 3. Classical Change-Point Detection

### 3.1 Problem classes and single-change scans

The basic piecewise model has \(y_t\sim F_j\) for \(\tau_{j-1}<t\leq\tau_j\). Dependence must either be modeled within segments or explicitly addressed in calibration. Parametric methods restrict \(F_j\), for example to Gaussian observations or linear regressions. Nonparametric methods use ranks, distances or kernels; they still require assumptions about sampling, dependence and separability. [Truong et al.](https://doi.org/10.1016/j.sigpro.2019.107299).

For a single mean change, a standardized contrast is

$$
Z(k)=\frac{1}{\hat\sigma}
\sqrt{\frac{k(T-k)}{T}}\,
(\bar y_{1:k}-\bar y_{k+1:T}),\qquad
\hat\tau=\arg\max_{m\le k\le T-m}|Z(k)|.
$$

Here \(m\) excludes poorly identified edge splits. Testing the maximum requires calibration for the search over \(k\); a fixed-location normal threshold is not generally valid. This is an **offline CUSUM contrast**, distinct from the recursive one-sided monitoring procedure in Section 6. The formula illustrates a mean target: it is not a general detector of all distributional changes.

**Profile:** offline; explicit boundary, no recurring-state identity. A cumulative-sum implementation costs \(O(T)\). Choose \(m\), noise/long-run variance estimation and a scan-level threshold. Its simplicity is attractive for a well-defined alternative; serial correlation, outliers, gradual drift and multiple offsetting changes can undermine it. Structural-break inference and calibration issues are reviewed by [Casini–Perron](https://arxiv.org/abs/1805.03807).

### 3.2 Multiple breaks in regression

A partial structural-change model is

$$
y_t=x_t^\top\beta+z_t^\top\delta_j+\varepsilon_t,
\quad \tau_{j-1}<t\leq\tau_j.
$$

\(\beta\) stays fixed; \(\delta_j\) can change. Bai–Perron develop estimation and tests for unknown multiple breaks; their practical companion discusses computation and break-date confidence intervals. [Bai–Perron 1998](https://doi.org/10.2307/2998540); [2003](https://doi.org/10.1002/jae.659).

**Profile:** principally offline inference; boundaries and segment coefficients, not a latent recurring-state dictionary. Specify changing coefficients, maximum breaks, trimming/minimum segment size and the error model. Assumptions about identification, regressor behavior, break separation and disturbance dependence matter for inference. Conditional on computable segment fits, dynamic programming avoids exhaustive enumeration; fitting and covariance estimation add cost. Collinearity, short segments, endogenous relationships, unit roots and incorrect dependence corrections can invalidate an apparently precise result. Do not present a generic mean-segmentation package as a full Bai–Perron implementation.

### 3.3 Binary Segmentation

On interval \([a,b]\), select the largest improvement

$$
\Delta(k)=C(a,b)-C(a,k)-C(k+1,b).
$$

Split at its maximizer if the improvement exceeds a stopping threshold, then recurse. This greedy method produces multiple boundaries without globally optimizing the final partition. Choose the cost, threshold or target number of changes, minimum segment length and allowed split grid. Balanced splits give \(O(T\log T)\); highly unbalanced recursion can require \(O(T^2)\). [Offline-method taxonomy](https://doi.org/10.1016/j.sigpro.2019.107299).

Its practical strength is a transparent, inexpensive baseline. Its weakness is irreversible early decisions: nearby changes can mask each other, especially an up-shift followed quickly by a down-shift. Wild Binary Segmentation addresses isolation using random subintervals, introducing their number and sampling scheme as additional choices. [Fryzlewicz 2014](https://arxiv.org/abs/1411.0858).

## 4. Bayesian Online Change-Point Detection

### 4.1 Run-length inference and indexing

BOCPD maintains \(w_t(r)=p(r_t=r\mid y_{1:t})\), rather than committing immediately to a single boundary. In the basic model, observations are conditionally independent within a segment and each new segment draws fresh parameters from a common prior. It produces boundary uncertainty, not automatically reusable economic-state labels. [Adams–MacKay](https://arxiv.org/abs/0710.3742).

Use the original **reset-after-observation** recursion. Define the segment predictive density
\(q_t(r)=p(y_t\mid r_{t-1}=r,y_{1:t-1})\). With normalized previous weights:

$$
\tilde w_t(r+1)=w_{t-1}(r)q_t(r)[1-H_t(r+1)],
$$

$$
\tilde w_t(0)=\sum_r w_{t-1}(r)q_t(r)H_t(r+1),\qquad
w_t(r)=\frac{\tilde w_t(r)}{\sum_s\tilde w_t(s)}.
$$

Initialize \(w_0(0)=1\) for a segment starting at the sample boundary. The reset branch has an empty segment for predicting the next observation; growth branches update sufficient statistics with \(y_t\). These details follow the [original algorithm](https://www.cs.princeton.edu/~rpa/pubs/adams2007changepoint.pdf).

**Algebraic implication, derived here:** if \(H_t(r+1)=h\) for all \(r\), the denominator is \(\sum_r w_{t-1}(r)q_t(r)\), so \(w_t(0)=h\). The observation changes the distribution over positive run lengths, not this particular reset mass. Alarm rules based only on \(w_t(0)>c\) are therefore uninformative under this convention.

One possible project-specific score is \(\sum_{r=1}^{w}w_t(r)\), excluding the constant reset mass and suppressing startup alerts. Its window, threshold and cooldown require calibration. It is a recent-boundary score, not a universal BOCPD test. Alternatively, use a different explicitly specified generative convention in which the current observation is generated by the new segment, or infer past boundaries with a fixed delay. Do not mix those recursions with the equations above.

### 4.2 Hazard, expected duration and sensitivity

For segment duration \(D\geq1\),

$$
H(a)=\Pr(D=a\mid D\geq a).
$$

Constant \(h\) implies \(\Pr(D=d)=h(1-h)^{d-1}\) and \(E[D]=1/h\). Age-dependent hazards encode duration effects; calendar/covariate-dependent \(H_t(a)\) can encode varying transition risk using information already available at \(t\). Learning hazard parameters is possible but creates another estimation problem. [Adaptive sequential Bayesian CPD](https://mlg.eng.cam.ac.uk/pub/pdf/TurSaaRas09.pdf).

**Calibration protocol proposed here:** define the sampling clock first. An expected run of 250 daily observations and 250 trades have very different meanings. Start from historical segment-duration evidence and operationally meaningful persistence, not a convenient default. Compare \(L=E[D]\) on a prespecified grid, for example \(\{50,100,250,500,1000\}\) observations. Evaluate predictive log score, alarm rate, detection delay and posterior duration on separate chronological validation data. Repeat after jointly changing the observation prior. These numbers are illustrative grid points, not recommended financial constants.

A larger hazard supplies more prior mass to short runs; the eventual detection effect also depends on predictive fit. A very small hazard can delay recognition, while strong expected persistence can manufacture certainty. If duration depends on age or calendar time, \(1/h\) no longer describes a single global expected duration in general.

### 4.3 Observation priors and an explicit conjugate example

Conjugacy means that a posterior remains in the prior's distributional family. For
\(y\mid\mu,\sigma^2\sim N(\mu,\sigma^2)\), choose

$$
\sigma^2\sim\operatorname{InvGamma}(\alpha,\beta),\qquad
\mu\mid\sigma^2\sim N(m,\sigma^2/\kappa),
$$

where the inverse-gamma density is proportional to
\((\sigma^2)^{-\alpha-1}\exp[-\beta/\sigma^2]\).
For each run hypothesis, after observing \(y\):

$$
\kappa'=\kappa+1,\quad m'=\frac{\kappa m+y}{\kappa'},\quad
\alpha'=\alpha+\frac12,\quad
\beta'=\beta+\frac{\kappa(y-m)^2}{2\kappa'}.
$$

The predictive is Student-\(t\) with degrees of freedom \(2\alpha\), location \(m\), and **scale squared**
\(\beta(\kappa+1)/(\alpha\kappa)\). Scale is not variance. The prior predictive uses the initial hyperparameters; the posterior predictive uses updated ones. [Murphy's Gaussian conjugacy note](https://www.cs.ubc.ca/~murphyk/Papers/bayesGauss.pdf).

**Worked prior elicitation:** suppose a training-only transformation gives a plausible segment standard deviation \(s\). Set a candidate \(\alpha_0>1\) and \(\beta_0=(\alpha_0-1)s^2\), so the prior mean of \(\sigma^2\) is \(s^2\). Choose \(m_0\) from plausible segment means and vary \(\kappa_0\), which controls confidence in that location. Simulate from the resulting prior predictive: are plausible new regimes given appreciable probability? No test-period observations should enter this construction.

An overconcentrated prior can make a genuinely new regime implausible even on the reset branch. An excessively diffuse prior can assign low density to ordinary observations, making resets unattractive. An understated continuation variance can turn individual outliers into apparent boundaries. These are predictive-likelihood effects, so hazard tuning alone cannot repair them.

The Student-\(t\) predictive arising from uncertainty in Gaussian parameters does not guarantee robust detection: with a long well-estimated segment it can become close to Gaussian. Generalized Bayesian alternatives explicitly address outlier influence. [Knoblauch–Jewson–Damoulas](https://arxiv.org/abs/1806.02261); [Altamirano–Briol–Knoblauch](https://arxiv.org/abs/2302.04759).

### 4.4 Cost, capability and extensions

With fixed-size sufficient statistics, retaining all runs costs \(O(t)\) per arrival, \(O(T^2)\) overall and \(O(T)\) current working memory. Storing every posterior row costs \(O(T^2)\). Truncation or a fixed particle budget can reduce work, but the retained support/resampling approximation must be documented. Related exact filtering and resampling methods are developed by [Fearnhead–Liu](https://doi.org/10.1111/j.1467-9868.2007.00601.x).

BOCPD's strengths are online uncertainty and modular predictive models. It detects changes only in properties represented by those models: mean, scale, regression or dependence changes need corresponding likelihoods. Weak changes, gradual drift and unmodeled autocorrelation can produce broad or misleading posteriors. Model-selection and spatio-temporal extensions broaden the within-segment model; robust extensions change the updating criterion. [Knoblauch–Damoulas 2018](https://arxiv.org/abs/1805.05383); [Altamirano et al. 2023](https://proceedings.mlr.press/v202/altamirano23a.html).

## 5. PELT and Optimization-Based Methods

### 5.1 Objective, costs and dynamic programming

For \(0=\tau_0<\cdots<\tau_{K+1}=T\), consider

$$
\min_{K,\tau}\left\{\sum_{j=0}^{K}C(\tau_j+1,\tau_{j+1})+\lambda K\right\}.
$$

For squared-error mean segmentation,
\(C(a,b)=\sum_{t=a}^{b}(y_t-\bar y_{a:b})^2\).
A Gaussian likelihood allowing segment variance gives a different cost; an AR or regression cost targets different changes. PELT is a search method, not a synonym for a mean-change model. [Truong et al.](https://doi.org/10.1016/j.sigpro.2019.107299).

For a fixed number \(q\) of segments,

$$
D(q,t)=\min_s\{D(q-1,s)+C(s+1,t)\}.
$$

The base case is \(D(1,t)=C(1,t)\). Computing up to \(Q\) segments costs \(O(QT^2)\) with constant-time costs, using \(O(QT)\) values/backpointers. Penalized optimal partitioning instead uses

$$
F(t)=\min_{s<t}\{F(s)+C(s+1,t)+\lambda\},\qquad F(0)=-\lambda.
$$

It costs \(O(T^2)\) without pruning. The initialization charges exactly \(K\) penalties. All statements are conditional on allowed segment lengths and split locations; regression fitting or an \(O(T^2)\) cost cache changes total resources. [Bai–Perron computation](https://doi.org/10.1002/jae.659); [PELT](https://doi.org/10.1080/01621459.2012.737745).

**DP profile:** offline boundaries, no latent identities, deterministic conditional on data and tuning. Exact optimization is its strength; expensive search and misspecified costs are its weaknesses. Choose \(Q\) or \(\lambda\), segment cost, minimum length and candidate grid using validation or an appropriately derived information criterion.

### 5.2 Why PELT can prune

Suppose a constant \(c_0\) satisfies, for admissible \(s<t<u\),

$$
C(s+1,t)+C(t+1,u)+c_0\leq C(s+1,u).
$$

If \(F(s)+C(s+1,t)+c_0\geq F(t)\), a future segmentation through \(t\) is no worse than one whose last earlier boundary remains \(s\); \(s\) can be discarded for those future endpoints. This is the PELT dominance condition. Minimum-length constraints require constraint-aware pruning. [Killick et al., Theorem 3.1](https://arxiv.org/pdf/1101.1438).

Expected \(O(T)\) work is established under specific moment, segment-duration and signal/penalty assumptions; it is not a worst-case guarantee, and a penalty growing with \(T\) is not automatically covered by that theorem. Without effective pruning, work is \(O(T^2)\). [Killick et al., Theorem 3.2](https://arxiv.org/pdf/1101.1438).

### 5.3 Penalty selection and failure modes

**Project calibration advice:** on a \(-2\log L\) cost scale, an information-criterion penalty should count the relevant additional parameters and handle breakpoint-model assumptions. Applying “\(\log T\)” directly to raw squared errors ignores their units. Compare a penalty path, report boundary stability, and calibrate against unchanged data with realistic serial dependence. Use a training-only noise scale. A dependence-preserving bootstrap can be useful when its own assumptions are credible.

Smaller \(\lambda\) favors extra segments; larger \(\lambda\) suppresses them. Minimum segment length sets the shortest detectable episode. An outlier can attract a short segment; gradual drift can become a staircase. Variance-fitting likelihoods can degenerate on tiny segments, requiring length/variance constraints. These are modeling and calibration limitations even when optimization is exact.

PELT provides a reproducible retrospective partition and a useful baseline for audit. It does not supply an online stopping rule, a posterior over segmentations, or a stable vocabulary of recurring regimes.

## 6. Sequential Monitoring: CUSUM and Related Methods

### 6.1 Likelihood-ratio CUSUM

For specified pre- and post-change conditional densities, let

$$
\ell_t=\log\frac{f_1(y_t\mid\mathcal F_{t-1})}
{f_0(y_t\mid\mathcal F_{t-1})},\quad
S_t=\max(0,S_{t-1}+\ell_t),\quad
\mathcal T=\inf\{t:S_t\geq b\}.
$$

Evidence accumulates while unfavorable evidence resets the statistic. The scalar recursion needs \(O(1)\) work and memory beyond evaluating the densities. It yields an alarm and an inferred change-start candidate, not recurring state identities. [Page 1954](https://doi.org/10.1093/biomet/41.1-2.100).

Under unit-variance Gaussian monitoring for a positive mean shift \(\delta\), the increment is \(\delta y_t-\delta^2/2\). A variance increase requires a variance likelihood ratio, not the same mean statistic. Design choices are baseline, target change, threshold, direction, initialization and post-alarm reset.

Classical optimality applies to specified statistical criteria and assumptions. Calibrate \(b\) against a false-alarm measure such as \(E_\infty[\mathcal T]\), and report delay and missed detections. Unknown parameters, dependence or repeated refitting alter calibration. [Xie et al.](https://arxiv.org/abs/2104.04186).

### 6.2 Page–Hinkley and sequential likelihood approaches

A concrete Page–Hinkley-style upward-mean monitor is

$$
A_t=A_{t-1}+y_t-\bar y_t-\delta,\qquad
PH_t=A_t-\min_{0\le s\le t}A_s.
$$

Alarm when \(PH_t>b\), after a warmup. Here \(\delta\) is a tolerance and \(\bar y_t\) a running mean. This is an explicitly defined variant: software may instead use forgetting, different mean estimates or two-sided monitoring. Cumulative-sum change-location inference is developed by [Hinkley](https://doi.org/10.1093/biomet/58.3.509).

**Profile:** online, \(O(1)\) scalar updates; simple and interpretable but not a posterior. Select warmup, \(\delta\), \(b\), forgetting if present and reset policy by realistic null simulations. An adapting mean can absorb slow change; outliers can trigger alarms; autocorrelation can inflate false alarms. This variant is not claimed to inherit every optimality property of known-density CUSUM.

An SPRT compares hypotheses specified from a starting point; unknown-onset monitoring needs a change-time treatment. A GLR scan, for example,

$$
G_t=\max_{t-W+1\le k\le t}\sup_\theta
\sum_{i=k}^{t}\log\frac{f_\theta(y_i\mid\mathcal F_{i-1})}
{f_0(y_i\mid\mathcal F_{i-1})},
$$

searches a window of candidate starts. A mixture procedure integrates rather than maximizes over alternatives. Cost is model-specific: with sufficient statistics a windowed scan may cost \(O(W)\) per update; expensive fitting adds more. Select \(W\), parameter restrictions or mixture prior and threshold. Flexibility against unknown shifts brings estimation and multiplicity costs. [Sequential review](https://arxiv.org/abs/2104.04186).

## 7. Hidden Markov and Markov-Switching Models

### 7.1 Latent states and inference

An HMM specifies \(z_t\in\{1,\ldots,M\}\), initial probabilities \(\pi\), transition matrix \(P\), and emissions \(b_j(y_t)=p(y_t\mid z_t=j)\). With fixed parameters,

$$
\alpha_t(j)\propto b_j(y_t)\sum_i\alpha_{t-1}(i)P_{ij}.
$$

Forward filtering uses past/current data. Backward messages combine with forward messages to give full-sample state marginals. Viterbi instead finds the highest-probability **joint path**; it is not the same as choosing the largest marginal at each time. Baum–Welch/EM estimates parameters but can reach local optima. [Rabiner](https://doi.org/10.1109/5.18626).

Inference costs \(O(TM^2)\) for dense transitions, plus emissions. Filtering uses \(O(M)\) state memory; smoothing/decoding typically stores \(O(TM)\). EM adds iteration and initialization factors. For fixed \(M,d\), filtering is practical online, but full-sample parameter estimation and smoothing remain retrospective.

Homogeneous transitions imply

$$
\Pr(D_i=d)=P_{ii}^{d-1}(1-P_{ii}),\qquad
E[D_i]=(1-P_{ii})^{-1}.
$$

Repeated visits reuse emission parameters. This is a model assumption, not proof that “crisis” has one permanent statistical signature.

### 7.2 Markov-switching econometric models

A simple switching AR model is

$$
y_t=c_{z_t}+\sum_{\ell=1}^{p}\phi_{\ell,z_t}y_{t-\ell}
+\sigma_{z_t}\varepsilon_t.
$$

It belongs to the broader hidden-state family but conditions emissions on observed history. Other specifications depend on past hidden states and require state augmentation or approximations; the basic \(O(TM^2)\) statement is not universal for all switching AR/GARCH models. [Hamilton 1989](https://doi.org/10.2307/1912559); [Hamilton 2016](https://www.nber.org/papers/w21863).

Switching ARCH models can combine volatility dynamics within states with transitions across states. This prevents the false choice between “all volatility persistence is GARCH” and “all persistence is a regime.” [Hamilton–Susmel](https://doi.org/10.1016/0304-4076(94)90067-1).

### 7.3 Selection, strengths and model risk

**HMM/MS profile:** explicit latent regimes; changes can be derived from state transitions but require a decoding/alert rule. Choose \(M\), emissions, lag order, covariance restrictions, transition regularization, initialization and fitting window. Compare several small \(M\) values using chronological predictive scores, stability across starts and interpretability. Information criteria are useful diagnostics, but latent-state likelihoods can be nonregular; do not apply naive chi-squared likelihood-ratio reasoning to selecting \(M\). [Hamilton survey](https://www.nber.org/papers/w21863).

Parameter reuse can help when states recur. Gaussian emissions may invent extra states to accommodate heavy tails or outliers; similar emissions make state identity weak; a fixed transition matrix can lag a changing transition mechanism. State labels can permute across fits. High \(P_{ii}\) may reflect real persistence or an overly sticky constraint. A low-variance state is a statistical label, not permission to increase risk. Finance applications are surveyed by [Ang–Timmermann](https://doi.org/10.1146/annurev-financial-110311-101808).

### 7.4 Hidden semi-Markov models

HSMMs specify state-duration distributions explicitly. Typically, a transition between segments changes state while \(p(D_i=d)\) controls residence time. With maximum duration \(D_{\max}\), a common factored explicit-duration recursion costs \(O(T(M^2+MD_{\max}))\); less factored implementations can cost \(O(TM^2D_{\max})\). Emission calculation and duration truncation also matter. [Yu 2010](https://doi.org/10.1016/j.artint.2009.11.011).

**Profile:** latent recurring states and derived boundaries; batch smoothing or online filtering. Choose state count, emission family, duration family/prior and duration cap. It is useful when geometric durations are implausible, but duration and emission misspecification can trade off, sparse visits weaken estimation, and a short cap can force artificial exits. It is more expressive, not automatically more accurate.

## 8. Threshold and Smooth-Transition Models

### 8.1 TAR and SETAR

A two-regime threshold regression is

$$
y_t=x_t^\top\beta_1\,1(q_t\le c)
+x_t^\top\beta_2\,1(q_t>c)+\varepsilon_t.
$$

For SETAR, the threshold variable is a lagged response, such as \(q_t=y_{t-d}\). Membership is determined by an observed variable, not inferred from a hidden Markov chain. A threshold crossing can repeat while model parameters remain unchanged. [Tong–Lim](https://doi.org/10.1111/j.2517-6161.1980.tb01126.x).

**Profile:** batch estimation, causal prediction once the threshold variable is available; observed regimes, not explicit latent regimes or historical break estimates. Specify lag order, delay, threshold variable, candidate thresholds and minimum regime occupancy. A naive grid of \(G\) thresholds with \(p\)-dimensional regressions costs approximately \(O(G(Tp^2+p^3))\); sorting and cumulative sufficient statistics can reduce repeated work.

Its strength is an interpretable rule tied to an observable condition. Select thresholds and delays on chronological training/validation data, using trimming to avoid nearly empty regimes. Failure modes include the wrong threshold variable, little data near the threshold, noisy repeated crossings and using a variable unavailable at decision time. Interpretability does not make the threshold causal.

### 8.2 STAR

A logistic STAR specification is

$$
y_t=x_t^\top\beta_0+x_t^\top\beta_1G(q_t;\gamma,c)+\varepsilon_t,\qquad
G=\frac{1}{1+\exp[-\gamma(q_t-c)]},\quad\gamma>0.
$$

Large \(\gamma\) approximates a sharp threshold; small \(\gamma\) creates weak separation. An exponential transition instead permits behavior varying with distance from a center. The gate is a deterministic weight, not automatically a posterior regime probability. [Teräsvirta 1994](https://doi.org/10.1080/01621459.1994.10476462).

**Profile:** nonlinear batch fitting, inexpensive causal evaluation; smooth observed-condition regimes, no inherent alarm or discrete boundary. Choose transition variable, lags, gate family, center and slope constraints, starts and error model. Each objective evaluation is \(O(Tp)\), but optimizer iterations and conditioning determine total fitting cost. Validate specification and forecast stability rather than maximizing in-sample fit alone.

STAR is attractive when behavior plausibly changes continuously with liquidity or volatility. It fails when the gate extrapolates poorly, \(\gamma\) is weakly identified, or an abrupt unobserved break is forced into a fixed smooth relationship. Smoothness in a covariate is not the same as smooth drift through calendar time.

## 9. Modern Machine-Learning Approaches

### 9.1 Kernel methods

For a positive-semidefinite kernel \(k\), the within-segment feature-space dispersion is

$$
C(a,b)=\sum_{t=a}^{b}k(y_t,y_t)
-\frac{1}{n}\sum_{s,t=a}^{b}k(y_s,y_t),\qquad n=b-a+1.
$$

Changes in kernel mean embeddings can represent distributional differences beyond the original mean. Kernel model selection supplies a principled way to penalize additional segments under stated assumptions. [Arlot–Celisse–Harchaoui](https://jmlr.org/papers/v20/16-155.html).

**Profile:** the cited method is offline CPD, not a recurring-state model. A full Gram matrix costs \(O(T^2)\) kernel evaluations/storage; subsequent fixed-segment DP can cost \(O(QT^2)\). Choose kernel, bandwidth, penalty and minimum segment length. Set bandwidth on training data and examine sensitivity; a median-distance heuristic is a starting candidate, not calibration evidence. High dimension, dependence, poor scaling or inappropriate bandwidth can hide change or promote nuisance variation. A nonparametric representation does not remove finite-sample limitations.

### 9.2 Bayesian extensions

Bayesian does not imply online, conjugate or computationally cheap. The relevant distinctions are the segment model, prior on boundaries/durations, parameter sharing and inference approximation. Spatio-temporal model selection allows different explanations of a segment; generalized-Bayes approaches modify evidence accumulation to resist contamination. [Knoblauch–Damoulas](https://proceedings.mlr.press/v80/knoblauch18a.html); [Knoblauch et al.](https://arxiv.org/abs/1806.02261); [Altamirano et al.](https://proceedings.mlr.press/v202/altamirano23a.html).

**Practical tradeoff:** robustness parameters, model-prior weights and pruning budgets need sensitivity analysis in addition to hazard calibration. A procedure designed to downweight outliers may also react more slowly to the first observations of a true crisis. This is a proposed deployment stress test, not a universal theorem about robust BOCPD.

### 9.3 Deep and representation-learning methods

Two representative mechanisms are:

- **Supervised detection:** train \(g_\phi(y_{a:b})\) on labeled or simulated windows to classify whether a change occurs, then localize or scan. Li et al. study a neural offline approach with theoretical and empirical analysis. [Li et al. 2024](https://doi.org/10.1093/jrsssb/qkae004).
- **Self-supervised representation:** learn \(e_t=f_\phi(y_{t-w+1:t})\) and assess compatibility of adjacent windows. Contrastive predictive coding can turn complex signal changes into differences between embeddings. [Deldari et al. 2021](https://doi.org/10.1145/3442381.3449903).

**Profile:** boundaries or scores; latent economic regimes require an additional clustering/state model and validation. Online suitability depends on causal inputs, feature windows and training protocol. There is no universal complexity: report training epochs, examples, architecture and measured inference latency; standard full-attention windows introduce quadratic attention work in window length. Choose window, embedding size, training distribution, loss, regularization and score threshold using held-out time periods.

Deep models can encode nonlinear multivariate structure but inherit training-distribution assumptions. Future-window encoders, full-sample pretraining, representation collapse and uncalibrated confidence are concrete failure modes. A learned representation may intentionally discard a variable that later becomes risk-critical. Recent coverage and evaluation concerns appear in [Xu et al. 2025](https://doi.org/10.1007/s42524-025-4109-z).

Concept-drift adaptation adds a further question: after detection, should a model forget, retrain or retrieve an old model? Input drift and conditional-target drift need not coincide. [Gama et al.](https://doi.org/10.1145/2523813).

## 10. Comparative Analysis

“Probabilistic” below means explicit model/predictive probabilities, not simply that an algorithm has a statistical justification. “Recurring” means parameter sharing across repeated states is built in, not that recurrence must occur. Costs omit feature dimension, emission fitting and repeated tuning unless specified. The table synthesizes the cited method sections; it is not a performance ranking.

| Method | Online / offline | Explicit CP? | Explicit latent regimes? | Probabilistic? | Recurring states built in? | Computational cost | Interpretability | Real-time suitability | Key choices | Typical failure |
|---|---|---|---|---|---|---|---|---|---|---|
| Single-change scan | Offline | Yes | No | Test, not posterior | No | \(O(T)\) | High | Retrospective | Contrast, trimming, threshold | Multiple changes mask each other |
| Binary Segmentation | Offline | Yes | No | Not inherently | No | Balanced \(O(T\log T)\); worst \(O(T^2)\) | High | Batch/prefix only | Cost, stopping, minimum length | Greedy wrong first split |
| DP / optimal partitioning | Offline | Yes | No | Not inherently | No | \(O(QT^2)\) / \(O(T^2)\) | High | Batch/prefix only | \(Q\) or penalty, cost | Exact answer to wrong model |
| PELT | Offline | Yes | No | Not inherently | No | Expected \(O(T)\) under conditions; worst \(O(T^2)\) | High | Audit; prefix variant needs own protocol | Penalty, cost, grid, minimum length | Outlier segments; weak pruning |
| BOCPD | Online | Posterior over recent boundary | No reusable labels | Yes | No, in basic model | \(O(t)\)/arrival exact; truncation reduces cost | Moderate–high | Good if budget controlled | Hazard, likelihood, priors, alarm rule | Prior/likelihood misspecification |
| CUSUM | Online | Alarm; onset estimate possible | No | LR score, not posterior | No | \(O(1)\)/arrival for scalar known models | High | Excellent computationally | Baseline, target shift, threshold | Wrong alternative; dependence |
| Page–Hinkley variant | Online | Alarm | No | Not inherently | No | \(O(1)\)/arrival | High | Good | Tolerance, mean update, threshold | Mean adaptation hides drift |
| GLR / mixture scan | Online | Yes/alarm | No | LR / integrated evidence | No | Often \(O(W)\)/arrival plus fitting | Moderate | Depends on window/model | Window, alternative/prior, threshold | Search cost; poor calibration |
| HMM | Both, via different inference | Derived transitions | Yes | Yes | Yes, allowed | \(O(TM^2)\); \(O(M^2)\)/filter step | Moderate | Filter with historical parameters | \(M\), emissions, transitions | Forced familiar state under novelty |
| Markov-switching AR | Both | Derived transitions | Yes | Yes | Yes, allowed | Model-dependent; simple case HMM-like | Moderate–high | Filter; refits add cost | Lags, switching parameters, \(M\) | Hidden-history complexity; wrong dynamics |
| HSMM | Both | Derived transitions | Yes | Yes | Yes, allowed | Common \(O(T(M^2+MD_{\max}))\) | Moderate | Duration budget matters | Durations, cap, states, emissions | Duration/emission confounding |
| TAR / SETAR | Batch fit; causal use | No break estimator | No; observed regimes | Conditional error model | Yes, via threshold crossings | Grid roughly \(O(G(Tp^2+p^3))\) | High | Good with available gate | Threshold, gate variable, lags | Noisy or unavailable gate |
| STAR | Batch fit; causal use | No discrete CP | No | Error model; gate not posterior | Reusable smooth conditions | \(O(Tp)\)/objective evaluation | Moderate–high | Cheap after fitting | Gate family, slope, center, lags | Weak identification |
| Kernel segmentation | Usually offline | Yes | No | Not inherently | No | Gram \(O(T^2)\), plus search | Moderate | Window/approximation needed | Kernel, bandwidth, penalty | Nuisance distances dominate |
| Deep / embedding CPD | Architecture-dependent | Score/boundary | Not by default | Not necessarily calibrated | Not by default | Architecture/training dependent | Lower | Only with causal latency audit | Windows, encoder, training set, threshold | Domain shift or leakage |

Evaluation must match the output. Offline boundaries need one-to-one matching within a declared tolerance, precision/recall and location error. Online alarms need false-alarm behavior, delay, misses and alert burden. State recovery needs label-invariant metrics or explicitly matched labels. Prediction needs chronological scoring. Real data may admit multiple credible annotations. [Van den Burg–Williams](https://arxiv.org/abs/2003.06222).

## 11. Applications in Quantitative Finance and Risk

The following are **proposed monitoring designs**, informed by the linked literature, not claims that each pairing has already been validated.

| Application | Useful input or target | Candidate approach | Decision-relevant check |
|---|---|---|---|
| Volatility regimes | Returns, squared innovations, log realized variance | Variance BOCPD/PELT; switching volatility | Distinguish transient shock, clustering and persistent change |
| Liquidity regimes | Executable spread, depth by side, quote age | Multivariate HMM or kernel CPD | Can the position actually be exited? |
| Order-flow change | Signed flow, cancellations, event rates | Count-model BOCPD; likelihood CUSUM | Normalize exposure and intraday seasonality |
| Microstructure shift | Impact coefficient, tick/spread, queue behavior | Regression breaks; multivariate monitoring | Separate venue/feed/rule change from market change |
| Risk-model breakdown | Standardized residuals and their dependence | CUSUM/GLR; regression CPD | Is the error model or the market-data process failing? |
| VaR monitoring | Exception indicator and exception severity | Coverage/independence diagnostics; sequential monitor | Repeated testing and sparse-tail data |
| Stress-event detection | Joint returns, spreads, depth and outages | Multiple indicators plus detector ensemble | Novel stress need not resemble an old latent state |
| Anomaly detection | Isolated extreme residual, rejected quote | Separate anomaly score and sustained-change score | Outlier versus a persistent new distribution |
| Futures monitoring | Contract prices, basis, roll, expiry, limit status | Contract-aware residual CPD and state models | Rolls and settlement conventions create artificial breaks |
| Trading-system surveillance | Rejects, latency, slippage, fills, inventory | Rate/mean CUSUM or BOCPD | Data/engineering incident versus market deterioration |

Volatility persistence and regime transitions can coexist in financial models. [Hamilton–Susmel](https://doi.org/10.1016/0304-4076(94)90067-1). Order-flow imbalance and depth are relevant to short-horizon price impact, motivating joint monitoring rather than a price-only signal. [Cont et al.](https://doi.org/10.1093/jjfinec/nbt003).

For an upper-tail loss VaR, define \(I_t=1\{L_t>q_{1-\alpha,t}\}\), where the forecast is issued before the outcome. Correct exception frequency is insufficient if exceptions cluster; coverage and independence address different defects. [Christoffersen](https://doi.org/10.2307/2527341). A Bernoulli CUSUM can target an increase from \(\alpha\) to a specified alternative rate, but few exceptions mean limited information, and dependence changes its calibration. Track loss magnitude and exposure changes separately.

### Observed volatility is not economic risk

**Observed volatility** summarizes movement in recorded marks over a chosen clock and window. **Economic risk**, as used here, includes uncertain liquidation value, adverse price discovery, funding needs and execution feasibility. Smoothed or infrequently refreshed marks can suppress measured variation; illiquidity-induced smoothing is studied by [Getmansky–Lo–Makarov](https://doi.org/10.1016/j.jfineco.2004.04.001).

**Illustrative scenario, not historical data:** a futures quote stays at 100 for 30 one-minute observations because the last trade is carried forward. The computed returns are all zero. Meanwhile the executable bid disappears, a large sell queue accumulates and related markets move downward. A Gaussian detector may confidently infer low variance. That inference describes the stale recorded series; it does not establish a narrow distribution of liquidation proceeds.

At a limit-down price, trading can be constrained or halted according to the contract's rules. A constant recorded price need not be an unconstrained equilibrium price. [CME price-limit documentation](https://www.cmegroup.com/trading/price-limits.html). With an empty book there may be no valid executable midpoint; assigning a zero return by forward filling creates apparent certainty precisely when information is missing.

Proposed real-time response: retain separate feed-health, quote-age, spread, depth, limit/halt and exposure indicators. Mark the statistical volatility signal as unreliable when its observation assumptions fail; keep the last valid estimate with an explicit stale flag rather than silently treating a frozen mark as a fresh measurement. Escalation, scenario losses and execution constraints should be governed independently of a “calm” state posterior.

Historical case studies reinforce the need for this separation: the [CFTC–SEC May 6 report](https://www.sec.gov/news/studies/2010/marketevents-report.pdf) describes disruption and liquidity dynamics, while the [CFTC WTI report](https://www.cftc.gov/media/5296/InterimStaffReportNYMEX_WTICrudeOil/download) motivates contract-specific treatment of negative prices. A log-return pipeline is undefined at nonpositive prices; dollar changes or another contract-appropriate transformation must be designed explicitly.

## 12. Failure Modes and Model Risk

This checklist is the review's implementation synthesis. Source families are indicated so the recommendations can be traced without implying that a paper validates the entire proposed system.

| Failure | Why a detector can look convincing | Practical diagnostic or response |
|---|---|---|
| Stale marks / empty book | Repeated records imply falsely low measured noise | Quote age, executable depth and missingness flags; do not replace unavailable liquidity with zero risk |
| Price limits / halt | Constrained prices resemble stability | Consume contract/session status independently of inferred regime |
| Unmodeled autocorrelation | Repeated evidence is counted as independent | Residual diagnostics; dependent null calibration |
| Heavy tails / outliers | Short extreme runs look like new segments | Robustness sensitivity plus separate stress alarms |
| Gradual drift | Step models approximate a slope with many boundaries | Compare drift-aware alternatives; report resolution dependence |
| New crisis outside state dictionary | An HMM must normalize over its known states | Monitor predictive fit as well as state probabilities |
| Adaptive baseline contamination | The monitor rapidly learns a failure as normal | Separate reference and adaptation policies; log each reset |
| Leakage | Full-sample transformations or state smoothing improve history | Audit availability timestamps, fitting windows and causal features |
| Correlation/basis breakdown | Marginal distributions can remain stable | Monitor joint structure and hedging residuals |
| Repeated monitoring / many assets | Small local false-alarm rates produce many alerts | Evaluate portfolio-wide alert burden and dependence |
| Threshold chosen on crisis dates | A visually persuasive fit is selected after the event | Precommit validation/test periods and selection criteria |
| Regime naming after inspection | Arbitrary state numbers acquire economic stories | Report parameters, uncertainty and refit stability |

Sources: [structural-break inference](https://arxiv.org/abs/1805.03807), [sequential monitoring](https://arxiv.org/abs/2104.04186), [robust Bayesian inference](https://arxiv.org/abs/1806.02261), [financial regimes](https://doi.org/10.1146/annurev-financial-110311-101808), [illiquidity](https://doi.org/10.1016/j.jfineco.2004.04.001), and [exchange limits](https://www.cmegroup.com/trading/price-limits.html).

High posterior confidence is conditional on the chosen model. An HMM can assign 99% to its least-wrong state even when every state fits badly. Combine state probabilities with predictive surprise and observation-quality diagnostics; this recommendation follows from the normalization of model probabilities, not from a guarantee that a particular novelty score solves model risk.

## 13. Practical Method Selection Guide

These are conditional decision rules, not rankings.

- **Use BOCPD when** sequential boundary uncertainty and segment-specific prediction matter, a plausible observation model is available, and run-length computation can be budgeted. Validate both hazard and predictive priors, then define the alarm separately.
- **Use PELT when** the task is retrospective segmentation under a defensible additive cost. Report the penalty path and admissible segment lengths; check that the implementation's pruning conditions match the cost.
- **Use HMM/Markov switching when** a small set of recurring patterns and parameter reuse are credible. Evaluate filtered predictions with historically fitted parameters and allow for unfamiliar observations outside the state dictionary.
- **Use CUSUM when** a meaningful baseline and adverse alternative can be specified and fast, interpretable monitoring is required. Calibrate the relevant false-alarm/delay tradeoff.
- **Use threshold models when** an observed, timely covariate plausibly controls behavior. Use STAR when a smooth transition is substantively more appropriate; verify that its gate remains identifiable.
- **Use HSMM when** duration modeling materially affects the decision and enough episodes exist to estimate it.
- **Use kernels when** distributional changes are not well described by a simple parametric target and window/Gram costs are affordable.
- **Use representation learning when** multivariate structure justifies the extra training and validation burden. First verify gains against simpler causal baselines under domain shift.

Before selecting a method, specify the target property, sampling clock, decision deadline, acceptable false alarms and actual action. Then inspect whether the data still measures the economic quantity of interest.

### Proposed experiments and repository deliverables

The [experiment protocol](benchmark-plan.md) specifies a shared Python benchmark for BOCPD, PELT, CUSUM and HMM, a public-data VIX experiment, a futures extension, tuning grids, information sets, metrics and validation checks. These are proposals; no result or runnable benchmark is claimed.

The [repository plan](repository-plan.md) distinguishes present files from future code, lists README sections and specifies figures. The existing README is the public-facing entry point.

### Interview Takeaways

1. “I first ask whether the task is boundary detection, recurring-state inference or an actionable sequential alarm.”
2. “PELT is exact for a specified objective and search space. That does not make its statistical model correct, and linear complexity is conditional.”
3. “A BOCPD hazard is a prior on duration, not an alert threshold. I inspect prior predictive behavior and the run-length indexing.”
4. “A filtered HMM posterior is usable in real time only if its parameters and features were also estimated using information available then.”
5. “Gaussian emissions can turn heavy tails into extra regimes. State count is partly a modeling choice.”
6. “A flat price can mean stale data, a binding limit or no liquidity. Falling observed volatility does not prove falling economic risk.”
7. “VaR coverage, exception clustering and loss severity answer different questions.”
8. “I compare delay at comparable false-alarm behavior and keep offline reconstruction separate from live monitoring.”

## 14. Open Research Questions

These are questions for this repository, not claims of previously undiscovered research gaps.

1. **Change or observation failure?** Can monitoring distinguish a true distributional shift from changing price freshness, censoring or missingness?
2. **Recurring versus novel states:** when does sharing old state parameters improve adaptation, and when does it suppress recognition of an unprecedented event?
3. **Robustness versus urgency:** how much protection against isolated outliers is appropriate when the first extreme observation may be the start of stress?
4. **Duration and trading clock:** how do elapsed-time, transaction-time and volume-time hazards differ in variable activity?
5. **Joint changes:** can marginal monitors miss deterioration in correlation, impact or hedge relationships? Network and functional extensions offer broader contexts. [Li, Wang & Yu 2026](https://doi.org/10.1146/annurev-statistics-041124-044143).
6. **Decision-aware evaluation:** does a statistically better detector improve alert triage, risk estimation or controlled adaptation after accounting for costs?
7. **Labels and uncertainty:** can results remain stable across plausible human annotations and tolerance choices? [Van den Burg–Williams](https://arxiv.org/abs/2003.06222).

## 15. References

The [annotated bibliography](references.md) contains **34 research papers/reviews/technical notes and 4 official operational or data sources**, with authors, year, title, venue, DOI/arXiv or primary-source URL, a contribution summary and supporting review sections. [BibTeX](references.bib) and [machine-readable records](sources.json) are provided.

Suggested entry sequence: R02 (offline taxonomy), R01 (structural inference), R08–R10 (Bayesian recursion and conjugacy), R12 (PELT), R04 (sequential objectives), R16–R18 (latent states and duration), R28 (finance), and R27 (recent deep-learning review). Recent papers expand coverage; recency alone is not evidence of superior practical performance.
