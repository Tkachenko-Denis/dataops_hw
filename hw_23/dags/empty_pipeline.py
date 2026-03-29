from __future__ import annotations

from datetime import datetime

from airflow import DAG


with DAG(
    dag_id="empty_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["hw23"],
):
    pass
