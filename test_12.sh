#!/usr/bin/env bash

set -ex

rm -rf github-actions-ios-emulator-tryout/.pytest_cache

cd github-actions-ios-emulator-tryout
  pipenv run python -m pytest --html=output_ios12/index.html test_ios12.py
cd -