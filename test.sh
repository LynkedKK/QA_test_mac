#!/usr/bin/env bash

set -ex

rm -rf github-actions-ios-emulator-tryout/.pytest_cache

pipenv run python -m pytest --html=output/ios13_test.h
tml test_ios13.py