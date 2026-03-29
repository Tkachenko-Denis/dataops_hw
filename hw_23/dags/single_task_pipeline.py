from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="single_task_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["hw23"],
) as dag:
    BashOperator(
        task_id="print_hello",
        bash_command="echo 'hello from single task pipeline'",
    )
