from google import genai
import os 
client=genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
def answer_question(question):
    response=client.models.generate_content(model="gemini-3.8-flash",contents=f"Answer this question in simple words for a college student:{question}")
    return response.text