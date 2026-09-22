# Analysis Preregistration

## 1. Research Question

Does study time have an association with students' final exam performance?

## 2. Hypothesis

Students with higher study time will have higher final exam scores.

## 3. Population

The population consists of students represented in the selected student performance dataset.

## 4. Exposure

The exposure variable is study time per week.

## 5. Comparator

Students with lower study time will be compared with students with higher study time.

## 6. Outcome

The primary outcome is final exam score.

## 7. Observation Window

The observation window is the academic period represented by the selected dataset.

## 8. Exclusion Rules

The following observations will be excluded:

- Duplicate records
- Records with missing study-time values
- Records with missing final-score values

Observations will not be removed based on their final score.

## 9. Data Transformations

- Study time will be represented as a numeric variable.
- Final exam score will remain on its original scale.
- Missing values will be handled according to the exclusion rules.

## 10. Primary Statistical Analysis

Pearson correlation will be used to estimate the association between study time and final exam score.

The analysis will report:

- Correlation coefficient (r)
- p-value
- Sample size

## 11. Secondary Statistical Analysis

A linear regression model will be fitted:

Final Score = β0 + β1(Study Time) + error

The analysis will report:

- Regression coefficient
- 95% confidence interval
- p-value
- R-squared

## 12. Significance Level

The significance level will be:

α = 0.05

## 13. Effect Sizes

The following effect sizes will be reported:

- Pearson correlation coefficient
- Regression coefficient
- R-squared

## 14. Robustness Checks

The following robustness checks will be performed:

1. Spearman rank correlation
2. Analysis excluding pre-defined extreme study-time observations
3. Comparison of primary and robustness estimates

## 15. Expected Outputs

The analysis will produce:

- Number of observations
- Pearson correlation
- Spearman correlation
- Regression coefficient
- 95% confidence interval
- p-value
- R-squared
- Robustness analysis results

## 16. Reproducibility

All analysis steps will be implemented using Python.

The computational environment is specified in `environment.yml`.

Synthetic data will be used to test the analysis pipeline before applying it to the real dataset.
