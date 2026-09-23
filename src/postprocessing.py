import re


def clean_response(response):
    """Clean unnecessary spaces from the model response."""

    if not isinstance(response, str):
        raise TypeError("The model response must be text.")

    cleaned_lines = []

    for line in response.splitlines():
        cleaned_line = re.sub(r"[ \t]+", " ", line).strip()

        if cleaned_line:
            cleaned_lines.append(cleaned_line)

    cleaned_response = "\n".join(cleaned_lines).strip()

    if not cleaned_response:
        return "The model did not generate a response."

    return cleaned_response


def count_words(text):
    """Count the number of words in a piece of text."""

    if not isinstance(text, str):
        raise TypeError("The input must be text.")

    return len(text.split())


def format_generation_time(seconds):
    """Format the model generation time."""

    if seconds < 0:
        raise ValueError("Generation time cannot be negative.")

    return f"{seconds:.2f} seconds"


if __name__ == "__main__":
    sample_response = """
    Artificial   intelligence helps computers learn.

    It can be used in education and healthcare.
    """

    cleaned = clean_response(sample_response)

    print("Cleaned response:")
    print(cleaned)

    print("\nWord count:")
    print(count_words(cleaned))

    print("\nGeneration time:")
    print(format_generation_time(4.687))
