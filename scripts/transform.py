import pandas as pd

def transform_data():
  print("Starting data tranformation...")

  df = pd.read_csv("data/extracted_transactions.csv")

  #Remove null values
  df.dropna(inplace=True)

  #Remove duplicates
  df.drop_duplicates(inplace=True)

  # Example transformation:
  # Add fraud flag if transaction > 10000
  df['fraud_flag']=df['trnaformation_amount'].apply(
    lambda x: 'YES' if x > 10000 else 'NO'
  )

  df.to_csv("data/transformed_transactions.csv", index=False)

  print(f"Transformed {len(df)} clean records")
  print("Transformation completeds successfully")
