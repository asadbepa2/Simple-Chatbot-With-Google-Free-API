!pip install google-genai gradio -q

import os
import gradio as gr
from google import genai
from google.colab import userdata

# 1. Grab your key directly from your Colab Secrets
try:
    api_key = userdata.get('GEMINI_API_KEY')
except Exception:
    api_key = "AIzaSyDroMajudvkv29mPZGVYbw1bjyqmLbWHgk"

try:
    # 2. Initialize the official client connection
    client = genai.Client(api_key=api_key)
    
    # 3. Create a persistent chat session
    chat = client.chats.create(model="gemini-3.6-flash")
    print("🎉 SUCCESS: Your AQ. key connected to the backend servers perfectly!")
except Exception as setup_err:
    print(f"❌ Initial Setup Failed: {setup_err}")

# 4. Define the prediction function for Gradio
def predict(message, history):
    try:
        # Send message through the self-managing session context
        response = chat.send_message(message)
        return response.text
    except Exception as api_err:
        return f"❌ Transmission Error: {api_err}"

# 5. Launch Gradio Chat Interface
griff = gr.ChatInterface(
    fn=predict,
    title="Gemini Assistant",
    description="Interact with gemini-3.6-flash using the official Google GenAI SDK.",
)

griff.launch(share=True)
