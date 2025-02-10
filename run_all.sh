#!/bin/bash

echo "🚀 Running Playwright tests..."
pytest tests/web/test_login.py --alluredir=allure-results

echo "📊 Generating Allure report..."
allure serve allure-results
