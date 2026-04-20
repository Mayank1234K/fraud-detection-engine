import pandas as pd
from src.validator import validate_transactions

def test_valid_transaction():
    merchants = pd.DataFrame([{
        "merchant_id":1,
        "status":"ACTIVE"
    }])

    transactions = pd.DataFrame([{
        "merchant_id":1,
        "transaction_amount":100,
        "transaction_time":"2025-01-01 10:00:00"
    }])

    result = validate_transactions(transactions, merchants)
    assert len(result) == 1


def test_invalid_merchant():
    merchants = pd.DataFrame(columns=["merchant_id","status"])

    transactions = pd.DataFrame([{
        "merchant_id":1,
        "transaction_amount":100,
        "transaction_time":"2025-01-01 10:00:00"
    }])

    result = validate_transactions(transactions, merchants)
    assert len(result) == 0