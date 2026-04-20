import pandas as pd

def generate_settlement(transactions, merchants):
    df = pd.DataFrame(transactions)

    result = []

    for merchant_id, group in df.groupby("merchant_id"):
        merchant_info = merchants[merchants["merchant_id"] == merchant_id].iloc[0]

        total = len(group)
        valid = len(group[group["transaction_status"] == "VALID"])
        fraud = len(group[group["transaction_status"] == "SUSPICIOUS"])

        settlement_amount = group[group["transaction_status"] == "VALID"]["transaction_amount"].sum()

        result.append({
            "merchant_id": merchant_id,
            "merchant_name": merchant_info["merchant_name"],
            "total_transactions": total,
            "valid_transactions": valid,
            "fraud_transactions": fraud,
            "settlement_amount": settlement_amount
        })

    return pd.DataFrame(result)