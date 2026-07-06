---
name: nature-data
description: "Process, analyze, and visualize experimental data for Nature-style publications. Covers statistical analysis, data cleaning, transformation, and reproducible analysis pipelines."
version: 1.0.0
author: Adapted from Yuan1z0825/nature-skills (26.4k stars)
license: Apache-2.0
metadata:
  hermes:
    tags: [academic, data-analysis, statistics, visualization, python, R]
    related_skills: [nature-figure, nature-writing]
    category: research
---

# Nature Data

Process, analyze, and visualize experimental data for Nature-style publications. Covers statistical analysis, data cleaning, transformation, and reproducible analysis pipelines.

## When to Use

Use this skill when analyzing:
- Experimental data for manuscript preparation
- Statistical analysis for Nature-style papers
- Data cleaning and preprocessing pipelines
- Reproducible analysis workflows
- Data transformation (normalization, batch correction)
- Statistical reporting (test selection, effect sizes)

Trigger phrases: "数据分析", "data analysis", "statistics", "统计", "数据处理", "数据清洗", "分析数据"

## Core Principles

1. **Reproducible pipeline** — Every analysis step must be scripted and repeatable. No manual Excel steps.
2. **Statistical rigor** — Choose tests based on data distribution and experimental design, not convention.
3. **Transparent reporting** — Report exact p-values, effect sizes, confidence intervals, and sample sizes.
4. **Nature standards** — Follow Nature's statistical reporting guidelines.
5. **Auditable** — Every transformation documented. Raw data preserved.

## Statistical Guidelines (Nature)

### Test Selection
| Data Type | Comparison | Recommended Test |
|-----------|-----------|-----------------|
| Normal, unpaired | Two groups | Student's t-test (two-sided) |
| Normal, paired | Two groups | Paired t-test |
| Non-normal, unpaired | Two groups | Mann-Whitney U test |
| Normal | Three+ groups | ANOVA (one-way or two-way) |
| Non-normal | Three+ groups | Kruskal-Wallis test |
| Categorical | Association | Chi-square or Fisher's exact |
| Correlation | Association | Pearson (normal) or Spearman (non-normal) |
| Survival | Time-to-event | Log-rank test / Cox regression |

### Reporting Requirements
- Report **exact p-values** (not just p<0.05)
- Use p<0.001 for very small values, not p<0.0001
- Always report **effect size** and **confidence interval**
- State **sample size** (n) and what n represents (biological replicates? technical replicates?)
- Define **error bars** (SD? SEM? CI?) in every figure legend
- Specify **post-hoc test** when using ANOVA
- Report **multiple testing correction** method (Bonferroni, FDR, Holm)

## Workflow

### Phase 1: Data Intake
- Load raw data (CSV, Excel, HDF5, etc.)
- Understand experimental design
- Identify variables, groups, replicates
- Check for missing values and outliers

### Phase 2: Data Cleaning
- Handle missing values (explicitly, never silently)
- Identify and flag outliers (Grubbs' test, IQR, or domain knowledge)
- Normalize/transform as needed
- Document every transformation

### Phase 3: Analysis
- Choose appropriate statistical tests
- Run analysis with diagnostic checks
- Generate summary statistics (mean, median, SD, SEM, CI)
- Create publication-ready tables

### Phase 4: Export
- Results summary for manuscript
- Statistical report (test name, test statistic, df, p-value, effect size, CI)
- Figure-ready data (long format for ggplot/matplotlib)
- Full script for reproducibility

## Code Templates

### Python (scipy)
```python
from scipy import stats

# Two-sample t-test
t_stat, p_val = stats.ttest_ind(group1, group2, equal_var=True)

# Mann-Whitney U
u_stat, p_val = stats.mannwhitneyu(group1, group2, alternative='two-sided')

# One-way ANOVA
f_stat, p_val = stats.f_oneway(group1, group2, group3)

# Effect size (Cohen's d)
def cohens_d(g1, g2):
    n1, n2 = len(g1), len(g2)
    s1, s2 = g1.var(ddof=1), g2.var(ddof=1)
    s_pool = ((n1-1)*s1 + (n2-1)*s2) / (n1+n2-2)
    return (g1.mean() - g2.mean()) / s_pool**0.5
```

### R
```r
# Two-sample t-test
t.test(group1, group2, paired = FALSE)

# Wilcoxon/Mann-Whitney
wilcox.test(group1, group2)

# ANOVA
aov(value ~ group, data = df) |> summary()

# Effect size (Cohen's d)
library(effsize)
cohen.d(group1, group2)
```

## Anti-Patterns

1. **p-hacking** — Running multiple tests until one is significant. Pre-register analyses.
2. **Ignoring assumptions** — Using t-test without checking normality. Using ANOVA without checking homoscedasticity.
3. **SEM vs SD confusion** — SEM describes precision of mean; SD describes variability. Use SD for descriptive stats, SEM or CI for group comparisons.
4. **Optional stopping** — Adding samples until significant. Predefine sample sizes.
5. **Cherry-picking** — Reporting only significant results. Report all analyses.
6. **Missing data transparency** — Not reporting excluded data points and why.

## Verification

- [ ] Raw data preserved (never overwritten)
- [ ] Test chosen based on data distribution and design
- [ ] Assumptions checked (normality, variance homogeneity)
- [ ] Exact p-values reported
- [ ] Effect size and CI reported
- [ ] Multiple testing correction applied where needed
- [ ] Error bars clearly defined in figure legends
- [ ] Full reproducible script available
- [ ] Sample size (n) and what n represents clearly stated
