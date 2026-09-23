import time

import psutil

from src.model import generate_response
from src.postprocessing import count_words


TEST_PROMPTS = [
    (
        "Explain artificial intelligence in simple English."
    ),
    (
        "What are three benefits of artificial intelligence "
        "in education?"
    ),
    (
        "Rewrite this sentence in simple English: "
        "Artificial intelligence facilitates the automation "
        "of repetitive administrative procedures."
    ),
]


def megabytes(number_of_bytes):
    """Convert bytes into megabytes."""

    return number_of_bytes / (1024 * 1024)


def run_performance_evaluation():
    """Evaluate model latency and process resource usage."""

    process = psutil.Process()

    results = []

    print("SmolLM2-360M-Instruct Performance Evaluation")
    print("=" * 55)

    for test_number, prompt in enumerate(TEST_PROMPTS, start=1):
        print(f"\nTest {test_number}")
        print(f"Prompt: {prompt}")

        memory_before = megabytes(
            process.memory_info().rss
        )

        process.cpu_percent(interval=None)

        total_start_time = time.perf_counter()

        response, generation_time = generate_response(
            prompt=prompt,
            max_new_tokens=150,
        )

        total_elapsed_time = (
            time.perf_counter() - total_start_time
        )

        cpu_usage = process.cpu_percent(interval=None)

        memory_after = megabytes(
            process.memory_info().rss
        )

        response_word_count = count_words(response)

        result = {
            "test_number": test_number,
            "generation_time": generation_time,
            "total_time": total_elapsed_time,
            "memory_before": memory_before,
            "memory_after": memory_after,
            "cpu_usage": cpu_usage,
            "word_count": response_word_count,
        }

        results.append(result)

        print("\nResponse:")
        print(response)

        print("\nMeasurements:")
        print(
            f"Generation time: {generation_time:.2f} seconds"
        )
        print(
            f"Total execution time: {total_elapsed_time:.2f} seconds"
        )
        print(
            f"Memory before: {memory_before:.2f} MB"
        )
        print(
            f"Memory after: {memory_after:.2f} MB"
        )
        print(
            f"Process CPU usage: {cpu_usage:.2f}%"
        )
        print(
            f"Response length: {response_word_count} words"
        )

        print("-" * 55)

    average_generation_time = sum(
        result["generation_time"] for result in results
    ) / len(results)

    highest_memory_usage = max(
        result["memory_after"] for result in results
    )

    print("\nEvaluation Summary")
    print("=" * 55)
    print(
        f"Average generation time: "
        f"{average_generation_time:.2f} seconds"
    )
    print(
        f"Highest measured process memory: "
        f"{highest_memory_usage:.2f} MB"
    )


if __name__ == "__main__":
    run_performance_evaluation()
