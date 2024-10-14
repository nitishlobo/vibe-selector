# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# MAKEFILE
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# General variables
PYTHON = python3
VENV_DIR = .venv
PYTEST_CMD = python -m pytest -vv -rfEsP --maxfail=1 --tb=long --color=yes --code-highlight=yes
PYTEST_CMD_WITH_THREADING = $(PYTEST_CMD) -n 5

.PHONY: help clean clean-build clean-pyc clean-test test install-lint update-lint lint

help:
	@echo "-----------------------------------------------------------------------------------------------------------"
	@echo "RUN"
	@echo "  run                            run the FastAPI app locally"
	@echo "-----------------------------------------------------------------------------------------------------------"
	@echo "TEST"
	@echo "  test                           run all unit and integration tests"
	@echo "  test-slow-only                 run only slow tests"
	@echo "  test-not-slow-only             run only tests that are not slow"
	@echo "  test-only-integration-tests    run only integration tests"
	@echo "  test-only-unit-tests           run only unit tests"
	@echo "-----------------------------------------------------------------------------------------------------------"
	@echo "LINT"
	@echo "  install-lint                   install python linting tools"
	@echo "  update-lint                    update python linting tools"
	@echo "  lint                           run autopep8, ruff, black and other linting tools on staged files"
	@echo "  lint-all                       run autopep8, ruff, black and other linting tools on the entire repo"
	@echo "-----------------------------------------------------------------------------------------------------------"
	@echo "CLEAN"
	@echo "  clean                          clean build, test, coverage, python artifacts and AWS outputs"
	@echo "  clean-build                    clean python build artifacts"
	@echo "  clean-pyc                      clean python file artifacts"
	@echo "  clean-lint                     clean python file artifacts"
	@echo "  clean-test                     clean python test and coverage artifacts"
	@echo "-----------------------------------------------------------------------------------------------------------"

run:
	cd src && uvicorn main:main_app --reload

test:
	pytest

test-only-slow-tests:
	pytest -m "slow"

test-only-fast-tests:
	pytest -m "not slow"

test-only-integration-tests:
	pytest -m "integration"

test-only-unit-tests:
	pytest -m "not integration"

# Remove all build, test, coverage and python artifacts.
clean: clean-build clean-pyc clean-lint clean-test

# Set up the git hook scripts
install-lint:
	pip install pre-commit
	pre-commit install

# Update version numbers of each pre-commit hook
update-lint:
	pre-commit autoupdate

# Run pre-commit hooks on staged files
# Note: you can run a specific pre-commit by doing:
# `pre-commit run black`
# Note: if you want to run ruff (isort module) manually:
# `ruff check --select I .`
# See docs/fond-dev-guide/content/lint for more.
lint:
	pre-commit run

# Run pre-commit hooks on entire repo
lint-all:
	pre-commit run -a

# -------------------------------------------------------------------------------------------------
# OS specific commands - please uncomment the relevant section depending on your OS
# -------------------------------------------------------------------------------------------------
# MacOS / Linux

# Remove build artifacts
clean-build:
	find . -name '.eggs' -exec rm -fr {} +
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

# Remove Python file artifacts
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

# Remove lint artifacts
clean-lint:
	find . -name '.ruff_cache' -exec rm -fr {} +
	find . -name '.mypy_cache' -exec rm -fr {} +

# Remove test and coverage artifacts
clean-test:
	find . -name '.pytest_cache' -exec rm -fr {} +
	find . -name 'htmlcov' -exec rm -fr {} +
	find . -name '.coverage' -exec rm -fr {} +

# -------------------------------------------------------------------------------------------------
# Windows

# # Remove build artifacts
# clean-build:
# 	for /d /r %%p in (.eggs, *.egg-info, *.egg) do  @if exist "%%p" rmdir /s /q "%%p"

# # Remove lint artifacts
# clean-lint:
# 	for /d /r %%p in (.ruff_cache, .mypy_cache) do  @if exist "%%p" rmdir /s /q "%%p"

# # Remove Python file artifacts
# clean-pyc:
# 	for /d /r %%p in (__pycache__) do  @if exist "%%p" rmdir /s /q "%%p"
# 	for /d /r %%p in (*.pyc, *.pyo, *~) do  @if exist "%%p" del /s /f /q "%%p"

# # Remove test and coverage artifacts
# clean-test:
# 	for /d /r %%p in (.pytest_cache, htmlcov) do  @if exist "%%p" rmdir /s /q "%%p"
# 	for /d /r %%p in (.coverage) do  @if exist "%%p" del /s /f /q "%%p"
