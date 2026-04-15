import streamlit as st
from config import USER_AVATAR, BOT_AVATAR

def display_messages():

    for role, text in st.session_state.messages:

        if role == "user":
            st.chat_message("user", avatar=USER_AVATAR).write(text)

        else:
            st.chat_message("assistant", avatar=BOT_AVATAR).write(text)


def clear_chat():

    if st.sidebar.button("Clear Chat"):

        st.session_state.messages = []

        st.rerun()


def download_chat():

    chat_text = ""

    for role, text in st.session_state.messages:

        chat_text += f"{role.upper()}: {text}\n\n"

    st.sidebar.download_button(
        label="Download Chat",
        data=chat_text,
        file_name="chat_history.txt",
        mime="text/plain"
    )


def typing_indicator():

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        return st.empty()
    