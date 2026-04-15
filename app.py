import streamlit as st
import time

from client import GeminiClient
from ui import display_messages, clear_chat, download_chat, typing_indicator
from config import USER_AVATAR, BOT_AVATAR


st.set_page_config(page_title="Career Advisor", page_icon="🎓")

st.title("🎓 Career Advisor Chatbot")


# Initialize client
if "client" not in st.session_state:

    st.session_state.client = GeminiClient()

# Initialize messages
if "messages" not in st.session_state:

    st.session_state.messages = []

# Sidebar features

clear_chat()

download_chat()

# Display chat
display_messages()

# User input
user_input = st.chat_input("Ask your career question...")

USER_AVATAR = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
BOT_AVATAR = "https://cdn-icons-png.flaticon.com/512/4712/4712109.png"


if user_input:

    st.session_state.messages.append(("user", user_input))

    st.chat_message("user", avatar=USER_AVATAR).write(user_input)

    # Typing indicator
    placeholder = typing_indicator()

    placeholder.write("Typing...")

    # Get response
    response = st.session_state.client.send_message(user_input)

    # Streaming effect
    full_response = ""

    placeholder.empty()

    with st.chat_message("assistant", avatar=BOT_AVATAR):

        message_placeholder = st.empty()

        for char in response:

            full_response += char

            message_placeholder.write(full_response)

            time.sleep(0.01)

    st.session_state.messages.append(("assistant", full_response))
