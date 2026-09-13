import pandas as pd


def flag_anomalies(df: pd.DataFrame):

    threshold = 3

    mean = df["Amount"].mean()
    std = df["Amount"].std()

    df["Z-Score"] = (
        (df["Amount"] - mean) / std
    )

    df["Flagged"] = (
        df["Z-Score"].abs() > threshold
    )

    return df