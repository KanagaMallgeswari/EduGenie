from google import genai
import os 
client=genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
def summarize_text(text):
    response=client.models.generate_content(model="gemini-3.8-flash",contents=f"Summarize this text in simple words:{topic}")
    return response.text