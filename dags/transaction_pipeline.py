#This is the transactions dag

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from scripts.extract import extract_data
from script.transform import tranform_data
from script.load_redshift import load_to_redshift

default_args = {
  'owner': 'sreeja',
  'depends_on_past': False,
  'email':['sreejasree7@gmail.com'],
  'email_on_failure': True,
  'email_on_retry': False,
  'retries': 2,
  'retry_delay': timedelta(minute=5),
}

with DAG(
  dag_id='banking_transaction_pipeline',
  default_args=default_args,
  description='Airflow DAG for AWS S3+Redshift EFT Pipeline',
  schedule_interval='@daily',
  start_date=datetime(2025,1,1),
  catchup=False,
  tags=['aws','airflow','redshift','datapipeline'],
) as dag:

  extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data
  )

  transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data
  )

  load_task = PythonOperator(
    task_id='load_to_redshift',
    python_callable=load_to_redshift
  )

 extract_task >> transform_task >> load_task
