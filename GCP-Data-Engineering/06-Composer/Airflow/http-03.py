#https://www.youtube.com/watch?v=KR0xmwxQGg8&list=PL7B3mwEXCi-aLpjswSYJkaiCehxQ2Xz39&index=5
"""Demo HTTP operators"""
from __future__ import annotations

import json
import os
from datetime import datetime
from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator

def handle_response(response):
    if response.status_code == 200:
        print ("Recived 200 OK")
        return True
    else:
        print("error")
        return False


dag = DAG('01_03-DAG-HTTP_Employee', start_date=datetime(2024,1,1), schedule_interval=timedelta(days=1))

list_emp=SimpleHttpOperator(
    task_id='list_emp',
    method='GET',
    http_conn_id='employee',
    headers={'Content-Type': 'application/json'},
    endpoint="api/v1/employees",
    #response_filter = lambda response : json.loads(response.text),
    response_check= lambda response: handle_response(response),
    dag=dag
)

list_emp