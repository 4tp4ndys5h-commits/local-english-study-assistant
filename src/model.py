import time

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from src.postprocessing import clean_response


MODEL_ID = "HuggingFaceTB/SmolLM2-360M-Instruct"

tokenizer = None
model = None


def load_model():
    """Load the tokenizer and language model."""

    global tokenizer, model

    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

    print("Loading model...")
    model = AutoModelForCausalLM.from_pretrained(MODEL_ID)

    model.to("cpu")
    model.eval()

    print("Model loaded successfully.")


def generate_response(prompt, max_new_tokens=150):
    """Generate a response for a user prompt."""

    if not prompt or not prompt.strip():
        raise ValueError("The prompt cannot be empty.")

    if model is None or tokenizer is None:
        load_model()

    messages = [
        {
            "role": "user",
            "content": prompt.strip(),
        }
    ]

    formatted_prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    inputs = tokenizer(
        formatted_prompt,
        return_tensors="pt",
    )

    start_time = time.perf_counter()

    with torch.inference_mode():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.1,
            pad_token_id=tokenizer.eos_token_id,
        )

    elapsed_time = time.perf_counter() - start_time

    input_length = inputs["input_ids"].shape[1]
    generated_tokens = output_ids[0][input_length:]

    response = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True,
    )

    cleaned_response = clean_response(response)

    return cleaned_response, elapsed_time


if __name__ == "__main__":
    test_prompt = "What are three benefits of using artificial intelligence in education."

    print("\nTest prompt:")
    print(test_prompt)

    answer, duration = generate_response(test_prompt)

    print("\nModel response:")
    print(answer)

    print(f"\nGeneration time: {duration:.2f} seconds")
