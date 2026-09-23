MAX_INPUT_CHARACTERS = 4000

VALID_TASKS = {
    "summarize",
    "rewrite",
    "question",
}


def normalize_text(text):
    """Remove unnecessary spaces from user input."""

    if not isinstance(text, str):
        raise TypeError("The input must be text.")

    cleaned_lines = []

    for line in text.splitlines():
        cleaned_line = " ".join(line.split())

        if cleaned_line:
            cleaned_lines.append(cleaned_line)

    return "\n".join(cleaned_lines)


def validate_text(text):
    """Validate and clean the main user input."""

    cleaned_text = normalize_text(text)

    if not cleaned_text:
        raise ValueError("Please enter some text.")

    if len(cleaned_text) > MAX_INPUT_CHARACTERS:
        raise ValueError(
            f"The input is too long. "
            f"Please use no more than {MAX_INPUT_CHARACTERS} characters."
        )

    return cleaned_text


def build_prompt(task, text, question=""):
    """Build a task-specific prompt for SmolLM2."""

    if not isinstance(task, str):
        raise TypeError("The task must be text.")

    normalized_task = task.strip().lower()

    if normalized_task not in VALID_TASKS:
        raise ValueError(
            "Invalid task. Choose summarize, rewrite, or question."
        )

    cleaned_text = validate_text(text)

    if normalized_task == "summarize":
        return (
            "Summarize the following text in clear and simple English. "
            "Include only the important points.\n\n"
            f"Text:\n{cleaned_text}"
        )

    if normalized_task == "rewrite":
        return (
            "Rewrite the following text using simple English. "
            "Keep the original meaning and do not add new facts.\n\n"
            f"Text:\n{cleaned_text}"
        )

    cleaned_question = normalize_text(question)

    if not cleaned_question:
        raise ValueError("Please enter a question.")

    return (
        "Answer the question using the information in the text. "
        "If the answer is not provided in the text, say that the "
        "information is not available.\n\n"
        f"Text:\n{cleaned_text}\n\n"
        f"Question:\n{cleaned_question}"
    )


if __name__ == "__main__":
    sample_text = """
    Artificial intelligence allows computers to perform tasks
    that normally require human intelligence.
    """

    prompt = build_prompt(
        task="summarize",
        text=sample_text,
    )

    print("Generated prompt:")
    print(prompt)
