.PHONY: requirements requirements-test requirements-dev pylint_file docs test

requirements:
	poetry export --without-hashes --without=dev,test \
	--format=requirements.txt > requirements.txt

requirements-test:
	poetry export --without-hashes --only=test \
	--format=requirements.txt > requirements-test.txt

requirements-dev:
	poetry export --without-hashes --only=dev \
	--format=requirements.txt > requirements-dev.txt

pylint_file:
	pylint --generate-rcfile > .pylintrc

test:
	pytest --cov=app/ --cov-report term-missing
