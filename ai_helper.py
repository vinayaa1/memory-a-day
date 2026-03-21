import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_memory(memory_text):
    prompt = f"""
you will be a journaling assistant using the memories a user provides
given this memory, return:
1. a short, creative title
2. the mood (one word)
3. a one-sentence summary

Memory:
{memory_text}

format exactly like this:
title: ...
mood: ...
summary: ...
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content