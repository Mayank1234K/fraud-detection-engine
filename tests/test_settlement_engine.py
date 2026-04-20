import pandas as pd
from src.settlement_engine import generate_settlement

# ✅ Settlement calculation
def test_settlement_amount_calculation():
    merchants = pd.DataFrame([{
        "merchant_id": 1,
        "merchant_name": "Test"
    }])

    txns = [
        {"merchant_id": 1, "transaction_amount": 100, "transaction_status": "VALID"},
        {"merchant_id": 1, "transaction_amount": 200, "transaction_status": "VALID"}
    ]

    result = generate_settlement(txns, merchants)

    assert result.iloc[0]["settlement_amount"] == 300
    assert result.iloc[0]["valid_transactions"] == 2