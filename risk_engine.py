import pandas as pd


def calculate_risk_score(row, df):
    """
    Calculate a demo fraud risk score from 0 to 100.

    Factors:
    - Global transaction anomaly
    - Account behavior
    - Transaction type
    - Existing anomaly flag
    """

    amount = float(row["Amount"])
    z_score = abs(float(row["Z-Score"]))

    # -----------------------------------------
    # 1. GLOBAL AMOUNT ANOMALY
    # -----------------------------------------

    # Maximum contribution = 55 points
    amount_risk = min((z_score / 6) * 55, 55)


    # -----------------------------------------
    # 2. ACCOUNT BEHAVIOR
    # -----------------------------------------

    account = row["Account"]

    account_transactions = df[
        df["Account"] == account
    ]["Amount"]

    account_mean = account_transactions.mean()
    account_std = account_transactions.std()

    if account_std > 0:

        account_z = abs(
            (amount - account_mean) / account_std
        )

    else:

        account_z = 0


    # Maximum contribution = 25 points
    behavior_risk = min(
        (account_z / 5) * 25,
        25
    )


    # -----------------------------------------
    # 3. TRANSACTION TYPE
    # -----------------------------------------

    type_risk_map = {
        "Transfer": 10,
        "Withdrawal": 10,
        "Payment": 5,
        "Refund": 2
    }

    type_risk = type_risk_map.get(
        row["Type"],
        5
    )


    # -----------------------------------------
    # 4. ANOMALY BONUS
    # -----------------------------------------

    anomaly_bonus = 10 if z_score > 3 else 0


    # -----------------------------------------
    # FINAL SCORE
    # -----------------------------------------

    risk_score = (
        amount_risk
        + behavior_risk
        + type_risk
        + anomaly_bonus
    )

    risk_score = min(
        round(risk_score),
        100
    )


    return risk_score


def get_risk_level(score):

    if score >= 80:
        return "CRITICAL"

    elif score >= 60:
        return "HIGH"

    elif score >= 30:
        return "MODERATE"

    else:
        return "LOW"


def add_risk_scores(df):

    df = df.copy()

    df["Risk Score"] = df.apply(
        lambda row: calculate_risk_score(
            row,
            df
        ),
        axis=1
    )

    df["Risk Level"] = df[
        "Risk Score"
    ].apply(get_risk_level)

    return df