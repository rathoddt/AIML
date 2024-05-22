"""Demo HTTP operators"""
from __future__ import annotations

import json
import os
from datetime import datetime

from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.operators.python import PythonOperator
from google.cloud import storage

# Dag name
DAG_ID = "01_01-DAG-HTTP"


# DAG definitions with all required params
dag = DAG(
    DAG_ID,
    default_args={"retries": 1},
    tags=["example"],
    start_date=datetime(2023, 4, 26),
    catchup=False,
)

# Task to get data from given HTTP end point
get_http_data = SimpleHttpOperator(
    task_id="get_http_data",
    http_conn_id="http_conn_id_demo",
    method="GET",
    endpoint="query?function=TOURNAMENT_PORTFOLIO&season=2021-09&apikey=demo",
    response_filter = lambda response : json.loads(response.text),
    dag=dag
)

# Task dependency set
get_http_data 