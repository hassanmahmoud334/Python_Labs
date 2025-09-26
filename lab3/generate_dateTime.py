from datetime import datetime

def run_task():
    while True:
        date_str = input("Enter a date (YYYY-MM-DD): ").strip()
        try:
            target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            break
        except Exception:
            print("Invalid date format. Please use YYYY-MM-DD.")

    today = datetime.today().date()
    delta = (target_date - today).days

    if delta < 0:
        print("This date has already passed.")
    else:
        with open("reminders.txt", "a") as f:
            f.write(f"{date_str} -> {delta} days left\n")
        print(f"Reminder saved: {date_str} -> {delta} days left")
