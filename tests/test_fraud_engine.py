import pandas as pd
from src.fraud_engine import detect_fraud

def merchants():
    return pd.DataFrame([{"merchant_id":1,"country":"IN"}])


# ✅ High value
def test_high_value_transaction():
    txns = [{
        "merchant_id":1,
        "transaction_amount":200000,
        "transaction_time":"2025-01-01 10:00:00",
        "customer_id":1,
        "payment_method":"CARD",
        "country":"IN"
    }]
    result = detect_fraud(txns, merchants())
    assert "HIGH_VALUE_TRANSACTION" in result[0]["fraud_reason"]


# ✅ Cross-border
def test_cross_border_transaction():
    txns = [{
        "merchant_id":1,
        "transaction_amount":100,
        "transaction_time":"2025-01-01 10:00:00",
        "customer_id":1,
        "payment_method":"CARD",
        "country":"US"
    }]
    result = detect_fraud(txns, merchants())
    assert "CROSS_BORDER_TRANSACTION" in result[0]["fraud_reason"]


# ✅ Crypto rule
def test_crypto_high_value():
    txns = [{
        "merchant_id":1,
        "transaction_amount":60000,
        "transaction_time":"2025-01-01 10:00:00",
        "customer_id":1,
        "payment_method":"CRYPTO",
        "country":"IN"
    }]
    result = detect_fraud(txns, merchants())
    assert "CRYPTO_HIGH_VALUE" in result[0]["fraud_reason"]


# ✅ Rapid transactions
def test_rapid_transactions():
    txns = []
    for i in range(4):
        txns.append({
            "merchant_id":1,
            "transaction_amount":100,
            "transaction_time":f"2025-01-01 10:00:0{i}",
            "customer_id":1,
            "payment_method":"CARD",
            "country":"IN"
        })

    result = detect_fraud(txns, merchants())
    assert "RAPID_TRANSACTIONS" in result[-1]["fraud_reason"]


# ✅ Valid (no fraud)
def test_valid_transaction():
    txns = [{
        "merchant_id":1,
        "transaction_amount":100,
        "transaction_time":"2025-01-01 10:00:00",
        "customer_id":1,
        "payment_method":"CARD",
        "country":"IN"
    }]
    result = detect_fraud(txns, merchants())
    assert result[0]["transaction_status"] == "VALID"