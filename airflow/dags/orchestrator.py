from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.standard.operators.python import PythonOperator

# def safe_main_callable():
#     print("This is a safe main callable for the orchestrator DAG.")
#     from insert_records import main
#     return main()

def safe_main_callable():
    import sys
    print("This is a safe main callable for the orchestrator DAG.")
    sys.path.append("/opt/airflow/api-request")

    from insert_records import main
    return main()


default_args = {
    "description": "Orchestrator DAG for weather data project",
    "start_date": datetime(2026, 1, 1),
    "catchup": False,
}

dag = DAG(
    dag_id="orchestrator",
    default_args=default_args,
    schedule=timedelta(minutes=1),
)

with dag:

    start = PythonOperator(
        task_id="start_task",
        python_callable=safe_main_callable
    )

