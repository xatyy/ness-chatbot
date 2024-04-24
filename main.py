"""main.py"""
import streamlit as st
from openai import OpenAI
from streamlit_chat import message
client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])
from read_file import read_file_to_string


def api_calling(question, scenario):
    file_path = scenario + ".txt"
    file_content = read_file_to_string(file_path)
    prompt = "In the following text:" + file_content + "please answer " + question 
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt }
        ]
    )
    message = completion.choices[0].message
    return message

st.title("NessAI Movie Chatbot")
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = []
 
if 'openai_response' not in st.session_state:
    st.session_state['openai_response'] = []

def get_scenario():
    with st.container(border=True):
        scenario = st.radio(
        "Choose from 3 demo script scenarios",
        ["scenario1", "scenario2", "scenario3"],
        )
    return scenario
 
def get_text():
    input_text = st.chat_input("Message NessAI", key="input")

    return input_text
 
user_input = get_text()
user_scenario = get_scenario()
 
if user_input:
    if "birthday" in user_input:
        st.balloons()
    output = api_calling(user_input, user_scenario)
    output = output.content
 
    # Store the output
    st.session_state.openai_response.append(output)
    st.session_state.user_input.append(user_input)
 
message_history = st.empty()
 
if st.session_state['user_input']:
    for i in range(len(st.session_state['user_input']) - 1, -1, -1):
        # This function displays user input
        st.chat_message("user").write(st.session_state["user_input"][i])
        st.chat_message("assistant").write(f"NessAI: {st.session_state['openai_response'][i]}")