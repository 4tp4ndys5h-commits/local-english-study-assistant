import pytest

from src.preprocessing import (
    MAX_INPUT_CHARACTERS,
    build_prompt,
    normalize_text,
    validate_text,
)


def test_normalize_text_removes_extra_spaces():
    text = "Artificial     intelligence   is useful."

    result = normalize_text(text)

    assert result == "Artificial intelligence is useful."


def test_normalize_text_removes_empty_lines():
    text = """
    Artificial intelligence is useful.

    It can support education.
    """

    result = normalize_text(text)

    assert result == (
        "Artificial intelligence is useful.\n"
        "It can support education."
    )


def test_normalize_text_rejects_non_string_input():
    with pytest.raises(TypeError):
        normalize_text(123)


def test_validate_text_rejects_empty_input():
    with pytest.raises(ValueError, match="Please enter some text"):
        validate_text("   ")


def test_validate_text_rejects_long_input():
    long_text = "A" * (MAX_INPUT_CHARACTERS + 1)

    with pytest.raises(ValueError, match="input is too long"):
        validate_text(long_text)


def test_build_summary_prompt():
    prompt = build_prompt(
        task="summarize",
        text="AI can support personalized learning.",
    )

    assert "Summarize" in prompt
    assert "AI can support personalized learning." in prompt


def test_build_rewrite_prompt():
    prompt = build_prompt(
        task="rewrite",
        text="Artificial intelligence has many applications.",
    )

    assert "Rewrite" in prompt
    assert "simple English" in prompt
    assert "Artificial intelligence has many applications." in prompt


def test_build_question_prompt():
    prompt = build_prompt(
        task="question",
        text="AI can help teachers analyze student performance.",
        question="How can AI help teachers?",
    )

    assert "AI can help teachers analyze student performance." in prompt
    assert "How can AI help teachers?" in prompt


def test_question_task_requires_question():
    with pytest.raises(ValueError, match="Please enter a question"):
        build_prompt(
            task="question",
            text="AI is used in education.",
            question="",
        )


def test_build_prompt_rejects_invalid_task():
    with pytest.raises(ValueError, match="Invalid task"):
        build_prompt(
            task="translate",
            text="Artificial intelligence is useful.",
        )
