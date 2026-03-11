from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts import extract, transform, load

def etl():
    # Path relative to AIRFLOW_HOME (/opt/airflow)
    df = extract.extract_data("data/raw_data.csv")
    df = transform.transform_data(df)
    load.load_data(df)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
)

etl_task = PythonOperator(
    task_id='run_etl',
    python_callable=etl,
    dag=dag
)
