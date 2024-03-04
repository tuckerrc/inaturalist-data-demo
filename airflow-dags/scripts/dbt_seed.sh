#!/usr/bin/env bash

set -e

echo "Run dbt seed"

pushd $DBT_PROJECT_PATH

source $DBT_VIRTUALENV_ACTIVATE_PATH
dbt seed --profiles-dir $DBT_PROFILES_DIR

deactivate
popd