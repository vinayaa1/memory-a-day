import json
import os
import random

FILE_PATH = "data/memories.json"

def load_memories():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, "r", encoding = "utf-8") as file:
        data = json.load(file)

    return data

def save_memory(date, memory_text):
    memories = load_memories()

    memories[date] = {
        "memory": memory_text
    }

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(memories, file, indent=4)

def memory_exists(date):
    memories = load_memories()

    return date in memories

def get_all_memories():
    return load_memories()

def get_random_memory():
    memories = load_memories()

    if not memories:
        return None

    random_date = random.choice(list(memories.keys()))
    return random_date, memories[random_date]["memory"]
