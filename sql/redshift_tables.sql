CREATE TABLE IF NOT EXISTS customer_transactions (
  transaction_id VARCHAR(50),
  custormer_id  VARCHAR(50),
  transactions_date TIMESTAMP,
  transaction_amount DECIMAL(18,2),
  transaction_type VARCHAR(100),
  fraud_flag VARCHAR(10)
  );
