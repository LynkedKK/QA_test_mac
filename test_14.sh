#!/usr/bin/env bash

set -ex

rm -rf github-actions-ios-emulator-tryout/.pytest_cache

cd github-actions-ios-emulator-tryout
  pipenv run python -m pytest --html=output/ios14_test.html test_ios14.py
cd -