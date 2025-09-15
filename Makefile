
# FastAPI Article Project — Makefile (uv-based)
.PHONY: help venv install run test lint format typecheck check lock clean pre-commit-install pre-commit-run pre-commit-autoupdate

help:
	@echo "Common commands: run, test, lint, format, typecheck, check, pre-commit-install"

venv:
	uv venv

install:
	uv pip install -e ".[dev]"

run:
	uv run uvicorn app.main:app --reload

test:
	uv run pytest -q

lint:
	uv run ruff check .

format:
	uv run ruff format .

typecheck:
	uv run mypy app tests

check: lint typecheck

lock:
	uv lock

clean:
	rm -rf .pytest_cache .ruff_cache .mypy_cache dist build **/__pycache__ *.egg-info

pre-commit-install:
	uv run pre-commit install

pre-commit-run:
	uv run pre-commit run --all-files

pre-commit-autoupdate:
	uv run pre-commit autoupdate
