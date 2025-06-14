import os
from datetime import datetime

# File to store reflections
journal_file = "daily_reflections.txt"

def write_reflection():
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"\n--- Writing Reflection for {today} ---")
    reflection = input("How was your day? What did you learn or feel? \n> ")

    with open(journal_file, "a") as file:
        file.write(f"\n[{today}]\n{reflection}\n{'-'*40}\n")

    print("✅ Reflection saved.\n")

def read_reflections():
    if not os.path.exists(journal_file):
        print("No reflections found yet.\n")
        return

    print("\n📖 Your Past Reflections:\n")
    with open(journal_file, "r") as file:
        print(file.read())

def main():
    while True:
        print("\n📝 Daily Reflection Journal")
        print("1. Write today's reflection")
        print("2. Read past reflections")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")
        if choice == "1":
            write_reflection()
        elif choice == "2":
            read_reflections()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
