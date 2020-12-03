#!/usr/bin/env bash

set -ex

rm -rf github-actions-ios-emulator-tryout/.pytest_cache

cd github-actions-ios-emulator-tryout
  pipenv run python -m pytest --html=output/ios12_test.html test_ios12.py
cd -