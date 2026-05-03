import pandas as pd

def extract_data():
  print("Starting data extraction...")

  df = pd.read_csv("data/sample_transactions.csv")

  print(f"Extracted {len(df)} records")

  df.tc_csv("data/extracted_transactions.csv", index=False)

  print("Extraction completed successfully")
