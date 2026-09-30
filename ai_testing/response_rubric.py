"""Small, deterministic rubric for demonstrating AI-output testing.

This module evaluates sample outputs against explicit acceptance criteria. It
does not call an LLM and is not a semantic evaluator; real projects should use
human-reviewed datasets and, where appropriate, a calibrated evaluator.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class ResponseCase:
    required_phrases: tuple[str, ...] = ()
    forbidden_phrases: tuple[str, ...] = ()
    clarification_required: bool = False


@dataclass(frozen=True)
class Evaluation:
    passed: bool
    reasons: tuple[str, ...]


CLARIFICATION_MARKERS = (
    "which date",
    "what date",
    "please provide",
    "could you clarify",
    "can you clarify",
)


def evaluate_response(response: str, case: ResponseCase) -> Evaluation:
    """Check explicit, deterministic acceptance criteria for one response."""
    normalized = " ".join(response.casefold().split())
    reasons: list[str] = []

    missing = [phrase for phrase in case.required_phrases
               if phrase.casefold() not in normalized]
    if missing:
        reasons.append(f"Missing required information: {', '.join(missing)}")

    present_forbidden = [phrase for phrase in case.forbidden_phrases
                         if phrase.casefold() in normalized]
    if present_forbidden:
        reasons.append(
            f"Contains prohibited claim(s): {', '.join(present_forbidden)}"
        )

    if case.clarification_required and not any(
        marker in normalized for marker in CLARIFICATION_MARKERS
    ):
        reasons.append("Should ask the user for clarification")

    return Evaluation(passed=not reasons, reasons=tuple(reasons))
