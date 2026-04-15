from google import genai
from config import GEMINI_API_KEY, MODEL_NAME
from prompts import SYSTEM_PROMPT

class GeminiClient:

    def __init__(self):

        self.client = genai.Client(api_key=GEMINI_API_KEY)

        self.chat_session = self.client.chats.create(
            model=MODEL_NAME,
            config=genai.types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )
        )

    def send_message(self, message):

        response = self.chat_session.send_message(message)

        return response.text