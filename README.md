# Payment Transaction Fraud Detection & Settlement Engine

## 📌 Project Overview
This project implements a Python-based fraud detection and settlement engine for processing payment transactions.

The system validates transactions, applies fraud detection rules, and generates settlement reports for merchants.

---

## 🎯 Features

- Load merchant and transaction data
- Validate transaction records
- Detect fraud using rule-based logic
- Identify rapid transactions within time window
- Generate settlement reports per merchant
- Export processed transaction data
- Provide fraud summary metrics
- Unit testing with high coverage

---

## ⚙️ Fraud Detection Rules

1. **High Value Transaction**
   - Amount > 100000  
   → Flag: `HIGH_VALUE_TRANSACTION`

2. **Cross Border Transaction**
   - Transaction country ≠ Merchant country  
   → Flag: `CROSS_BORDER_TRANSACTION`

3. **Rapid Transactions**
   - More than 3 transactions within 2 minutes (same customer)  
   → Flag: `RAPID_TRANSACTIONS`

4. **Crypto High Value**
   - Payment method = CRYPTO AND amount > 50000  
   → Flag: `CRYPTO_HIGH_VALUE`

---

## ✅ Validation Rules

Transactions are rejected if:
- Merchant does not exist
- Merchant is BLOCKED
- Transaction amount ≤ 0
- Invalid timestamp

---

## 💰 Settlement Logic

- Only **VALID transactions** are included
- Settlement Amount = Sum of valid transaction amounts per merchant

---

## 📂 Output Files

### 1. processed_transactions.csv
Contains:
- transaction_id
- merchant_id
- customer_id
- transaction_amount
- transaction_time
- fraud_flag
- fraud_reason
- transaction_status

---

### 2. merchant_settlement_report.csv
Contains:
- merchant_id
- merchant_name
- total_transactions
- valid_transactions
- fraud_transactions
- settlement_amount

---

### 3. fraud_summary.json
Contains:
- total_transactions
- valid_transactions
- fraud_transactions
- high_value_frauds
- cross_border_frauds
- rapid_transaction_frauds

---

## 🧪 Unit Testing

Framework used: **pytest**

### Run tests:
```bash
python -m pytest