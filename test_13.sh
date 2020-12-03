#!/usr/bin/env bash

set -ex

rm -rf github-actions-ios-emulator-tryout/.pytest_cache

git pull

cd github-actions-ios-emulator-tryout
  pipenv run python -m pytest --html=output_ios13/index.html test_ios13.py
cd -