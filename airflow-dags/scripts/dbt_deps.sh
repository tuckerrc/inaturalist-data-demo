#!/usr/bin/env bash

set -e

echo "Run dbt deps if needed"

pushd $DBT_PROJECT_PATH

source $DBT_VIRTUALENV_ACTIVATE_PATH
if [ $DBT_DEPS_REQUIRED = "1"]; then
  dbt deps --profiles-dir $DBT_PROFILES_DIR
else
  echo 'dbt deps not required'
fi

deactivate
popd
