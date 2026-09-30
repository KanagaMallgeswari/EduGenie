from google import genai
import os 
client=genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
def recommend_learning_path(topic):
    response=client.models.generate_content(model="gemini-3.8-flash",contents=f"Create a simple learning path for a college student:{topic}")
    return response.text