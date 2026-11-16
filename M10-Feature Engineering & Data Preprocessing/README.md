# M10 · Feature Engineering & Data Preprocessing

> Generated from `curriculum.yml` by `tools/build_curriculum.py`. Do not edit by hand.

**Group:** Data · **Lessons:** 16 existing + 0 planned (16 verified) · **GPU:** —

**Prerequisites:** [M08 NumPy, Pandas & Polars](../M08-NumPy%2C%20Pandas%20%26%20Polars/README.md) · **Recommended:** [M06 Statistics & Inference (R)](../M06-Statistics%20%26%20Inference%20%28R%29/README.md)

**Part of paths:** [Data Scientist](../paths/data-scientist.md), [Machine Learning Engineer](../paths/ml-engineer.md)

| # | Lesson | Level | Status | Description |
| :-: | :--- | :--- | :-: | :--- |
| 01 | [Data Profiling and Quality Checks](01-Data%20Profiling%20and%20Quality%20Checks.ipynb) | 🟢 Beginner | ✅ | Column profiles, disguised missing values (0, '?', 'No_...'), duplicates, constant and redundant columns, range and consistency rules on Adult and Ames. |
| 02 | [Missing Value Treatment](02-Missing%20Value%20Treatment.ipynb) | 🟡 Intermediate | ✅ | MCAR/MAR/MNAR, imputation error measured on hidden values (mean, group median, KNN, iterative), 'missing' categories and indicators in pipelines. |
| 03 | [Outlier Detection and Robust Handling](03-Outlier%20Detection%20and%20Robust%20Handling.ipynb) | 🟡 Intermediate | ✅ | z-score, IQR and robust MAD rules, Isolation Forest, the Ames Partial sales, and the measured effect of removal, winsorising and Huber loss. |
| 04 | [Scaling and Normalization](04-Scaling%20and%20Normalization.ipynb) | 🟡 Intermediate | ✅ | Standard/min-max/robust/max-abs scalers, log, Yeo-Johnson and quantile transforms, which models need scaling (measured), log-target regression. |
| 05 | [Categorical Encoding](05-Categorical%20Encoding.ipynb) | 🟡 Intermediate | ✅ | One-hot, ordinal with the true order, frequency, cross-fitted target encoding (leakage demo), hashing, rare and unseen categories. |
| 06 | [Binning and Discretization](06-Binning%20and%20Discretization.ipynb) | 🟡 Intermediate | ✅ | Equal-width, quantile, k-means and tree binning, splines vs bins for non-linear effects, weight of evidence and information value. |
| 07 | [Feature Construction](07-Feature%20Construction.ipynb) | 🟡 Intermediate | ✅ | Domain features for house prices, feature groups measured with CV, interactions and polynomial terms (and when they do not help). |
| 08 | [Feature Selection & PCA](08-Feature%20Selection%20&%20PCA.ipynb) | 🟡 Intermediate | ✅ | Variance, correlation and mutual information filters, Lasso, RFECV, permutation importance, selection bias on noise, PCA trade-offs. |
| 09 | [Target Leakage Prevention](09-Target%20Leakage%20Prevention.ipynb) | 🟡 Intermediate | ✅ | The Bank Marketing duration leak, preprocessing leakage with feature selection, random vs time-ordered splits, a leakage checklist. |
| 10 | [Pipeline Engineering (scikit-learn)](10-Pipeline%20Engineering%20(scikit-learn).ipynb) | 🟡 Intermediate | ✅ | ColumnTransformer, a custom transformer, joint grid search over preprocessing and models, saving pipelines with metadata, unseen inputs. |
| 11 | [Handling Imbalanced Data](11-Handling%20Imbalanced%20Data.ipynb) | 🟡 Intermediate | ✅ | PR AUC vs accuracy, class weights, over/under-sampling and SMOTE in pipelines, profit-based threshold tuning with TunedThresholdClassifierCV. |
| 12 | [Temporal Feature Engineering](12-Temporal%20Feature%20Engineering.ipynb) | 🟡 Intermediate | ✅ | Calendar and cyclical features, lags and rolling windows without future data, time-ordered CV, a centred-window leak, when lags do not help. |
| 13 | [Text and Categorical Cleaning (Advanced)](13-Text%20and%20Categorical%20Cleaning%20(Advanced).ipynb) | 🟡 Intermediate | ✅ | Unicode/case/whitespace normalisation, aliases, fuzzy matching with measured threshold trade-offs, rare categories, multi-valued fields. |
| 14 | [Data Validation with pandera](14-Data%20Validation%20with%20pandera.ipynb) | 🟡 Intermediate | ✅ | pandera schemas and DataFrameModels, cross-column checks, lazy validation reports, schemas as gates before training and prediction. |
| 15 | [Embeddings as Features](15-Embeddings%20as%20Features.ipynb) | 🟡 Intermediate | ✅ | TF-IDF vs nomic-embed-text embeddings on 20 Newsgroups, label efficiency, embedding space, combining with tabular features, costs and risks. |
| 16 | [Feature Stores and Reuse](16-Feature%20Stores%20and%20Reuse.ipynb) | 🟠 Advanced | ✅ | Feature views and event timestamps, point-in-time joins, a Redis online store, training/serving consistency checks, Feast concepts. |

## Assignments

| Assignment | Solution |
| :--- | :--- |
| [Campaign Targeting Pipeline](assignments/01-Campaign-Targeting-Pipeline.ipynb) | [solution](assignments/01-Campaign-Targeting-Pipeline-solution.ipynb) |
| [House Price Feature Lab](assignments/02-House-Price-Feature-Lab.ipynb) | [solution](assignments/02-House-Price-Feature-Lab-solution.ipynb) |

Status legend: ✅ done · 🔍 review · 📈 deepen · ⚙️ realise · 🔀 merge · ✏️ rewrite · 🆕 planned
