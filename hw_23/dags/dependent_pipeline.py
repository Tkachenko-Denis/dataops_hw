from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="dependent_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["hw23"],
) as dag:
    extract = BashOperator(
        task_id="extract",
        bash_command="echo 'extract step'",
    )

    transform = BashOperator(
        task_id="transform",
        bash_command="echo 'transform step'",
    )

    load = BashOperator(
        task_id="load",
        bash_command="echo 'load step'",
    )

    extract >> transform >> load
