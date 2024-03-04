#!/usr/bin/env bash

set -e

echo "Run dbt run"

pushd $DBT_PROJECT_PATH

source $DBT_VIRTUALENV_ACTIVATE_PATH
dbt run --profiles-dir $DBT_PROFILES_DIR

deactivate
popd
