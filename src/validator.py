import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def validate_transactions(transactions, merchants):
    valid_records = []

    merchant_map = merchants.set_index("merchant_id").to_dict("index")

    for _, row in transactions.iterrows():
        try:
            if row["merchant_id"] not in merchant_map:
                logger.warning("Invalid merchant")
                continue

            merchant = merchant_map[row["merchant_id"]]

            if merchant["status"] == "BLOCKED":
                logger.warning("Blocked merchant")
                continue

            if row["transaction_amount"] <= 0:
                logger.warning("Negative amount")
                continue

            try:
                datetime.strptime(row["transaction_time"], "%Y-%m-%d %H:%M:%S")
            except:
                logger.warning("Invalid timestamp")
                continue

            valid_records.append(row.to_dict())

        except Exception as e:
            logger.error(f"Validation error: {e}")

    return valid_records