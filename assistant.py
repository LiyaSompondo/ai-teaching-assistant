import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

#.env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

#Get API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found in environment variables.")

#initialize client
client = OpenAI(api_key=api_key)

def ask_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful personal tutor."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.script()
    except Exception as e:
        return f"[Error {str(e)}]"

if __name__ == "__main__":
    print("Script started... (Type 'exit' or 'quit' to stop)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Tutor: Goodbye")
            break
        answer = ask_gpt(user_input)
        print("Tutor:", answer)
