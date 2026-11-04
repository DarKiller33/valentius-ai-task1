import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class ContextManagedChatbot:
    def __init__(self, max_history_length: int = 6):
        # 1. Retrieve the Groq API Key from environment variables
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables.")
        
        # Initialize official Groq client
        self.client = Groq(api_key=api_key)
        
        # Using a reliable model available on Groq's tier
        self.model_id = "openai/gpt-oss-120b"
        
        # System prompt (Requirement 4)
        self.system_instruction = (
            "You are 'Astra', an advanced onboard AI assistant for autonomous mobile robots "
            "and smart automated logistics systems. You are technical, precise, helpful, "
            "and concise in your troubleshooting and architectural suggestions."
        )
        
        self.history = []
        self.max_history_length = max_history_length

    def send_message(self, user_input: str) -> str:
        """Sends a message with multi-turn history, context window management, and error handling."""
        try:
            # 1. Append new user message to the long-term history array
            self.history.append({"role": "user", "content": user_input})

            # 2. Context Window Management (Requirement 3)
            truncated_history = self.history[-self.max_history_length:]
            active_history = [{"role": "system", "content": self.system_instruction}] + truncated_history

            # 3. Call the native Groq API
            response = self.client.chat.completions.create(
                model=self.model_id,
                messages=active_history
            )

            bot_reply = response.choices[0].message.content

            # 4. Append model response back into long-term history
            self.history.append({"role": "assistant", "content": bot_reply})
            return bot_reply

        except Exception as e:
            # Basic error handling for network timeouts / API limits (Requirement 5)
            return f"[API Error]: Unable to process request due to a service issue. ({str(e)})"
