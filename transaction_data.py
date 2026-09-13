import pandas as pd
import numpy as np


def generate_transactions(n=100):
    np.random.seed(42)

    amounts = np.random.normal(
        loc=200,
        scale=50,
        size=n
    )

    # Create some unusually large transactions
    fraud_indices = np.random.randint(0, n, 5)

    amounts[fraud_indices] *= np.random.randint(5, 10)

    transactions = pd.DataFrame({
        "Transaction ID": [
            f"TX-{i+1:04d}" for i in range(n)
        ],
        "Amount": amounts.round(2),
        "Type": np.random.choice(
            ["Payment", "Refund", "Transfer", "Withdrawal"],
            size=n
        ),
        "Account": np.random.choice(
            ["A101", "A102", "A103"],
            size=n
        )
    })

    return transactions