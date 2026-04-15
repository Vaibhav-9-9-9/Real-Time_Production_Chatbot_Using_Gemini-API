import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USER_AVATAR = os.path.join(BASE_DIR, "assets", "user.png")
BOT_AVATAR = os.path.join(BASE_DIR, "assets", "bot.png")

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
MODEL_NAME = "gemini-2.5-flash"
