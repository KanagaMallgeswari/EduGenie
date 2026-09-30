from google import genai
import os 
client=genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
def explain_topic(topic):
    response=client.models.generate_content(model="gemini-3.8-flash",contents=f"Explain this topic in simple words for a college student:{topic}")
    return response.text