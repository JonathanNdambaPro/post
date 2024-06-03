.PHONY: test test_unit requirements requirements-test requirements-dev


test:
	pytest --cov=dags/ingestion_pipelines/tasks/operators/ --cov=dags/ingestion_pipelines/tasks/operators/scripts --cov=dags/ingestion_pipelines/common --cov=dags/ingestion_pipelines/datacatalog --cov=dispatcher/ --cov=dqm/ --cov-report term-missing -vv --cov-fail-under=80

test_unit:
	pytest tests/unit_tests --cov=dags/ingestion_pipelines/tasks/operators/ --cov=dags/ingestion_pipelines/tasks/operators/scripts --cov=dispatcher/ --cov=dqm/ --cov-report term-missing -vv --cov-fail-under=81

requirements:
	poetry export --without-hashes --without=dev,test --format=requirements.txt > requirements.txt

requirements-test:
	poetry export --without-hashes --only=test --format=requirements.txt > requirements-test.txt

requirements-dev:
	poetry export --without-hashes --only=dev --format=requirements.txt > requirements-dev.txt