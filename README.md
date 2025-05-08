# 🤖 AI Teaching Assistant

This project is a command-line based AI-powered personal tutor built using OpenAI's GPT models. It allows users to ask questions and receive intelligent responses directly in the terminal.

---

## 🧠 Features

- Chat with GPT-3.5 or GPT-4 (if you have access)
- .env integration to securely manage your API key
- Built with modern OpenAI SDK (v1.x)
- Lightweight and easy to use

---

## 🚀 How to Use

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/ai-teaching-assistant.git
   cd ai-teaching-assistant

2. **Create and Activate virtual environment**
    python -m venv venv
    .\venv\Scripts\activate

3. **Install dependencies**
    pip install openai python-dotenv

4. **Add your OpenAI API key to .env**
    OPENAI_API_KEY='your_api_key_here'

5.**Run the Script**
    python assistant.py

**FILE STRUCTURE**
|
|- assistant.py
|- .env
|- .gitignore
|_ README.md

**EXAMPLE PROMPT**
You: Explain the difference between a list and a tuple in python.
Tutor: A list is mutable...

**DISCLAIMER**
This is a personal education tool and uses OpenAI's API, which may incur costs. Make sure to monitor your usage in your OpenAI account.

**AUTHOR**
LiyaSompondo