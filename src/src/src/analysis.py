import pandas as pd
from scipy.stats import pearsonr, spearmanr
import statsmodels.api as sm

def run_analysis(file_path):
    df = pd.read_csv(file_path)

    df = df.drop_duplicates()
    df = df.dropna(subset=["study_time", "final_score"])

    pearson_r, pearson_p = pearsonr(
        df["study_time"], df["final_score"]
    )

    spearman_r, spearman_p = spearmanr(
        df["study_time"], df["final_score"]
    )

    X = sm.add_constant(df["study_time"])
    y = df["final_score"]

    model = sm.OLS(y, X).fit()

    print("Sample size:", len(df))
    print("Pearson correlation:", pearson_r)
    print("Pearson p-value:", pearson_p)
    print("Spearman correlation:", spearman_r)
    print("Spearman p-value:", spearman_p)

    print("Regression coefficient:",
          model.params["study_time"])

    print("95% CI:",
          model.conf_int().loc["study_time"].tolist())

    print("Regression p-value:",
          model.pvalues["study_time"])

    print("R-squared:", model.rsquared)


if __name__ == "__main__":
    run_analysis("data/raw/students.csv")
