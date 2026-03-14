from datetime import date
from memory_store import save_memory, memory_exists

today = date.today().isoformat()

print("\ntoday's date:", today)

if memory_exists(today):
    print("\nyou already wrote a memory for todayyy")
    print("\ncome back tomorrow!!!")
else:
    print("\nwrite your memory for today(to log):")

    user_memory = input("> ")
    save_memory(today,user_memory)

    print("\n memory successfully saved yay! :)")