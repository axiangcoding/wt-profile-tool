.PHONY: setup test lint format


setup:
	poetry install

test:
	pytest

lint:
	poetry run ruff check ./wt_profile_tool ./tests

format:
	poetry run ruff format ./wt_profile_tool ./tests
	poetry run ruff --fix ./wt_profile_tool ./tests