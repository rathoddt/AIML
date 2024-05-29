"""A liveness prober dag for monitoring composer.googleapis.com/environment/healthy."""
import os 
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash_operator import BashOperator
#import airflow
import requests

yesterday = datetime.combine(datetime.today()-timedelta(1),datetime.min.time())


default_args = {
    #'start_date': airflow.utils.dates.days_ago(0),
    'start_date': yesterday,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def print_hello():
    print('----- Hay I am Python Operator ----')

def handle_http():
    url="http://35.187.43.128/hello.html"
    print("Calling HTTP: ", url)
    r = requests.get(url)
    print(r.status_code)
    print(r.headers)
    print(r.content) 
    print(r.text)
    

with DAG(
    dag_id='01_05_http-apache-bash-py',
    default_args=default_args,
    description='liveness monitoring dag',
    #schedule_interval='*/10 * * * *',
    schedule_interval=timedelta(days=1),
    max_active_runs=2,
    catchup=False,
    #dagrun_timeout=timedelta(minutes=10),
    ) as dag: 
    
    # Dummy Tasks start here
    start = DummyOperator(
        task_id = 'start',
        dag=dag
    )

    bash_task = BashOperator(
        task_id='bash_task',
        bash_command="date; echo 'Hey I am bash operator'; curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' -X GET 'http://35.187.43.128/hello.html' ",
        dag=dag,
        #depends_on_past=False,
        #priority_weight=2**31 - 1,
        #do_xcom_push=False
    )
    python_task = PythonOperator(
        task_id ="python_task",
        #python_callable = print_hello,
        python_callable = handle_http,
        dag = dag 
    )

    #Dummay end task
    end = DummyOperator(
        task_id="end",
        dag = dag
    )

# Setting up task dependencies using airflow operators
start >> bash_task >>  python_task >> end