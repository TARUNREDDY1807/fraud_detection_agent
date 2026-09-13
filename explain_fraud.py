import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

explanation_prompt = PromptTemplate.from_template("""
You are a financial fraud detection assistant.

A financial transaction has been flagged as potentially suspicious.

Transaction ID: {transaction_id}
Amount: ${amount}
Type: {type}
Account: {account}
Z-Score: {z_score}

Explain:
1. Why this transaction may be suspicious.
2. What the Z-score means.
3. What the finance team should verify.

Do not say that the transaction is definitely fraudulent.
Give a professional and concise explanation.
""")


def explain_transaction(row):

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.3,
        api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = explanation_prompt.format(
        transaction_id=row["Transaction ID"],
        amount=row["Amount"],
        type=row["Type"],
        account=row["Account"],
        z_score=round(row["Z-Score"], 2)
    )

    response = llm.invoke(prompt)

    return response.content