#### from https://github.com/portkeys/chatOutside
#### author: https://github.com/portkeys

import os
import pandas as pd
from PIL import Image
from streamlit_chat import message
from langchain.chains import ConversationChain
from langchain.llms import OpenAI
# import supporting funcitons
from utils import *

openai.api_key = st.secrets["OPENAI_KEY"]
# For Langchain
os.environ["OPENAI_API_KEY"] = openai.api_key


# ==== Section 1: Streamlit Settings ======
with st.sidebar:
    st.markdown("# Welcome to chatOutside 🙌")
    st.markdown(
        "**chatOutside** allows you to talk to version of **chatGPT** \n"
        "that has access to latest Outside content!  \n"
        )
    st.markdown(
        "Unlike chatGPT, chatOutside can't make stuff up\n"
        "and will answer from Outside knowledge base. \n"
    )
    st.markdown("👩‍🏫 Developer: Wen Yang")
    st.markdown("---")
    st.markdown("# Under The Hood 🎩 🐇")
    st.markdown("How to Prevent Large Language Model (LLM) hallucination?")
    st.markdown("- **Pinecone**: vector database for Outside knowledge")
    st.markdown("- **Langchain**: to remember the context of the conversation")


st.title("chatOutside: Outside + ChatGPT")

image = Image.open('/home/cdsw/pattern.jpg')

st.image(image, caption='Get Outside!')

st.header("chatGPT 🤖")


# ====== Section 2: ChatGPT only ======
def chatgpt(prompt):
    res = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system",
             "content": "You are a friendly and helpful assistant. "
                        "Answer the question as truthfully as possible. "
                        "If unsure, say you don't know."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )["choices"][0]["message"]["content"]

    return res


input_gpt = st.text_input(label='Chat here! 💬')
output_gpt = st.text_area(label="Answered by chatGPT:",
                          value=chatgpt(input_gpt), height=200)


   
