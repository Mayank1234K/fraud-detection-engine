from collections import defaultdict
from datetime import datetime, timedelta

def detect_fraud(transactions, merchants):
    merchant_map = merchants.set_index("merchant_id").to_dict("index")

    customer_txn_times = defaultdict(list)
    processed = []

    for row in transactions:
        fraud_flag = False
        reasons = []

        amount = row["transaction_amount"]
        merchant = merchant_map[row["merchant_id"]]

        txn_time = datetime.strptime(row["transaction_time"], "%Y-%m-%d %H:%M:%S")

        # Rule 1: High amount
        if amount > 100000:
            fraud_flag = True
            reasons.append("HIGH_VALUE_TRANSACTION")

        # Rule 2: Cross-border
        if row["country"] != merchant["country"]:
            fraud_flag = True
            reasons.append("CROSS_BORDER_TRANSACTION")

        # Rule 4: Crypto high value
        if row["payment_method"] == "CRYPTO" and amount > 50000:
            fraud_flag = True
            reasons.append("CRYPTO_HIGH_VALUE")

        # Rule 3: Rapid transactions
        customer = row["customer_id"]
        customer_txn_times[customer].append(txn_time)

        recent = [
            t for t in customer_txn_times[customer]
            if txn_time - t <= timedelta(minutes=2)
        ]

        if len(recent) > 3:
            fraud_flag = True
            reasons.append("RAPID_TRANSACTIONS")

        row["fraud_flag"] = fraud_flag
        row["fraud_reason"] = "|".join(reasons) if reasons else "NA"
        row["transaction_status"] = "SUSPICIOUS" if fraud_flag else "VALID"

        processed.append(row)

    return processed