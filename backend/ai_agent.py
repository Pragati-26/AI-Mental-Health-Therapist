# ---------------------------------
# SAFE SPACE AI AGENT (Stable Version)
# ---------------------------------

from backend.tools import query_medgemma   


SYSTEM_PROMPT = """
You are a mental health AI assistant.
Always respond warmly and safely.
If crisis is detected, provide helpline information.
"""


# -----------------------------
# Simple Crisis Detection
# -----------------------------
CRISIS_KEYWORDS = [
    "suicide",
    "kill myself",
    "end my life",
    "self harm",
    "die",
    "want to disappear"
]


def is_crisis(message: str) -> bool:
    message = message.lower()
    return any(keyword in message for keyword in CRISIS_KEYWORDS)


# -----------------------------
# Crisis Response
# -----------------------------
def crisis_response():
    return (
        "I'm really sorry you're feeling this way.\n\n"
        "If you are in immediate danger, please seek urgent help right now.\n\n"
        "India Crisis Helplines:\n"
        "• Kiran: 1800-599-0019\n"
        "• iCALL: +91 9152987821\n"
        "• AASRA: +91 9820466726\n\n"
        "You are not alone. Help is available. 💙"
    )


# -----------------------------
# Main Query Function
# -----------------------------
def handle_query(user_message: str):

    if is_crisis(user_message):
        return {
            "response": crisis_response(),
            "tool_called": "crisis_support"
        }

    # Otherwise use MedGemma
    response = query_medgemma(user_message)

    return {
        "response": response,
        "tool_called": "mental_health_specialist"
    }