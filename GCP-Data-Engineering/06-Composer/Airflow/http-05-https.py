"""Example HTTP operator and sensor"""

from __future__ import annotations

import json
import os
from datetime import datetime

from airflow import DAG
from airflow.providers.http.operators.http import HttpOperator
from airflow.providers.http.sensors.http import HttpSensor

ENV_ID = os.environ.get("SYSTEM_TESTS_ENV_ID")

DAG_ID = "https_employee_list_02"



dag = DAG(
    DAG_ID,
    default_args={"retries": 1},
    tags=["https_emp_list"],
    start_date=datetime(2021, 1, 1),
    catchup=False,
)


dag.doc_md = __doc__

# task_post_op, task_get_op and task_put_op are examples of tasks created by instantiating operators


# [START howto_operator_http_task_get_op_response_filter]
task_get_op_response_filter = HttpOperator(
    task_id="get_op_response_filter",
    http_conn_id='dummy-api',
    method="GET",
    endpoint="api/v1/employees",
    response_filter=lambda response: response.json()["nested"]["property"],
    dag=dag,
)
# [END howto_operator_http_task_get_op_response_filter]

task_get_op_response_filter 