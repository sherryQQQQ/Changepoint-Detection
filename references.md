# Annotated references

Each record includes the cited version, contribution and review sections. Working papers and technical notes are explicitly distinguished from peer-reviewed publications. Official operational sources have no DOI/arXiv identifier; their primary URLs are supplied instead.

<a id="r01"></a>

## R01 — Casini, Alessandro; Perron, Pierre (2018)

**[Structural Breaks in Time Series](https://arxiv.org/abs/1805.03807)**. arXiv preprint.

Reviews econometric break estimation, testing and computation, including dependent errors and extensions beyond basic regression. It anchors the distinction between locating boundaries and making valid structural-stability inferences.

Type: Review. Supports Sections 1–3, 12.

<a id="r02"></a>

## R02 — Truong, Charles; Oudre, Laurent; Vayatis, Nicolas (2020)

**[Selective review of offline change point detection methods](https://doi.org/10.1016/j.sigpro.2019.107299)**. Signal Processing, 167, 107299.

Organizes offline detection by segment cost, search algorithm and complexity constraint. This decomposition separates statistical modeling choices from optimization choices.

Type: Review. Supports Sections 3, 5, 10.

<a id="r03"></a>

## R03 — Hamilton, James D. (2016)

**[Macroeconomic Regimes and Regime Shifts](https://doi.org/10.3386/w21863)**. NBER Working Paper 21863; handbook survey.

Surveys empirical and theoretical approaches to regime changes in macroeconomics. The cited record is the NBER version, not a separate claim of journal publication.

Type: Review. Supports Sections 2, 7.

<a id="r04"></a>

## R04 — Xie, Liyan; Zou, Shaofeng; Xie, Yao; Veeravalli, Venugopal V. (2021)

**[Sequential (Quickest) Change Detection: Classical Results and New Directions](https://arxiv.org/abs/2104.04186)**. IEEE Journal on Selected Areas in Information Theory, 2(2), 494–514.

Reviews sequential detection objectives, classical procedures and modern extensions. Provides the framework for distinguishing false-alarm constraints from delay objectives.

Type: Review. Supports Sections 6, 10, 13.

<a id="r05"></a>

## R05 — Gama, João; Žliobaitė, Indrė; Bifet, Albert; Pechenizkiy, Mykola; Bouchachia, Abdelhamid (2014)

**[A survey on concept drift adaptation](https://doi.org/10.1145/2523813)**. ACM Computing Surveys, 46(4), Article 44.

Connects distributional change to updating predictive systems and evaluating adaptation. Useful for distinguishing detection from the downstream decision to retrain or reuse a model.

Type: Review. Supports Sections 9, 12–14.

<a id="r06"></a>

## R06 — Bai, Jushan; Perron, Pierre (1998)

**[Estimating and Testing Linear Models with Multiple Structural Changes](https://doi.org/10.2307/2998540)**. Econometrica, 66(1), 47–78.

Develops estimation and testing for multiple structural changes in linear models. It supports treating coefficient breaks as an inferential problem rather than a visual segmentation exercise.

Type: Foundational. Supports Sections 3.

<a id="r07"></a>

## R07 — Bai, Jushan; Perron, Pierre (2003)

**[Computation and analysis of multiple structural change models](https://doi.org/10.1002/jae.659)**. Journal of Applied Econometrics.

Addresses computation, break-date intervals and practical testing for multiple structural-change models. Its dynamic-programming treatment is a useful bridge to optimization-based CPD.

Type: Foundational. Supports Sections 3, 5.

<a id="r08"></a>

## R08 — Adams, Ryan Prescott; MacKay, David J. C. (2007)

**[Bayesian Online Changepoint Detection](https://arxiv.org/abs/0710.3742)**. arXiv preprint.

Introduces a recursive posterior over run length using a segment-duration prior and segment-specific predictive distributions. The equations in Section 4 explicitly use its reset-after-observation convention.

Type: Foundational. Supports Sections 4.

<a id="r09"></a>

## R09 — Fearnhead, Paul; Liu, Zhen (2007)

**[On-line inference for multiple changepoint problems](https://doi.org/10.1111/j.1467-9868.2007.00601.x)**. Journal of the Royal Statistical Society: Series B, 69(4), 589–605.

Develops exact online filtering for a class of multiple-change models and particle-resampling approximations that reduce computation. Supports the distinction between exact inference and bounded-cost approximations.

Type: Foundational. Supports Sections 4.

<a id="r10"></a>

## R10 — Murphy, Kevin P. (2007)

**[Conjugate Bayesian analysis of the Gaussian distribution](https://www.cs.ubc.ca/~murphyk/Papers/bayesGauss.pdf)**. Technical note.

Collects Gaussian conjugate-prior parameterizations, posterior updates and predictive distributions. Used for the Normal–Inverse-Gamma worked example; no DOI or arXiv identifier is asserted.

Type: Technical reference. Supports Sections 4.

<a id="r11"></a>

## R11 — Turner, Ryan; Saatci, Yunus; Rasmussen, Carl Edward (2009)

**[Adaptive Sequential Bayesian Change Point Detection](https://mlg.eng.cam.ac.uk/pub/pdf/TurSaaRas09.pdf)**. Author-hosted workshop manuscript.

Studies learning parameters within sequential Bayesian change detection, including hazard and predictive-model parameters. It motivates adaptive priors while not eliminating the need for external calibration; no DOI or arXiv identifier was verified.

Type: Extension. Supports Sections 4.

<a id="r12"></a>

## R12 — Killick, Rebecca; Fearnhead, Paul; Eckley, Idris A. (2012)

**[Optimal Detection of Changepoints With a Linear Computational Cost](https://doi.org/10.1080/01621459.2012.737745)**. Journal of the American Statistical Association, 107(500), 1590–1598.

Introduces PELT, an exact pruning algorithm for a penalized segmentation objective. Expected linear complexity requires assumptions; quadratic worst-case behavior remains possible.

Type: Foundational. Supports Sections 5.

<a id="r13"></a>

## R13 — Fryzlewicz, Piotr (2014)

**[Wild binary segmentation for multiple change-point detection](https://arxiv.org/abs/1411.0858)**. The Annals of Statistics.

Uses randomized subintervals to improve isolation of changes compared with ordinary binary segmentation. Its guarantees concern specified signal and noise conditions, not arbitrary financial data.

Type: Method. Supports Sections 3.

<a id="r14"></a>

## R14 — Page, E. S. (1954)

**[Continuous Inspection Schemes](https://doi.org/10.1093/biomet/41.1-2.100)**. Biometrika, 41(1–2), 100–115.

Establishes cumulative inspection schemes for detecting sustained departures. It is a foundational source for CUSUM monitoring.

Type: Foundational. Supports Sections 6.

<a id="r15"></a>

## R15 — Hinkley, D. V. (1971)

**[Inference about the change-point from cumulative sum tests](https://doi.org/10.1093/biomet/58.3.509)**. Biometrika, 58(3), 509–523.

Studies change-location inference from cumulative-sum tests for normal mean changes and its relationship to likelihood inference. Modern software called Page–Hinkley varies; this citation does not certify every implementation variant.

Type: Foundational. Supports Sections 6.

<a id="r16"></a>

## R16 — Rabiner, Lawrence R. (1989)

**[A tutorial on hidden Markov models and selected applications in speech recognition](https://doi.org/10.1109/5.18626)**. Proceedings of the IEEE, 77(2), 257–286.

Explains HMM likelihood evaluation, state decoding and parameter estimation. Supports forward–backward, Viterbi and EM distinctions.

Type: Foundational tutorial. Supports Sections 7.

<a id="r17"></a>

## R17 — Hamilton, James D. (1989)

**[A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle](https://doi.org/10.2307/1912559)**. Econometrica, 57(2), 357–384.

Introduces an influential econometric treatment of unobserved recurring shifts in growth dynamics. It is the main historical reference for Markov-switching time-series models here.

Type: Foundational. Supports Sections 7.

<a id="r18"></a>

## R18 — Yu, Shun-Zheng (2010)

**[Hidden semi-Markov models](https://doi.org/10.1016/j.artint.2009.11.011)**. Artificial Intelligence, 174(2), 215–243.

Reviews models with explicit state-duration distributions and their inference algorithms. Provides a route beyond the geometric dwell times of homogeneous HMMs.

Type: Review. Supports Sections 7.

<a id="r19"></a>

## R19 — Tong, Howell; Lim, K. S. (1980)

**[Threshold Autoregression, Limit Cycles and Cyclical Data](https://doi.org/10.1111/j.2517-6161.1980.tb01126.x)**. Journal of the Royal Statistical Society: Series B, 42(3).

Develops threshold autoregression as a nonlinear time-series model. Regime membership is governed by an observed threshold variable rather than an unobserved Markov chain.

Type: Foundational. Supports Sections 8.

<a id="r20"></a>

## R20 — Teräsvirta, Timo (1994)

**[Specification, Estimation, and Evaluation of Smooth Transition Autoregressive Models](https://doi.org/10.1080/01621459.1994.10476462)**. Journal of the American Statistical Association, 89(425), 208–218.

Develops a modeling cycle for logistic and exponential smooth-transition autoregression, including specification choices. Supports distinguishing smooth conditional dynamics from discrete latent states.

Type: Foundational. Supports Sections 8.

<a id="r21"></a>

## R21 — Arlot, Sylvain; Celisse, Alain; Harchaoui, Zaid (2019)

**[A Kernel Multiple Change-point Algorithm via Model Selection](https://arxiv.org/abs/1202.3878)**. Journal of Machine Learning Research, 20(162), 1–56.

Develops model-selection penalties for kernel multiple-change detection, with an oracle inequality under the paper's conditions. Kernel embeddings permit changes beyond a scalar mean to be represented as changes in feature-space means.

Type: Modern method. Supports Sections 9.

<a id="r22"></a>

## R22 — Knoblauch, Jeremias; Damoulas, Theodoros (2018)

**[Spatio-temporal Bayesian On-line Changepoint Detection with Model Selection](https://arxiv.org/abs/1805.05383)**. ICML, PMLR 80, 2718–2727.

Extends Bayesian online CPD to model selection and nonstationary spatio-temporal data. It illustrates why richer within-segment models can matter as much as the boundary prior.

Type: Modern method. Supports Sections 4, 9.

<a id="r23"></a>

## R23 — Knoblauch, Jeremias; Jewson, Jack; Damoulas, Theodoros (2018)

**[Doubly Robust Bayesian Inference for Non-Stationary Streaming Data with β-Divergences](https://arxiv.org/abs/1806.02261)**. NeurIPS 2018.

Uses generalized Bayesian inference to reduce the influence of outliers in online CPD. Robustness requires its stated loss and model conditions, not merely a Bayesian label.

Type: Modern method. Supports Sections 4, 9.

<a id="r24"></a>

## R24 — Altamirano, Matias; Briol, François-Xavier; Knoblauch, Jeremias (2023)

**[Robust and Scalable Bayesian Online Changepoint Detection](https://arxiv.org/abs/2302.04759)**. ICML, PMLR 202, 642–663.

Uses diffusion score matching within generalized Bayes to obtain tractable robust updates. The paper's robustness results and timing comparisons should not be generalized to all deployment settings.

Type: Modern method. Supports Sections 4, 9.

<a id="r25"></a>

## R25 — Deldari, Shohreh; Smith, Daniel V.; Xue, Hao; Salim, Flora D. (2021)

**[Time Series Change Point Detection with Self-Supervised Contrastive Predictive Coding](https://doi.org/10.1145/3442381.3449903)**. The Web Conference 2021, 3124–3135.

Learns representations through contrastive predictive coding and uses their similarities for change detection. A detected boundary in representation space is not automatically an economically interpretable recurring regime.

Type: Modern method. Supports Sections 9.

<a id="r26"></a>

## R26 — Li, Jie; Fearnhead, Paul; Fryzlewicz, Piotr; Wang, Tengyao (2024)

**[Automatic change-point detection in time series via deep learning](https://doi.org/10.1093/jrsssb/qkae004)**. Journal of the Royal Statistical Society: Series B, 86(2), 273–285.

Trains neural networks for offline change detection and gives theoretical and empirical analysis. Performance depends on the training distribution's relationship to the target change and noise mechanisms.

Type: Modern method. Supports Sections 9.

<a id="r27"></a>

## R27 — Xu, Ruiyu; Song, Zheren; Wu, Jianguo; Wang, Chao; Zhou, Shiyu (2025)

**[Change-point detection with deep learning: A review](https://doi.org/10.1007/s42524-025-4109-z)**. Frontiers of Engineering Management, 12, 154–176.

Surveys supervised and unsupervised deep CPD methods, datasets and evaluation. It is a recent entry point for representation learning and generalization concerns.

Type: Recent review. Supports Sections 9.

<a id="r28"></a>

## R28 — Ang, Andrew; Timmermann, Allan (2012)

**[Regime Changes and Financial Markets](https://doi.org/10.1146/annurev-financial-110311-101808)**. Annual Review of Financial Economics, 4, 313–337.

Reviews regime changes in financial markets and their implications for financial decisions. Supports recurring-state modeling without implying that regime classification guarantees profitable timing.

Type: Finance review. Supports Sections 7, 11.

<a id="r29"></a>

## R29 — Hamilton, James D.; Susmel, Raul (1994)

**[Autoregressive conditional heteroskedasticity and changes in regime](https://doi.org/10.1016/0304-4076(94)90067-1)**. Journal of Econometrics, 64(1–2), 307–333.

Combines ARCH dynamics with Markov changes in regime in an application to stock returns. Shows how within-state volatility dynamics and between-state changes can coexist.

Type: Finance application. Supports Sections 7, 11.

<a id="r30"></a>

## R30 — Christoffersen, Peter F. (1998)

**[Evaluating Interval Forecasts](https://doi.org/10.2307/2527341)**. International Economic Review, 39(4), 841–862.

Develops conditional interval-forecast evaluation, including coverage and independence. VaR exception frequency alone is therefore an incomplete diagnostic of forecast adequacy.

Type: Risk evaluation. Supports Sections 11.

<a id="r31"></a>

## R31 — Getmansky, Mila; Lo, Andrew W.; Makarov, Igor (2004)

**[An econometric model of serial correlation and illiquidity in hedge fund returns](https://doi.org/10.1016/j.jfineco.2004.04.001)**. Journal of Financial Economics, 74, 529–609.

Models return smoothing and serial correlation associated with illiquidity. It supports questioning whether quiet reported returns represent quiet underlying economic exposures.

Type: Finance application. Supports Sections 11–12.

<a id="r32"></a>

## R32 — Cont, Rama; Kukanov, Arseniy; Stoikov, Sasha (2014)

**[The Price Impact of Order Book Events](https://doi.org/10.1093/jjfinec/nbt003)**. Journal of Financial Econometrics, 12(1), 47–88.

Studies short-horizon price changes in relation to order-flow imbalance and depth. Motivates monitoring order-book conditions alongside returns; it is not itself a universal regime detector.

Type: Microstructure application. Supports Sections 11–12.

<a id="r33"></a>

## R33 — van den Burg, Gerrit J. J.; Williams, Christopher K. I. (2020)

**[An Evaluation of Change Point Detection Algorithms](https://arxiv.org/abs/2003.06222)**. arXiv preprint; revised 2022.

Introduces a real-data benchmark with multiple human annotations and evaluates CPD algorithms. Highlights ambiguity in real-world change labels and the importance of evaluation design.

Type: Benchmark. Supports Sections 10, 13.

<a id="r34"></a>

## R34 — Li, Jialiang; Wang, Jingli; Yu, Yuetao (2026)

**[Change-Point Detection and Its Modern Applications](https://doi.org/10.1146/annurev-statistics-041124-044143)**. Annual Review of Statistics and Its Application, 13, 421–438.

Reviews change-plane subgroups, functional discontinuities and dynamic-network changes. Included as a boundary-of-scope reference, not as evidence that ordinary univariate risk monitoring requires these models.

Type: Recent review; scope extension. Supports Sections 14.

<a id="s01"></a>

## S01 — CME Group (2026)

**[Price Limits: Ags, Energy, Metals, Equity Index](https://www.cmegroup.com/trading/price-limits.html)**. Official exchange documentation; accessed 2026-09-16.

Explains exchange price-limit mechanisms and contract-specific conditions. Rules can change; the review avoids treating one product's limit levels as universal.

Type: Operational source. Supports Sections 11–12.

<a id="s02"></a>

## S02 — CFTC; SEC (2010)

**[Findings Regarding the Market Events of May 6, 2010](https://www.sec.gov/news/studies/2010/marketevents-report.pdf)**. Joint staff report, September 30, 2010.

Documents the sequence of the May 6 market disruption and liquidity dynamics. Used as a historical case, not as a generic ground-truth label for all regime methods.

Type: Official event study. Supports Sections 11–12.

<a id="s03"></a>

## S03 — CFTC (2020)

**[Interim Staff Report on Trading in NYMEX WTI Crude Oil Futures Contract Leading up to, on, and around April 20, 2020](https://www.cftc.gov/media/5296/InterimStaffReportNYMEX_WTICrudeOil/download)**. Official staff report.

Examines the episode surrounding negative WTI futures prices. Motivates contract-aware transformations and expiry checks instead of assuming all futures prices admit log returns.

Type: Official event study. Supports Sections 11–12.

<a id="s04"></a>

## S04 — Cboe (2026)

**[VIX Index Historical Data](https://www.cboe.com/tradable_products/vix/vix_historical_data)**. Official data page; accessed 2026-09-16.

Provides historical VIX observations for the proposed reproducible finance experiment. VIX is an implied-volatility index, not a futures return or a realized-volatility series.

Type: Data source. Supports Sections 13.

