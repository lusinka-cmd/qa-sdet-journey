"""Demonstration tests for evaluating variable AI-style text responses.

The samples are mocked. These tests validate the rubric and test-design approach,
not a live model or the factual correctness of any real company's policy.
"""
from ai_testing.response_rubric import ResponseCase, evaluate_response


RETURN_POLICY = ResponseCase(
    required_phrases=("14 days", "purchase"),
    forbidden_phrases=("you can return it after 20 days"),
)


def test_accepts_paraphrased_answer_that_covers_policy():
    answer = (
        "Returns are accepted within 14 days of purchase. "
        "Since 20 days have passed, this item is outside the return period."
    )

    result = evaluate_response(answer, RETURN_POLICY)

    assert result.passed
    assert result.reasons == ()


def test_rejects_answer_that_invents_a_policy_exception():
    answer = (
        "Returns are accepted within 14 days of purchase, "
        "but you can return it after 20 days."
    )

    result = evaluate_response(answer, RETURN_POLICY)

    assert not result.passed
    assert "prohibited claim" in result.reasons[0].lower()


def test_rejects_answer_that_omits_required_policy_information():
    result = evaluate_response(
        "Sorry, that return window has passed.",
        RETURN_POLICY,
    )

    assert not result.passed
    assert any("14 days" in reason for reason in result.reasons)


def test_asks_for_clarification_when_purchase_date_is_missing():
    case = ResponseCase(clarification_required=True)

    good = evaluate_response("What date did you make the purchase?", case)
    bad = evaluate_response("Yes, you can return it.", case)

    assert good.passed
    assert not bad.passed
    assert "clarification" in bad.reasons[0].lower()


def test_evaluation_is_case_and_whitespace_insensitive():
    result = evaluate_response(
        "Returns are accepted within 14 DAYS of   PURCHASE.",
        RETURN_POLICY,
    )

    assert result.passed
