import math_auto
import regex
import generate_dateTime
import transformer
import os_manager
import generate_random_data
import decorator7

tasks = {
    "1": ("Math Automation", math_auto.run_task),
    "2": ("Regex Log Cleaner", regex.run_task),
    "3": ("Datetime Reminder Script", generate_dateTime.run_task),
    "4": ("Product Data Transformer", transformer.run_task),
    "5": ("OS File Manager", os_manager.run_task),
    "6": ("Random Data Generator", generate_random_data.run_task),
    "7": ("Decorators Task", decorator7.run_task),
}

def main():
    print("\n=== Task Runner Menu ===")
    for num, (name, _) in tasks.items():
        print(f"{num}. {name}")

    while True:
        choice = input("Select a task number: ").strip()
        if choice in tasks:
            print(f"\n▶ Running: {tasks[choice][0]}\n")
            tasks[choice][1]()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
