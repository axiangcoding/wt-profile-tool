.PHONY: setup test test_in_ci lint format


setup:
	poetry install --with test,lint,typing

test:
	poetry run pytest --cov=./wt_profile_tool --cov-report=term

test_in_ci:
	poetry run pytest --cov=./wt_profile_tool --cov-report=xml

lint:
	poetry run ruff check ./wt_profile_tool ./tests
	poetry run mypy ./wt_profile_tool ./tests

format:
	poetry run ruff --fix ./wt_profile_tool ./tests
	poetry run ruff format ./wt_profile_tool ./tests