.PHONY: help install test lint format type-check security clean build proto docs

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	poetry install
	poetry run pre-commit install

test: ## Run tests with coverage
	poetry run pytest tests/ --cov=src --cov-report=html --cov-report=term

lint: ## Run linting checks
	poetry run flake8 src/ tests/

format: ## Format code with black and isort
	poetry run black src/ tests/
	poetry run isort src/ tests/

format-check: ## Check code formatting
	poetry run black --check src/ tests/
	poetry run isort --check-only src/ tests/

type-check: ## Run type checking
	poetry run mypy src/

security: ## Run security scans
	poetry run bandit -r src/
	poetry run safety check

clean: ## Clean build artifacts
	@if (Test-Path "build") { Remove-Item -Recurse -Force "build" }
	@if (Test-Path "dist") { Remove-Item -Recurse -Force "dist" }  
	@if (Test-Path "*.egg-info") { Remove-Item -Recurse -Force "*.egg-info" }
	@if (Test-Path ".coverage") { Remove-Item -Force ".coverage" }
	@if (Test-Path "htmlcov") { Remove-Item -Recurse -Force "htmlcov" }
	@if (Test-Path ".pytest_cache") { Remove-Item -Recurse -Force ".pytest_cache" }
	@if (Test-Path ".mypy_cache") { Remove-Item -Recurse -Force ".mypy_cache" }
	@Get-ChildItem -Recurse -Directory -Name "__pycache__" | Remove-Item -Recurse -Force
	@Get-ChildItem -Recurse -File -Name "*.pyc" | Remove-Item -Force

build: ## Build package
	poetry build

proto: ## Generate protobuf files
	poetry run python -m grpc_tools.protoc \
		--proto_path=proto \
		--python_out=src \
		--grpc_python_out=src \
		proto/*.proto

docs: ## Generate documentation
	@echo "Documentation generation not implemented yet"

all-checks: format-check lint type-check security test ## Run all quality checks

ci: proto all-checks ## Run CI pipeline locally
