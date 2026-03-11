from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime
from scripts import extract, transform, load

def extract_step():
    # Path relative to AIRFLOW_HOME (/opt/airflow)
    df = extract.extract_data("data/raw_data.csv")
    return df

def transform_step(ti):
    # Retrieve data from XCom (return value of extract_step)
    df = ti.xcom_pull(task_ids='extract_task')
    df_transformed = transform.transform_data(df)
    return df_transformed

def load_step(ti):
    # Retrieve data from XCom (return value of transform_step)
    df_transformed = ti.xcom_pull(task_ids='transform_task')
    load.load_data(df_transformed)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['example', 'etl']
)

# Tâche de nettoyage des anciennes données (optionnel, selon le besoin)
cleanup_task = PostgresOperator(
    task_id='cleanup_old_data',
    postgres_conn_id='postgres_default',
    sql="DELETE FROM sales WHERE price < 0;", # Exemple simple de nettoyage
    dag=dag
)

extract_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract_step,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_task',
    python_callable=transform_step,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_task',
    python_callable=load_step,
    dag=dag
)

cleanup_task >> extract_task >> transform_task >> load_task
