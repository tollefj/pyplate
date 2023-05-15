export PYTHONPATH := $(PWD)

.PHONY: run test mypy lint format check-format install-req

run:
	python src/main.py

test:
	python -m unittest discover tests

mypy:
	mypy src --config-file mypy.ini

lint:
	flake8 src tests

format:
	black src tests
	isort src tests

check-format:
	black src tests --check
	isort src tests --check

setup:
	pip install -r requirements/requirements.txt

install-req:
	pip install -r requirements/requirements_$(TASK).txt

new:
	@read -p "Enter your repository URL: " repository_url; \
	git remote remove origin && \
	git remote add origin $$repository_url && \
	git push --set-upstream origin main