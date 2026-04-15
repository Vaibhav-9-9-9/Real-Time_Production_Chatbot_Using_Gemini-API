import streamlit as st

USER_AVATAR = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
BOT_AVATAR = "https://cdn-icons-png.flaticon.com/512/4712/4712109.png"


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
    
