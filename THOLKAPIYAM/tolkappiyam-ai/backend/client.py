import google.generativeai as genai
from config import _API_KEY, MODEL_NAME

genai.configure(api_key=_API_KEY)


model = genai.GenerativeModel(MODEL_NAME)

def ask_gemini(prompt):
    """
    Sends a prompt to the Gemini model and returns the generated text response.
    """
    try:
        response = model.generate_content(prompt)

        # Some Gemini responses may return parts; handle safely
        if hasattr(response, "text") and response.text:
            return response.text.strip()
        else:
            return ""

    except Exception as e:
        # Fail safely for backend stability
        return f"Error generating response: {str(e)}"
