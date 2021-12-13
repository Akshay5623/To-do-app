#!/bin/bash

source venv/bin/activate

python3 -m pytest --cov=application --junitxml=junit_report.xml --cov-report xml:coverage.xml