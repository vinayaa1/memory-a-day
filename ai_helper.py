import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_memory(memory_text):
    prompt = f"""
    Analyze this daily memory and return:
    1. a short and creative title for the memory
    2. the mood (should be one word)
    3. a one sentence summary

    Memory:
    {memory_text}

    Format:
    title: ...
    mood: ...
    summary: ...
    """

    response = client.chat.completions.create(
        model = "gpt-4o-mini"
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response.choices[0].message.content
