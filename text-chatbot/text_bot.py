import os
from google import genai
api_key = os.environ.get('GEMINI_API_KEY', "AQ.Ab8RN6KFR6P***********************")

try:
    client = genai.Client(api_key=api_key)
    chat = client.chats.create(model="gemini-3.6-flash")

    print("🎉 SUCCESS: Terminal gateway open using gemini-3.6-flash!")
    print("Type your message below. Type 'exit' to quit.\n" + "="*60)

    while True:
        user_message = input("You: ")
        if user_message.lower() in ['exit', 'quit']:
            print("\nChat closed safely. Goodbye!")
            break
        if not user_message.strip():
            continue
            
        try:
            response = chat.send_message(user_message)
            print(f"\nGemini: {response.text}\n" + "="*60)
        except Exception as api_err:
            print(f"\n❌ Transmission Error: {api_err}\n" + "="*60)

except Exception as setup_err:
    print(f"❌ Initial Setup Failed: {setup_err}")
