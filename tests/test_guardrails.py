"""Guardrail tests: PII and length run without OpenAI; intent tests require OPENAI_API_KEY."""

import os

import pytest

from guardrails import run_guardrails


def _nr(**kw):
    return dict(check_pii=True, check_length=True, check_intent=False, **kw)


@pytest.mark.parametrize(
    ("query", "answers", "kwargs", "expected"),
    [
        ("What is quantum computing?", [], _nr(), True),
        ("Impact of AI on healthcare", ["Europe", "Last 5 years"], _nr(), True),
        ("Research about siva@example.com", [], _nr(), False),
        ("Call me at +44 1234 567890", [], _nr(), False),
        ("My postcode is SW1A 1AA", [], _nr(), False),
        ("", [], _nr(), False),
        ("A" * 2500, [], _nr(), False),
        ("Short", ["A" * 8000], _nr(), False),
        (
            "Research topic\nRecipient email: test@example.com",
            [],
            dict(check_pii=True, check_length=True, check_intent=False, allow_recipient_email=True),
            True,
        ),
    ],
)
def test_guardrails_no_intent(query, answers, kwargs, expected):
    result = run_guardrails(query, answers, **kwargs)
    assert result.passed is expected


@pytest.mark.skipif(not os.environ.get("OPENAI_API_KEY"), reason="OPENAI_API_KEY required for intent guardrail")
@pytest.mark.parametrize(
    ("query", "expected"),
    [
        ("Write a poem about cats", False),
        ("Tell me a joke", False),
    ],
)
def test_guardrails_intent(query, expected):
    result = run_guardrails(query, [], check_pii=True, check_intent=True, check_length=True)
    assert result.passed is expected
