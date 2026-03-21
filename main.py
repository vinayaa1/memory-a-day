from datetime import date
from memory_store import save_memory, memory_exists, get_all_memories, get_random_memory
from ai_helper import analyze_memory

def write_memory():
    today = date.today().isoformat()

    print("\ntoday's date:", today)

    if memory_exists(today):
        print("\nyou already wrote a memory for todayyy")
        print("\ncome back tomorrow!!!")
    else:
        print("\nwrite your memory for today(to log):")

    user_memory = input("> ")
    
    analysis = analyze_memory(user_memory)
    save_memory(today,user_memory)

    print("\n memory successfully saved yay! :)")
    print(analysis)

def view_all_memories():
    memories = get_all_memories()

    if not memories:
        print("\nno memories saved yettt")
        return
    print("\nyour memories:")

    for date, entry in memories.items():
        print(f"{date} - {entry['memory']}")

def random_memory():
    result = get_random_memory()

    if result is None:
        print("\nno memories saved yet")
        return
    
    date, memory = result

    print("\nrandom memory generator:\n")
    print(f"{date}-{memory}")

def main_menu():
    while True:
        print("\n~a memory a day~\n")
        print("1. write your memory for today")
        print("2. view all memories")
        print("3. show a random memory")
        print("4. exit")

        choice = input("\nchoose an option 1 through 4:")

        if choice == "1":
            write_memory()
        elif choice == "2":
            view_all_memories()
        elif choice == "3":
            random_memory()
        elif choice == "4":
            print("goodbyeee see u next time")
            break
        else:
            print("please choose an option 1-4")
main_menu()