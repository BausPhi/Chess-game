echo "Tests"
python -m coverage run tests/runner.py
echo "Coverage:"
coverage report
coverage html -d coverage_reports/
rm .coverage
cd coverage_reports || exit
/usr/bin/open Firefox 'localhost:8000'
python3 -m http.server