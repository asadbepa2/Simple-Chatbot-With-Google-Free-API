import os
import gradio as gr
from google import genai

# Using the public token to keep your private key completely safe from usage limits!
api_key = "AIzaSyDroMajudvkv29mPZGVYbw1bjyqmLbWHgk"

try:
    # Initialize the client connection
    client = genai.Client(api_key=api_key)
    
    # Create the persistent chat engine session
    chat = client.chats.create(model="gemini-3.6-flash")
    print("🎉 SUCCESS: Connected to the backend gateway!")
except Exception as setup_err:
    print(f"❌ Initial Setup Failed: {setup_err}")

# Define the prediction processing loop
def predict(message, history):
    try:
        response = chat.send_message(message)
        return response.text
    except Exception as api_err:
        return f"❌ Transmission Error: {api_err}"

# Configure the visual interface components
griff = gr.ChatInterface(
    fn=predict,
    title="Gemini Assistant",
    description="Interact with gemini-3.6-flash using the official Google GenAI SDK.",
)

# Render server launch requirements
if __name__ == "__main__":
    griff.launch(server_name="0.0.0.0", server_port=10000, share=False)
