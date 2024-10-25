import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag = DAG(
    dag_id='spark_airflow',
    default_args={
        'owner': 'airflow',
        'start_date': airflow.utils.dates.days_ago(1)
    },
    schedule_interval='@daily'
)

start = PythonOperator(
    task_id='start',
    python_callable=lambda: print('start'),
    dag=dag
)

python_job = SparkSubmitOperator(
    task_id='python_job',
    conn_id='spark_con',
    application="jobs/wordcountjob.py",
    dag=dag
)

end = PythonOperator(
    task_id="end",
    python_callable=lambda: print("Jobs completed successfully"),
    dag=dag
)
start >> python_job >> end
