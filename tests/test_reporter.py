import pandas as pd
import os
from src.reporter import generate_reports

def test_generate_reports(tmp_path):
    transactions = [{
        "transaction_id":1,
        "merchant_id":1,
        "customer_id":1,
        "transaction_amount":100,
        "transaction_time":"2025-01-01 10:00:00",
        "fraud_flag":False,
        "fraud_reason":"NA",
        "transaction_status":"VALID"
    }]

    settlement_df = pd.DataFrame([{
        "merchant_id":1,
        "merchant_name":"Test",
        "total_transactions":1,
        "valid_transactions":1,
        "fraud_transactions":0,
        "settlement_amount":100
    }])

    os.chdir(tmp_path)

    generate_reports(transactions, settlement_df)

    assert os.path.exists("outputs/processed_transactions.csv")
    assert os.path.exists("outputs/merchant_settlement_report.csv")
    assert os.path.exists("outputs/fraud_summary.json")