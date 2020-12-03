#!/usr/bin/env bash

set -ex

rm -rf github-actions-ios-emulator-tryout/.pytest_cache

git fetch --all

git pull

cd github-actions-ios-emulator-tryout
  pipenv run python -m pytest --html=output_ios14/index.html test_ios14.py
cd -