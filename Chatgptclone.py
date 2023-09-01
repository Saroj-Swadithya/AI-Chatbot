import streamlit as st
from langchain.llms import Cohere
from langchain import PromptTemplate, LLMChain
import speech_recognition as sr
import pyaudio

template = """You are an AI assisstant that helps people solve their doubts and questions in a kind manner
Your prompt is: {question}"""
prompt=PromptTemplate(template=template, input_variables=["question"])
#llm = Cohere(cohere_api_key="YOUR COHERE API KEY")
llm_chain=LLMChain(prompt=prompt, llm=llm)
st.header("Chat GPT Clone")
userin = st.text_input('Ask me anything!')
def input_reply():
    response=llm_chain.run(userin)
    st.text(response)

def input_voice():
    warning1= st.warning('Speak now...', icon="🗣️")
    r= sr.Recognizer()
    p = pyaudio.PyAudio()
    with sr.Microphone(1) as source:
        r.adjust_for_ambient_noise(source, 1)  
        audio=r.listen(source)

    try:
        question = r.recognize_google(audio, language='en-US')
        response = llm_chain.run(question)
        st.text(response)
    except:
        pass
st.button("Submit here",on_click=input_reply())
st.button("Voice", on_click=input_voice)
