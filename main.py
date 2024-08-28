from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="hello_world_dag",
    start_date=datetime(2011, 1, 1),
    schedule_interval="@hourly",
    catchup=False,
) as dag:

    def helloWorld():
        print("Hello World!")


task1 = PythonOperator(task_id="hello_world", python_callable=helloWorld)
