# AI Test Case Agent Demo

A small portfolio demo for an AI-assisted QA workflow. It reads synthetic requirements and existing test cases, asks an LLM to identify coverage gaps and likely duplicates, and drafts pytest/Playwright tests for human review.

## What the demo does

1. Reads `examples/requirements.md` and `examples/existing_tests.json`.
2. Sends those inputs plus explicit test-generation criteria to the OpenAI Responses API.
3. Produces `output/agent_report.json` and `output/draft_tests.py`.
4. Does not run, import, or execute generated test code. A tester reviews it first.

The sample is a login workflow with synthetic data. Do not put production requirements, personal information, credentials, or confidential test cases into this demo.

## Requirements

- Python 3.11 or newer
- An OpenAI API key with API access and available billing/credits
- Internet access for the model request

ChatGPT Plus does not include API usage. API requests may incur separate charges.

## Run on Windows PowerShell

From this folder:

```powershell
$env:OPENAI_API_KEY = "your-api-key"
$env:OPENAI_MODEL = "gpt-4.1-mini"
python .\agent.py
```

The API key is read from the environment and is never written into this project. Do not commit a real key.

## Run offline checks

These tests do not call the API and do not require an API key:

```powershell
python -m unittest discover -s tests -v
```

## Review the result

Open `output/agent_report.json` to inspect missing coverage, likely duplicates, assumptions, and generated drafts. Open `output/draft_tests.py` and review every locator, assertion, fixture, and test-data assumption. Adapt the draft to your real project's fixtures and Page Objects, run it in a safe test environment, and verify the result yourself.

## How to explain it in an interview

> “I built a small AI-assisted test-generation demo. It takes requirements and existing test cases, asks an agent to identify coverage gaps and likely duplicates, and draft Playwright tests using defined criteria. The output is saved for human review; the demo never executes generated code automatically. I check each suggestion against the requirement and run only reviewed tests.”

Be clear that this is a portfolio demo, not a production deployment.
