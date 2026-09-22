import pandas as pd
from scipy.stats import pearsonr

def test_required_columns():
    df = pd.read_csv("tests/fixtures/synthetic_students.csv")
    assert "study_time" in df.columns
    assert "final_score" in df.columns

def test_no_missing_values():
    df = pd.read_csv("tests/fixtures/synthetic_students.csv")
    assert df["study_time"].notna().all()
    assert df["final_score"].notna().all()

def test_sample_size():
    df = pd.read_csv("tests/fixtures/synthetic_students.csv")
    assert len(df) == 10

def test_positive_association():
    df = pd.read_csv("tests/fixtures/synthetic_students.csv")
    correlation, p_value = pearsonr(
        df["study_time"],
        df["final_score"]
    )
    assert correlation > 0
