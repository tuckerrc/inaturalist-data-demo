#!/usr/bin/env bash

set -e

echo 'Cloud Query Sync'

pushd $CLOUDQUERY_PROJECT_PATH

source .env
cloudquery sync $CLOUDQUERY_CONFIG_FILENAME

popd
