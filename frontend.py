# ===============================
# SafeSpace – AI Mental Health Therapist
# Streamlit Frontend
# ===============================

import streamlit as st
import requests

# 🔹 Replace with your Render backend URL
BACKEND_URL = "https://ai-mental-health-therapist-3.onrender.com/ask"

st.set_page_config(page_title="AI Mental Health Therapist", layout="wide")
st.title("🧠 SafeSpace – AI Mental Health Therapist")

# ===============================
# Session State for Chat History
# ===============================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ===============================
# Chat Input
# ===============================
user_input = st.chat_input("What's on your mind today?")

if user_input:
    # Add user message to chat
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input
    })

    with st.spinner("Thinking... 💭"):

        try:
            # 🔹 Send request to backend with timeout
            response = requests.post(
                BACKEND_URL,
                json={"message": user_input},
                timeout=60  # Important for Render free tier cold start
            )

            # Convert response to JSON safely
            data = response.json()

            # Extract values safely
            reply = data.get("response", "No response received.")
            tool_used = data.get("tool_called", "None")

            assistant_message = f"{reply}\n\n🔧 Tool Used: {tool_used}"

        except requests.exceptions.Timeout:
            assistant_message = "⏳ Backend is waking up. Please try again in 30 seconds."

        except requests.exceptions.ConnectionError:
            assistant_message = "⚠️ Cannot connect to backend. Please check if it is deployed correctly."

        except Exception as e:
            assistant_message = f"❌ Unexpected error: {str(e)}"

    # Add assistant reply
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": assistant_message
    })

# ===============================
# Display Chat History
# ===============================
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])