# Testing Results and Qualitative Analysis

## 1. Test Environment

The Local English Study Assistant was tested using the following environment:

- Model: `HuggingFaceTB/SmolLM2-360M-Instruct`
- Framework: Hugging Face Transformers
- Interface: Streamlit
- Device: CPU
- Python: 3.12.10
- PyTorch: 2.14.0+cpu
- Transformers: 5.17.0
- Maximum output length: 150 new tokens

## 2. Unit Testing

The preprocessing and postprocessing functions were tested using pytest.

The tests covered:

- Removal of unnecessary spaces and empty lines
- Empty-input validation
- Maximum-input-length validation
- Summary, rewriting and question prompt construction
- Missing-question validation
- Invalid task and input handling
- Model-response cleaning
- Word counting
- Generation-time formatting

The tests were executed with:

```powershell
python -m pytest -v
```

Final result:

```text
[19 passed in 0.07s]
```

All implemented preprocessing and postprocessing functions operated as expected during the application tests.

## 3. Performance Results

The model was evaluated using three different prompts.

| Test | Task | Generation Time | Total Time | Memory Before | Memory After | CPU Usage | Response Length |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | Explain artificial intelligence | 5.73 s | 9.57 s | 308.17 MB | 1066.91 MB | 489.20% | 85 words |
| 2 | Benefits of AI in education | 6.99 s | 6.99 s | 1066.91 MB | 1070.35 MB | 792.20% | 108 words |
| 3 | Rewrite in simple English | 0.94 s | 0.94 s | 1070.35 MB | 1073.65 MB | 785.30% | 15 words |

Summary:

- Average generation time: **4.55 seconds**
- Highest measured process memory: **1073.65 MB**
- All three prompts generated a response successfully.
- No model-loading or generation errors occurred.

CPU usage exceeded 100% because PyTorch used multiple CPU cores during inference. This is expected and does not indicate a program error.

The first test required more total time because the tokenizer and model had to be loaded into memory. Tests 2 and 3 reused the loaded model, so their total execution time was almost identical to their generation time.

## 4. Qualitative Analysis

### Test 1: Explanation of Artificial Intelligence

Prompt:

> Explain artificial intelligence in simple English.

The model described artificial intelligence as giving computers the ability to think and learn. It also used Alexa and Google Assistant as familiar examples.

The response was:

- Relevant to the question
- Complete
- Easy to understand
- Grammatically coherent
- Suitable for a general audience

No major factual error was identified, although the explanation simplified how AI systems work.

### Test 2: Benefits of AI in Education

Prompt:

> What are three benefits of artificial intelligence in education?

The model correctly produced three benefits:

1. Personalized learning
2. Enhanced efficiency
3. Improved accessibility

The response followed the requested numbered format and provided an explanation for each point. It was relevant, coherent and complete.

Some statements were broad and would require supporting evidence in an academic report, but the answer was appropriate for a general text-generation application.

### Test 3: Simple-English Rewriting

Prompt:

> Rewrite this sentence in simple English: Artificial intelligence facilitates the automation of repetitive administrative procedures.

Model response:

> Artificial intelligence helps do all kinds of jobs that can be done easily with machines.

The rewritten sentence was shorter and easier to understand. However, it did not fully preserve the original meaning. The original sentence specifically referred to repetitive administrative procedures, while the generated response changed this to the broader phrase “all kinds of jobs.”

This shows that the model can simplify English but may remove important details.

## 5. Comparison with the Initial Test

The initial performance evaluation used a maximum output length of 100 new tokens. Two responses ended before completing their final sentences.

The maximum output length was increased to 150 new tokens, and the evaluation was repeated. After this change:

- All three responses were complete.
- Test 1 produced 85 words.
- Test 2 produced 108 words.
- Test 3 produced 15 words.
- No response ended in the middle of a sentence.

This change improved response completeness, although longer outputs required slightly more generation time.

## 6. Limitations

The testing identified the following limitations:

- SmolLM2-360M-Instruct may produce inaccurate or oversimplified information.
- Rewriting may remove important details from the original text.
- Responses vary because sampling is enabled.
- Long answers may reach the maximum token limit.
- The model primarily performs best with English input.
- CPU inference is slower than GPU inference.
- The first request is slower because the model must be loaded into memory.
- Model responses should be reviewed before being treated as factual.

## 7. Conclusion

SmolLM2-360M-Instruct was successfully integrated into the Local English Study Assistant using Hugging Face Transformers and Streamlit.

The model completed all three evaluated tasks on a CPU. The average generation time was **4.55 seconds**, and the highest measured process memory was **1073.65 MB**.

The model performed well for simple explanations and structured question answering. It also generated simplified text quickly, but the rewriting test showed that a small language model may lose specific details from the original input.

Overall, SmolLM2-360M-Instruct is suitable for a lightweight educational text-generation application, provided that users review its responses for accuracy and completeness.