"""
CareerPilot AI - AI Client
Supports OpenRouter models through a single interface.
"""

import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

DEFAULT_MODEL = "google/gemini-2.5-flash-lite"

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

def _chat(prompt:str, model:str=DEFAULT_MODEL, temperature:float=0.2)->str:
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content.strip()

def analyze_resume(prompt:str, model:str=DEFAULT_MODEL):
    text = _chat(prompt, model=model, temperature=0)
    text = text.replace("```json","").replace("```","").strip()
    return json.loads(text)

def generate_text(prompt:str, model:str=DEFAULT_MODEL, temperature:float=0.4):
    return _chat(prompt, model=model, temperature=temperature)

def generate_markdown(prompt:str, model:str=DEFAULT_MODEL):
    return _chat(prompt, model=model, temperature=0.5)

def list_supported_models():
    return {
        "Gemini 2.5 Flash Lite":"google/gemini-2.5-flash-lite",
        "GPT-4.1 Mini":"openai/gpt-4.1-mini",
        "Claude Sonnet 4":"anthropic/claude-sonnet-4",
        "DeepSeek V3":"deepseek/deepseek-chat",
        "Llama 3.3 70B":"meta-llama/llama-3.3-70b-instruct",
        "Qwen 3":"qwen/qwen3-32b"
    }
