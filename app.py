import streamlit as st

from src.model import generate_response
from src.postprocessing import count_words, format_generation_time
from src.preprocessing import MAX_INPUT_CHARACTERS, build_prompt


st.set_page_config(
    page_title="Local English Study Assistant",
    page_icon="🤖",
    layout="centered",
)


TASK_OPTIONS = {
    "Summarize": "summarize",
    "Rewrite in Simple English": "rewrite",
    "Ask a Question": "question",
}


st.title("Local English Study Assistant")

st.write(
    "This application uses SmolLM2-360M-Instruct to summarize, "
    "rewrite, and answer questions about English text."
)

st.caption(
    "The model runs locally using Hugging Face Transformers."
)


with st.sidebar:
    st.header("Project Information")

    st.write("**Model:** SmolLM2-360M-Instruct")
    st.write("**Framework:** Hugging Face Transformers")
    st.write("**Interface:** Streamlit")
    st.write("**Device:** CPU")

    st.divider()

    st.write(
        "SmolLM2 is a small language model. "
        "Its responses may contain inaccurate information."
    )


selected_label = st.selectbox(
    "Choose a task",
    options=list(TASK_OPTIONS.keys()),
)

selected_task = TASK_OPTIONS[selected_label]


input_text = st.text_area(
    "Enter the English text",
    height=220,
    max_chars=MAX_INPUT_CHARACTERS,
    placeholder=(
        "Paste or type the English text that you want the model "
        "to summarize, rewrite, or answer questions about."
    ),
)

st.caption(
    f"Character count: {len(input_text)} / {MAX_INPUT_CHARACTERS}"
)


question = ""

if selected_task == "question":
    question = st.text_input(
        "Enter your question",
        placeholder="What would you like to know about the text?",
    )


generate_button = st.button(
    "Generate Response",
    type="primary",
)


if generate_button:
    try:
        prompt = build_prompt(
            task=selected_task,
            text=input_text,
            question=question,
        )

        with st.spinner(
            "Loading SmolLM2 and generating the response..."
        ):
            response, elapsed_time = generate_response(
                prompt=prompt,
                max_new_tokens=150,
            )

        response_words = count_words(response)
        formatted_time = format_generation_time(elapsed_time)

        st.success("Response generated successfully.")

        st.subheader("Model Response")
        st.write(response)

        time_column, word_column = st.columns(2)

        with time_column:
            st.metric(
                label="Generation Time",
                value=formatted_time,
            )

        with word_column:
            st.metric(
                label="Response Length",
                value=f"{response_words} words",
            )

    except (ValueError, TypeError) as error:
        st.warning(str(error))

    except Exception as error:
        st.error(
            "An unexpected error occurred while generating "
            f"the response: {error}"
        )


st.divider()

st.caption(
    "AI Assignment 1A – Local LLM Application"
)
