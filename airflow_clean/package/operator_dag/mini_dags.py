from airflow import DAG
from airflow.utils.task_group import TaskGroup

import operator_dag
import operator_dag.operator

def generate_dag(dag: DAG, **kwargs) -> TaskGroup:
    with TaskGroup(
        group_id="my_mini_dags",
        dag=dag,
    ) as task_group:
        task_1 = operator_dag.operator.MyOperator1(**kwargs, dag=dag)
        task_2 = operator_dag.operator.MyOperator2(**kwargs, dag=dag)

        task_1 >> task_2

    return task_group