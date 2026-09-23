import pytest

from src.postprocessing import (
    clean_response,
    count_words,
    format_generation_time,
)


def test_clean_response_removes_extra_spaces():
    response = "Artificial     intelligence   is useful."

    result = clean_response(response)

    assert result == "Artificial intelligence is useful."


def test_clean_response_removes_empty_lines():
    response = """
    AI can support education.

    It can provide feedback.
    """

    result = clean_response(response)

    assert result == (
        "AI can support education.\n"
        "It can provide feedback."
    )


def test_clean_response_handles_empty_output():
    result = clean_response("   ")

    assert result == "The model did not generate a response."


def test_clean_response_rejects_non_string_input():
    with pytest.raises(TypeError):
        clean_response(None)


def test_count_words():
    result = count_words(
        "Artificial intelligence can support education."
    )

    assert result == 5


def test_count_words_handles_empty_text():
    result = count_words("")

    assert result == 0


def test_count_words_rejects_non_string_input():
    with pytest.raises(TypeError):
        count_words(123)


def test_format_generation_time():
    result = format_generation_time(4.687)

    assert result == "4.69 seconds"


def test_format_generation_time_rejects_negative_value():
    with pytest.raises(
        ValueError,
        match="Generation time cannot be negative",
    ):
        format_generation_time(-1.0)
