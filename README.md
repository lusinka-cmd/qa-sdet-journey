# QA Automation Portfolio — Python, Pytest & Playwright

A compact QA/SDET portfolio demonstrating maintainable UI, API, and business-logic automation.

## What this project demonstrates

- UI automation with Playwright and the Page Object Model
- API validation with Requests and Pytest
- Positive and negative test coverage
- Reusable fixtures and deterministic assertions
- Headless CI execution with GitHub Actions
- Clean test naming and repository structure

## Tech stack

- Python 3.11+
- Pytest
- Playwright
- Requests
- GitHub Actions

## Project structure

```text
.
├── api/                 # API tests
├── pages/               # Page Objects
├── tests/               # UI and logic tests
├── conftest.py          # Shared Playwright fixture
└── .github/workflows/   # CI pipeline
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install chromium
```

On macOS/Linux, activate the environment with `source .venv/bin/activate`.

## Run tests

```bash
pytest
pytest tests/test_login.py
pytest api/
pytest tests/test_ui.py
```

UI tests run headlessly by default for reliable local and CI execution.

## Test coverage

- Login validation: parameterized accepted and rejected credentials
- SauceDemo UI: successful login, inventory verification, and invalid-login error handling
- Fake Store API: response status, collection structure, and product schema checks

## CI

GitHub Actions installs dependencies and Chromium, then runs the complete Pytest suite on every push and pull request.

> Portfolio project by Lusine Karapetyan — Senior QA Engineer transitioning deeper into QA Automation/SDET.
