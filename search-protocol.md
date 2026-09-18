# Search protocol and evidence ledger

Literature-search cutoff: **2026-09-16**. Editorial and consistency checks completed 2026-09-18. This is a bounded systematic search with narrative synthesis for an educational/research repository. It is not a registered protocol, exhaustive bibliographic-database review, meta-analysis, or independent replication of each method.

## Questions and eligibility

Include work supporting temporal boundary estimation, sequential monitoring, recurring-state inference, observed-threshold dynamics, modern representation/robust methods, or financial observation and evaluation risks. Prefer primary methodological papers, peer-reviewed surveys and official exchange/regulator/data sources. Retain foundational preprints and technical notes with their status explicit.

Exclude trading blogs and vendor performance claims as methodological evidence; deduplicate working-paper/journal versions; avoid performance rankings across incompatible datasets. Network/functional extensions are boundary-of-scope references rather than core derivations. Anomaly detection is included to clarify its relationship to sustained changes.

## Search process actually used

Web discovery was followed by targeted publisher, arXiv, author/institutional, PMLR, NeurIPS, JMLR, exchange and regulator retrieval. Search snippets and secondary indexes helped locate records. Technical explanations combine accessible primary material, established method formulations and explicitly identified algebraic derivations. The earlier Chinese draft supplied seed references; the English pass expanded them.

Representative exact queries from the search calls are recorded below. This is a query-family log, not a raw export of every ranked search hit.

| Family | Queries used | Retained evidence |
|---|---|---|
| Structural breaks / surveys | structural breaks review Perron 2006 dealing structural breaks survey; regime switching models review survey Hamilton 2016 | R01, R03, R06–R07, R17 |
| Offline methods | Truong Oudre Vayatis 2020 selective review offline change point detection methods; "Optimal Detection of Changepoints With a Linear Computational Cost"; "Fryzlewicz" "2014" "Wild binary segmentation" | R02, R12–R13 |
| Online Bayes | "Bayesian Online Changepoint Detection" Adams MacKay; Fearnhead Liu 2007 online inference multiple changepoint problems exact particle filters | R08–R09 |
| Priors / adaptation | Murphy 2007 conjugate Bayesian analysis Gaussian distribution normal inverse gamma; Turner Saatci Rasmussen 2009 adaptive sequential Bayesian change point detection hazard | R10–R11 |
| Sequential methods | "Sequential (Quickest) Change Detection" Xie Zou Xie Veeravalli 2021; "Page" "1954" "Continuous Inspection Schemes" Biometrika; "Hinkley" "1971" "Inference about the change-point" | R04, R14–R15 |
| Latent duration | "Rabiner" "1989" "tutorial" "10.1109"; hidden semi Markov models Yu 2010 artificial intelligence 174 | R16, R18 |
| Threshold dynamics | "Tong" "Lim" "1980" "Threshold autoregression"; "Teräsvirta" "1994" "Specification, Estimation" | R19–R20 |
| Kernel / robust Bayes | kernel change point detection Arlot Celisse Harchaoui 2019 consistent; Bayesian online changepoint detection generalized Bayesian robust Knoblauch Jewson Damoulas 2018 | R21–R24 |
| Deep / recent | "Time series change point detection with self-supervised contrastive predictive coding"; deep learning change point detection review 2024 2025 time series; change point detection time series review 2024 2025 2026 survey | R25–R27, R34 |
| Drift / evaluation | "A survey on concept drift adaptation" Gama 2014; change point detection benchmarking van den Burg Williams 2020 evaluation | R05, R33 |
| Finance | Ang Timmermann 2012 regime changes financial markets annual review financial economics; "Hamilton" "Susmel" "1994" "Autoregressive conditional heteroskedasticity" | R28–R29 |
| Risk / microstructure | Christoffersen 1998 Evaluating interval forecasts 10.2307; Getmansky Lo Makarov 2004 econometric model serial correlation illiquidity hedge fund returns; Cont Kukanov Stoikov 2014 price impact order book events | R30–R32 |
| Operational evidence | site.cmegroup.com price limits limit down markets trading halt futures; site.sec.gov 2010 findings market events May 6 liquidity futures report; site.cmegroup.com negative oil prices April 2020 futures risk; site.cboe.com VIX historical data daily closing prices csv | S01–S04 |

Follow-up retrieval verified exact titles, publication years and primary versions. Journal year is used where verified: Li et al. is 2024 although its arXiv submission is 2022; Deldari et al. is 2021 although its preprint is 2020; R34 is 2026 despite advance publication in 2025. Crawling dates and later digitization dates are not treated as publication years.

## Included records and access limitations

The register contains **38 unique included sources: R01–R34 and S01–S04**, in [sources.json](sources.json). Each [annotated entry](references.md) maps its contribution to review sections. No PRISMA count of screened hits is asserted: search-engine results were not exported as an exhaustive deduplicated candidate database.

| Claim area | Evidence retrieved | Verification depth / limitation |
|---|---|---|
| BOCPD indexing | Adams–MacKay author PDF, recursion and algorithm | Relevant method text inspected; constant reset-mass implication is derived explicitly |
| Gaussian conjugacy | Murphy author technical note | Parameterization and standard update/predictive formulas checked; not a peer-reviewed article |
| PELT exactness / cost | Killick et al. manuscript, Theorems 3.1–3.2 | Conditions inspected; expected-cost and worst-case distinctions retained |
| HMM algorithms | Rabiner tutorial PDF and Hamilton sources | Tutorial PDF accessible but scanned-text extraction limited; no complete proof audit claimed |
| HSMM / TAR / STAR | Publisher records and methodological/review sources | Standard formulations synthesized; all theorem proofs not independently audited |
| Modern methods | JMLR/PMLR/NeurIPS, author arXiv, JRSSB and Springer records | Contributions and scope checked; superiority claims not generalized or re-benchmarked |
| Finance evidence | Author-hosted illiquidity record, publisher records and official reports | Evidence types separated; no causal inference from event-date alignment |
| VIX / limits | Official source pages | Dynamic sources; input snapshots and rule versions needed for experiments |

For sources whose full text was not machine-readable, this review limits claims to established formulations and verified contributions. The small [verification script](verify_review.py) checks selected mathematical identities and document consistency; it is not a comprehensive method implementation or replication.

## Screening decisions

- **Tan & Wu (2025), “On Regime Switching Models”:** bibliographic record located, publisher article not retrievable in the initial search. Excluded from technical evidence pending [full-text verification](https://www.mdpi.com/2227-7390/13/7/1128).
- **Li, Wang & Yu (2026):** included as R34 after verifying the publisher record; its change-plane, functional and network focus is marked as a scope extension.
- **Additional 2024 broad CPD and graph-only surveys:** surfaced in the recency sweep; not added because this review prioritizes requested methods and directly relevant primary sources over redundant breadth.
- **Trading blogs, forum backtests and vendor summaries:** not retained as evidence of algorithmic properties or financial effectiveness.
- **Institutional copies of an included article:** alternate access routes, not separate studies.

## Extraction and synthesis

For each method extract target, output, information set, assumptions, tuning, computation, failure modes and risk use. For each paper record authors/year/title/venue/link, contribution and supporting sections. Calibration grids and operating rules are marked as repository proposals.

No aggregate effect size is calculated: boundaries, alarms, states and forecasts have different targets. No universal ranking is inferred from citation counts, publication year or an article's own benchmark.

A publication-grade systematic review would additionally export full database results, preregister eligibility rules, retain every exclusion reason and independently extract full texts. Those steps remain limitations of this bounded review.
