#!/usr/bin/env bash

set -ex

rm -rf github-actions-ios-emulator-tryout/.pytest_cache

git fetch --all

git pull

cd src
  pipenv run python -m pytest --json-report --json-report-file=test_IOS12.json	 --html=./output_ios12/index.html test_json_metadata.py
cd -

# cd github-actions-ios-emulator-tryout
#   pipenv run python -m pytest --json-report --json-report-file=test_IOS12.json	 --html=./output_ios12/index.html test_json_metadata.py
# cd -