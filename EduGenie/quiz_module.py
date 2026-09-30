from google import genai
import os 
client=genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
def generate_quiz(topic):
    response=client.models.generate_content(model="gemini-3.8-flash",contents=f"Create 5 simple quiz questions about:{topic}")
    return response.text
