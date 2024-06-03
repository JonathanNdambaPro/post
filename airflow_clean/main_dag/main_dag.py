from airflow import DAG

from package.operator_dag.mini_dags import generate_dag
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG("my_dag",
  start_date=datetime(2023, 1 ,1),
  schedule='@daily',
  catchup=False
):
    task_general = generate_dag()

    task_specialized_1 = EmptyOperator(
    task_id='task_specialized_1',
    )

    task_general >> task_specialized_1
