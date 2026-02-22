import streamlit as st
import requests

BACKEND_URL = "https://ai-mental-health-therapist-3.onrender.com/ask"

st.set_page_config(page_title="AI Mental Health Therapist", layout="wide")
st.title("🧠 SafeSpace – AI Mental Health Therapist")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("What's on your mind today?")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    try:
        response = requests.post(
            BACKEND_URL,
            json={"message": user_input}
        )

        if response.status_code == 200:
            data = response.json()
            reply = data.get("response", "No response received.")
            tool = data.get("tool_called", "None")

            st.session_state.chat_history.append({
                "role": "assistant",
                "content": f"{reply}\n\n🔧 Tool Used: {tool}"
            })
        else:
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": "⚠️ Backend error. Please try again."
            })

    except Exception:
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": "❌ Cannot connect to backend server."
        })

# Display chat
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])