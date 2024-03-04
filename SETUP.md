# Setup

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
export APACHE_AIRFLOW=/home/tuckerc/Code/airflow-testing/airflow
```

Run Apache Airflow in standalone mode (Not great for production but works well in this case)

```bash
airflow standalone
```

## CloudQuery

Run the gRPC server for the iNaturalist sourcer plugin (This is also not the best way to do it but it works for the demo)

```bash
cd ~/Code/cloudquery-inaturalist-sourcer
source ~/.virtualenvs/cq-inat-sourcer/bin/activate
poetry run main serve
```

## dbt


