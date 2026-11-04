# Context-Managed Chatbot (Astra)

A responsive multi-turn AI chatbot interface built with Streamlit and powered by Groq's low-latency infrastructure. The assistant is customized with a distinct system persona ("Astra") tailored for mobile robotics and smart automated logistics systems troubleshooting.

## Features
- **Context Window Management:** Automatic short-term truncation to manage active conversation memory tokens.
- **System Customization:** Custom architectural expert persona constraints.
- **Graceful Error Handling:** Structural try-except layers protecting the user interface from direct network API crash failures.

## Setup & Local Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/DarKiller33/valentius-ai-task1.git
   cd valentius-ai-task1
   ```

2. **Install Required Libraries**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Credentials**
   Create a `.env` file in the root directory and add your private Groq API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Launch the Application**
   ```bash
   streamlit run main.py
   ```
