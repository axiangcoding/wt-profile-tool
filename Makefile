.PHONY: setup test test_in_ci lint format


setup:
	poetry install

test:
	poetry run pytest -vv --cov=./wt_profile_tool

test_in_ci:
	poetry run pytest --cov=./wt_profile_tool --cov-report=xml

lint:
	poetry run ruff check ./wt_profile_tool ./tests

format:
	poetry run ruff --fix ./wt_profile_tool ./tests
	poetry run ruff format ./wt_profile_tool ./tests