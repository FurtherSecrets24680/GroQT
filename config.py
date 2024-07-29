# In this file, provide your Groq AI API key to use the chatbot.

from groq import Groq

# API key for Groq
# Go to https://console.groq.com/keys to get your own API key. It's free.
API_KEY = "YOUR_API_KEY"

# System prompt
SYSTEM_PROMPT = {"role": "system", "content": "You are a very helpful assistant. "}

# Available models for the chatbot
MODELS = {
#    "Llama 3.1 405B (Preview)": "llama-3.1-405b-reasoning", # This model has been released, but the Groq API doesn't have access yet.
    "Llama 3.1 70B (Preview)": "llama-3.1-70b-versatile",
    "Llama 3.1 8B (Preview)": "llama-3.1-8b-instant",
    "Llama 3 Groq 70B Tool Use (Preview)": "llama3-groq-70b-8192-tool-use-preview",
    "Llama 3 Groq 8B Tool Use (Preview)": "llama3-groq-8b-8192-tool-use-preview",
    "Meta Llama 3 70B": "llama3-70b-8192",
    "Meta Llama 3 8B": "llama3-8b-8192",
    "Mixtral 8x7B": "mixtral-8x7b-32768",
    "Gemma 7B": "gemma-7b-it",
    "Gemma 2 9B": "gemma2-9b-it"
}

# Initialize Groq API key
client = Groq(api_key=API_KEY)

