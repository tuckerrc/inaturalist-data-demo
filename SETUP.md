# Setup

Instructions for setup (change paths for your setup)

## Install and Start Apache Airflow

Create and/or source python venv

```bash
python3 -m venv ~/.virtualenvs/airflow-testing
source ~/.virtualenvs/airflow-testing/bin/activate
```

Install apache airflow

```bash
pip install apache-airflow
```

Make sure to export the AIRFLOW_HOME env

```bash
export APACHE_HOME=$HOME/tuckerc/Code/airflow-testing/airflow
```

Copy or symlink dags to the `$APACHE_HOME` directory

```bash
ln -s ~/Code/airflow-dags $APACHE_HOME/dags
```

Run Apache Airflow in standalone mode (Not great for production but works well
for a demo)

```bash
airflow standalone
```

## Database

I used Postgres with `docker compose`.

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:latest
    container_name: postgres_airflow_data
    environment:
      POSTGRES_DB: airflow
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
    ports:
      - "5432:5432"
    volumes:
      - pgdata-airflow:/var/lib/postgresql/data

volumes:
  pgdata-airflow:

```

## CloudQuery

Run the gRPC server for the iNaturalist sourcer plugin (This is also not the
best but it works for a demo). I use tmux to get the gRPC server running in the
background and I can come back to it if needed.

```bash
cd ~/Code/cloudquery-inaturalist-sourcer
source ~/.virtualenvs/cq-inat-sourcer/bin/activate
poetry run main serve
```

**Note**: If this was a production system I would build and publish (privately)
the Docker image and use that in the config instead of a separate running gRPC
server


You need to login manually and download the postgres module for `cloudquery` to work.

```bash
cloudquery login
## Follow any instructinos
```

**Note**: I couldn't figure out how to use the cloudquery repo anonymously.

Create a `.env` file that exports the `POSTGRESQL_CONNECTION_STRING` (this file
is sourced in the airflow task)

```bash
# .env
export POSTGRESQL_CONNECTION_STRING=postgresql://airflow:airflow@localhost:5432/airflow?sslmode=disable
```

## dbt

Create a python virtual environment and install dbt (I used the apache airflow venv for this)

```bash
python3 -m venv ~/.virtualenvs/airflow-testing
source ~/.virtualenvs/airflow-testing/bin/activate
pip install dbt-postgres
```

Create and populate a `~/.dbt/profiles.yml` file
([docs](https://docs.getdbt.com/docs/core/connect-data-platform/profiles.yml)). 

**Note**: In my case I only used a single target (`dev`) but with a production
environment having separate targes (`dev`, `stg`, `prd`) would be better.

## Airflow variables

A few variables are required for the airflow dag

```python
cloudquery_project_path ## path to cloudquery project
cloudquery_config_filename ## path to cloudquery config file
dbt_project_path ## path to dbt project
dbt_profiles_dir ## path to dbt profiles directory
dbt_virtualenv_path ## path to virtualenv with dbt-postgres installed
```
