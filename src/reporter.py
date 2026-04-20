import pandas as pd
import json
import os

def generate_reports(transactions, settlement_df):
    os.makedirs("outputs", exist_ok=True)

    df = pd.DataFrame(transactions)

    df.to_csv("outputs/processed_transactions.csv", index=False)
    settlement_df.to_csv("outputs/merchant_settlement_report.csv", index=False)

    summary = {
        "total_transactions": int(len(df)),
        "valid_transactions": int(len(df[df["transaction_status"] == "VALID"])),
        "fraud_transactions": int(len(df[df["transaction_status"] == "SUSPICIOUS"])),

        "high_value_frauds": int(df["fraud_reason"].str.contains("HIGH_VALUE", na=False).sum()),
        "cross_border_frauds": int(df["fraud_reason"].str.contains("CROSS_BORDER", na=False).sum()),
        "rapid_transaction_frauds": int(df["fraud_reason"].str.contains("RAPID", na=False).sum())
    }

    with open("outputs/fraud_summary.json", "w") as f:
        json.dump(summary, f, indent=4)