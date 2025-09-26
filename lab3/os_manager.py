import os
import shutil

def run_task():
    while True:
        dir_path = input("Enter a directory path: ").strip()
        if os.path.isdir(dir_path):
            break
        print("Invalid directory. Try again.")

    backup_dir = os.path.join(dir_path, "backup")
    os.makedirs(backup_dir, exist_ok=True)

    copied_count = 0
    for filename in os.listdir(dir_path):
        if filename.endswith(".txt"):
            src = os.path.join(dir_path, filename)
            dst = os.path.join(backup_dir, filename)
            shutil.copy(src, dst)
            copied_count += 1

    print(f"{copied_count} .txt files copied to {backup_dir}")
