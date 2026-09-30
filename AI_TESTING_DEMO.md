# AI Output Testing Demo

This is a small interview-preparation example in `ai_testing/response_rubric.py`
and `tests/test_ai_output_rubric.py`.

It demonstrates how to test AI-style responses against explicit acceptance
criteria without requiring exact sentence matching. The sample scenario uses a
hypothetical 14-day return policy and covers:

- a correct paraphrased answer;
- an invented exception (hallucination);
- a missing required fact;
- an ambiguous request that should trigger a clarification question;
- case and whitespace variation.

The responses are mocked. The demo does **not** call an AI model and does not
prove that a model is accurate. The phrase-based rubric is deliberately limited:
it is suitable for deterministic examples, not nuanced semantic judgments.
A production evaluation should use a reviewed dataset, clear scoring guidance,
representative and adversarial prompts, privacy-safe logging, and human review
for ambiguous results. After prompt/model changes, rerun the same dataset and
compare pass rates and failure categories.

Run locally:

```bash
pytest tests/test_ai_output_rubric.py
```

Interview framing: “I already use Pytest for deterministic API, UI, and business
logic checks. For AI outputs, I would preserve those checks and add a reviewed
prompt dataset with criteria such as correctness, relevance, safety, and
clarification behavior. I would avoid exact text matching when several
wordings can be correct.”
