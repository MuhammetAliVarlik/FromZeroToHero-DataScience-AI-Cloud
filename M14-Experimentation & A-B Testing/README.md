# M14 · Experimentation & A/B Testing

> Generated from `curriculum.yml` by `tools/build_curriculum.py`. Do not edit by hand.

**Group:** Data Science · **Lessons:** 8 existing + 0 planned (8 verified) · **GPU:** —

**Prerequisites:** [M06 Statistics & Inference (R)](../M06-Statistics%20%26%20Inference%20%28R%29/README.md), [M08 NumPy, Pandas & Polars](../M08-NumPy%2C%20Pandas%20%26%20Polars/README.md)

**Part of paths:** [Data Analyst & BI](../paths/data-analyst.md), [Data Scientist](../paths/data-scientist.md)

| # | Lesson | Level | Status | Description |
| :-: | :--- | :--- | :-: | :--- |
| 01 | [Python Statistics Toolkit (SciPy, statsmodels, pingouin)](01-Python%20Statistics%20Toolkit%20(SciPy,%20statsmodels,%20pingouin).ipynb) | 🟢 Beginner | ✅ | The hypothesis-testing toolbox for A/B tests: z-test, Welch t-test, chi-square, Mann-Whitney U, bootstrap and permutation tests on the Hillstrom e-mail experiment, the same comparison in SciPy, statsmodels and pingouin, A/A simulations with uniform p-values, and Bonferroni/Holm/BH corrections. |
| 02 | [Experiment Design & Power Analysis (statsmodels)](02-Experiment%20Design%20&%20Power%20Analysis%20(statsmodels).ipynb) | 🟡 Intermediate | ✅ | Hypothesis, unit of randomization, primary/secondary/guardrail metrics and OEC; sample size from MDE, alpha and power with real Hillstrom baselines; test duration, a simulation check, why heavy-tailed spend needs 37 times more users, unequal splits, and a pre-registration checklist. |
| 03 | [A/B Testing End to End (tea-tasting)](03-A-B%20Testing%20End%20to%20End%20(tea-tasting).ipynb) | 🟡 Intermediate | ✅ | A full A/B analysis of the Hillstrom e-mail test: SRM and covariate balance checks, lift CIs by hand and with tea-tasting, practical significance against a break-even threshold, three arms with Holm, a scorecard and a forest plot. |
| 04 | [Ratio Metrics & the Delta Method](04-Ratio%20Metrics%20&%20the%20Delta%20Method.ipynb) | 🟠 Advanced | ✅ | Ratio metrics where the analysis unit differs from the randomization unit: the delta method from a Taylor expansion, Fieller vs bootstrap CIs for the relative lift, and an A/A simulation where a naive session-level test reaches an 18.7 % false positive rate. |
| 05 | [Variance Reduction with CUPED](05-Variance%20Reduction%20with%20CUPED.ipynb) | 🟠 Advanced | ✅ | CUPED: theta, rho-squared variance reduction, the OLS equivalence, regression adjustment and CUPAC, bias and false positive rate checks, sample size savings, and the post-treatment covariate trap; small real gain on two-week spend vs a halved variance on a stable repeat metric. |
| 06 | [Trustworthy Experiments (SRM, A/A Tests & Guardrails)](06-Trustworthy%20Experiments%20(SRM,%20A-A%20Tests%20&%20Guardrails).ipynb) | 🟠 Advanced | ✅ | The chi-square SRM test on real and deliberately corrupted data, 2,000 A/A tests and what breaks them (unit mismatch, heavy tails at small n), guardrail metrics with non-inferiority tests, and a trustworthiness checklist. |
| 07 | [Sequential Testing & Safe Peeking (mSPRT)](07-Sequential%20Testing%20&%20Safe%20Peeking%20(mSPRT).ipynb) | 🟠 Advanced | ✅ | How peeking inflates the false positive rate (5 % to 42 %), group sequential designs with O'Brien-Fleming/Pocock alpha spending, and the mSPRT with always-valid p-values and confidence sequences, replayed on the real Hillstrom stream. |
| 08 | [Multi-Armed Bandits (Thompson Sampling)](08-Multi-Armed%20Bandits%20(Thompson%20Sampling).ipynb) | 🟠 Advanced | ✅ | Epsilon-greedy, UCB1 and Beta-Bernoulli Thompson sampling with regret analysis, offline replay evaluation on the randomized Hillstrom logs, the bias of estimates under adaptive allocation, and a simple contextual bandit. |

## Assignments

| Assignment | Solution |
| :--- | :--- |
| [Which E-Mail, to Whom?](assignments/01-Email-Campaign-Experiment.ipynb) | [solution](assignments/01-Email-Campaign-Experiment-solution.ipynb) |

Status legend: ✅ done · 🔍 review · 📈 deepen · ⚙️ realise · 🔀 merge · ✏️ rewrite · 🆕 planned
