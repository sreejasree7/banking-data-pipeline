import pandas as pd

def load_to_redshift():
  print("Starting Redshift load simulation...")

df = pd.read_csv("data/transformed_transactions.csv")

#Real project:
#Replace this with psycopg2 / SQLAlchemy
#and COPY command to Redshift

print(f"Loaded {len(df)} records to Redshift")

print("Redshift load completed successfully")
