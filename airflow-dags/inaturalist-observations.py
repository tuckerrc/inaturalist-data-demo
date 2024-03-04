#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from datetime import timedelta
from textwrap import dedent

from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.models import Variable
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': "@daily",
}
with DAG(
    'inaturalist-observations',
    default_args=default_args,
    description='Download Observations from iNaturalist',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    catchup=False,
    tags=['inaturalist', 'dbt', 'cloudquery'],
) as dag:

    cloudquery_project_path = Variable.get("cloudquery_project_path")
    cloudquery_config_filename = Variable.get("cloudquery_config_filename")
    dbt_project_path = Variable.get("dbt_project_path")
    dbt_profiles_dir = Variable.get('dbt_profiles_dir')
    dbt_virtualenv_path = Variable.get("dbt_virtualenv_path")
    dbt_env = {
            "DBT_PROJECT_PATH": dbt_project_path,
            "DBT_PROFILES_DIR": dbt_profiles_dir,
            "DBT_DEPS_REQUIRED": "0",
            "DBT_VIRTUALENV_ACTIVATE_PATH": dbt_virtualenv_path,
    }

    t1 = BashOperator(
        task_id='cloudquery_sync',
        bash_command='scripts/cloudquery_sync.sh',
        env={
            "CLOUDQUERY_PROJECT_PATH": cloudquery_project_path,
            "CLOUDQUERY_CONFIG_FILENAME": cloudquery_config_filename
        }
    )

    t2 = BashOperator(
        task_id='dbt_deps',
        bash_command='scripts/dbt_deps.sh',
        env=dbt_env
    )

    t3 = BashOperator(
        task_id='dbt_run',
        bash_command='scripts/dbt_run.sh',
        env=dbt_env
    )

    t4 = BashOperator(
        task_id='dbt_test',
        bash_command='scripts/dbt_test.sh',
        env=dbt_env
    )

    t5 = BashOperator(
        task_id='dbt_docs',
        bash_command='scripts/dbt_docs.sh',
        env=dbt_env
    )

    t1 >> t2 >> t3 >> t4 >> t5
