# -----------------------
# tools.py (Ollama Version)
# -----------------------

import ollama


def query_medgemma(prompt: str) -> str:
    """
    Calls MedGemma model with a therapist personality profile.
    Returns responses as an empathic mental health professional.
    """

    system_prompt = """You are Dr. Emily Hartman, a warm and experienced clinical psychologist. 
Respond to patients with:

1. Emotional attunement
2. Gentle normalization
3. Practical guidance
4. Strengths-focused support

Guidelines:
- Never use brackets or labels
- Blend elements naturally
- Mirror the user's language level
- Use warm, conversational tone
- Ask open-ended questions to explore root causes
"""

    try:
        response = ollama.chat(
            model="alibayram/medgemma:4b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            options={
                "num_predict": 350,
                "temperature": 0.7,
                "top_p": 0.9
            }
        )

        return response["message"]["content"].strip()

    except Exception as e:
        print("OLLAMA ERROR:", e)
        return (
            "I'm having technical difficulties right now, "
            "but I want you to know your feelings truly matter. "
            "Please try again shortly."
       )