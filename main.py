import streamlit as st
from chatbot import ContextManagedChatbot

st.set_page_config(page_title="Valentius Kryptix - AI Task 1", page_icon="🤖")

st.title("🤖 Astra: Autonomous Systems Assistant")
st.caption("Valentius Kryptix AI Internship | Task 1: LLM API Integration & Context Management")

# Initialize chatbot session
if "chatbot" not in st.session_state:
    try:
        st.session_state.chatbot = ContextManagedChatbot(max_history_length=6)
    except Exception as e:
        st.error(f"Initialization Failed: {e}")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages on reload
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User text input box
if prompt := st.chat_input("Ask Astra about robotics, ROS2, or system logs..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response_text = st.session_state.chatbot.send_message(prompt)
            st.markdown(response_text)
            
    st.session_state.messages.append({"role": "assistant", "content": response_text})