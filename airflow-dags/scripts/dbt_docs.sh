#!/usr/bin/env bash

set -e

echo "Run dbt docs"

pushd $DBT_PROJECT_PATH

source $DBT_VIRTUALENV_ACTIVATE_PATH
dbt docs generate --profiles-dir $DBT_PROFILES_DIR

deactivate
popd
