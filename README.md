## Local English Study Assistant

## AI Large Language Model Assignment 1A

Local English Study Assistant is a lightweight application built with SmolLM2-360M-Instruct, Hugging Face Transformers and Streamlit.

The model runs locally on a CPU without requiring a paid API.

## Group Members

| [Student Name] | [Student Number] |
| [Bruce] | [P2319796] |
| [Billy] | [P2303322] |


## Features

The application provides three functions:

- **Summarize:** Summarizes an English passage.
- **Rewrite:** Rewrites complex text using simpler English.
- **Ask a Question:** Answers a question based on a supplied passage.

The application also displays:

- Generation time
- Response word count
- Input character count
- Input-validation messages

## Model and Technologies

- Model: `HuggingFaceTB/SmolLM2-360M-Instruct`
- Model page: https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct
- Python 3.12
- PyTorch
- Hugging Face Transformers
- Streamlit
- pytest
- psutil

SmolLM2-360M-Instruct was selected because it is small enough to run locally on a normal CPU and does not require a paid API.

## Project Structure

```text
ai-assessment1/
├── src/
│   ├── __init__.py
│   ├── model.py
│   ├── preprocessing.py
│   └── postprocessing.py
├── tests/
│   ├── __init__.py
│   ├── test_preprocessing.py
│   └── test_postprocessing.py
├── videos/
├── app.py
├── performance_evaluation.py
├── requirements.txt
├── RESULTS.md
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the Repository

```powershell
git clone [YOUR_GITHUB_REPOSITORY_URL]
cd ai-assessment1
```

### 2. Create a Virtual Environment

```powershell
python -m venv .venv
```

### 3. Activate the Environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the script:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the environment again.

### 4. Install Dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The required packages are:

```text
torch
transformers
accelerate
streamlit
pytest
psutil
```

## Running the Application

Run:

```powershell
python -m streamlit run app.py
```

Open the following address if the browser does not open automatically:

```text
http://localhost:8501
```

Press `Ctrl + C` in the terminal to stop the application.

## Running Unit Tests

Run:

```powershell
python -m pytest -v
```

The tests check:

- Input normalization
- Empty-input validation
- Maximum input length
- Prompt construction
- Invalid tasks
- Missing questions
- Model-output cleaning
- Word counting
- Generation-time formatting

Final pytest result:

```text
[19 passed in 0.07s]
```

## Performance Evaluation

Run:

```powershell
python performance_evaluation.py
```

The model was evaluated on a CPU with a maximum output length of 150 new tokens.

| Test | Task | Generation Time | Total Time | Memory After | CPU Usage | Words |
|---|---|---:|---:|---:|---:|---:|
| 1 | Explain artificial intelligence | 5.73 s | 9.57 s | 1066.91 MB | 489.20% | 85 |
| 2 | Benefits of AI in education | 6.99 s | 6.99 s | 1070.35 MB | 792.20% | 108 |
| 3 | Rewrite in simple English | 0.94 s | 0.94 s | 1073.65 MB | 785.30% | 15 |

Summary:

- Average generation time: **4.55 seconds**
- Highest measured process memory: **1073.65 MB**

CPU usage exceeded 100% because PyTorch used multiple CPU cores during inference.

The first test had a longer total execution time because the tokenizer and model had to be loaded into memory. The later tests reused the loaded model.

## Qualitative Results

### Test 1: Explain Artificial Intelligence

The response was complete, relevant and easy to understand. It explained AI using the idea of a smart helper and included familiar examples such as Alexa and Google Assistant.

### Test 2: Benefits of AI in Education

The response correctly provided three benefits:

1. Personalized learning
2. Improved efficiency
3. Improved accessibility

The response was complete, clearly structured and relevant to the question.

### Test 3: Simple-English Rewriting

The response was short and easy to understand. However, it was less precise than the original sentence because it did not clearly preserve the ideas of repetitive administrative procedures.

This demonstrates that a small model can simplify text but may lose some details from the original meaning.

More detailed analysis is available in `RESULTS.md`.

## Limitations

- The model may generate inaccurate information.
- SmolLM2-360M performs best with English input.
- Responses may vary because sampling is enabled.
- Simplified text may lose details from the original meaning.
- Long responses may reach the maximum token limit.
- CPU inference is slower than GPU inference.
- Generated responses should be checked by the user.

## Demonstration Videos

### Installation



### Implementation



### Testing


Suggested filenames:

```text
[p2303322 p2319796] _ [LocalEnglishStudyAssistant_1]_1-installation.mp4
[p2303322 p2319796] _ [LocalEnglishStudyAssistant_1]_2-implementation.mp4
[p2303322 p2319796] _ [LocalEnglishStudyAssistant_1]_3-testing.mp4
```

## Conclusion

SmolLM2-360M-Instruct was successfully integrated with Hugging Face Transformers and Streamlit.

The application can summarize English text, rewrite text in simpler English and answer questions about a passage. The model achieved an average generation time of 4.55 seconds on a CPU, with a highest measured process memory usage of 1073.65 MB.

The results show that SmolLM2-360M-Instruct is suitable for lightweight local text-generation tasks, although its answers should be checked for accuracy and completeness.

## References

- SmolLM GitHub: https://github.com/huggingface/smollm
- SmolLM2-360M-Instruct: https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct
- Transformers: https://github.com/huggingface/transformers
- Streamlit: https://docs.streamlit.io/
- pytest: https://docs.pytest.org/