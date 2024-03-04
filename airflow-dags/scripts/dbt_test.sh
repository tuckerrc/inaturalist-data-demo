#!/usr/bin/env bash

set -e

echo "Run dbt test"

pushd $DBT_PROJECT_PATH

source $DBT_VIRTUALENV_ACTIVATE_PATH
dbt test --profiles-dir $DBT_PROFILES_DIR

deactivate
popd
