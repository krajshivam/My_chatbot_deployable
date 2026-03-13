import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from core.chat import start_chat, send_message

st.set_page_config(page_title="SKRs_AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot")

# initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = start_chat()

# display conversation history
for message in st.session_state.messages:
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# input box
user_input = st.chat_input("Type your message...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    reply = send_message(st.session_state.messages, user_input)
    with st.chat_message("assistant"):
        st.markdown(reply)
