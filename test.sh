#!/usr/bin/env bash

set -ex

rm -rf /home/logic/_workspace/LynkedKK/QA_test_mac/github-actions-ios-emulator-tryout/.pytest_cache

cd github-actions-ios-emulator-tryout
  pipenv run python  -m pytest --html=output/ios14_test.html .
cd ..
