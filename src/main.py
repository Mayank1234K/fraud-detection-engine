import logging
import os

from src.loader import load_merchants, load_transactions
from src.validator import validate_transactions
from src.fraud_engine import detect_fraud
from src.settlement_engine import generate_settlement
from src.reporter import generate_reports

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/fraud_engine.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    merchants = load_merchants("data/merchants.csv")
    transactions = load_transactions("data/transactions.csv")

    valid_txns = validate_transactions(transactions, merchants)
    processed_txns = detect_fraud(valid_txns, merchants)

    settlement_df = generate_settlement(processed_txns, merchants)

    generate_reports(processed_txns, settlement_df)

    print("Processing completed successfully!")

if __name__ == "__main__":
    main()