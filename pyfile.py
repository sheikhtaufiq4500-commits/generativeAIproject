# streamlit+langchain+ollama(LLM-gemma2:2b model)
#import required libraries 

import os
import streamlit as st

#import python builtin os 

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# set 1 --> create Prompt Template 
# this defines how AI should Behave and how it recives user input 

prompt = ChatPromptTemplate.from_messages(
    [
        # system message defines ai behaviour 
        ("system","you are a helpful assistant , please respond clearly to questions asked "),
        #user message contains placeholder {question}
        ("user","Question : {question}") 
    ]
)
# step 2 --> streamlit app UI

# streamlit title 
st.title("Langchain Demo Model(Ollama)")

# textinput box for user question 
input_txt = st.text_input("What is your question ")

# step 3 --> load ollama model 

# load local gemma model
LLM = Ollama(model="gemma2:2b")

# Condition - convert output model to string 
output_parser = StrOutputParser()

# create langchain pipeline (prompt --> model --> output_parser )
chain = prompt | LLM | output_parser 

# step 4 --> run the model when user inputs the question
if input_txt:
    response = chain.invoke({"question":input_txt})
    st.write(response)