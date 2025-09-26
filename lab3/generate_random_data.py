import csv
import random

def run_task():
    while True:
        try:
            count = int(input("How many random numbers to generate? ").strip())
            if count > 0:
                break
            else:
                print("Enter a number greater than 0.")
        except Exception:
            print("Invalid input. Please enter an integer.")

    numbers = [random.randint(1, 100) for _ in range(count)]

    with open("random_numbers.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["index", "value"])
        for i, num in enumerate(numbers, 1):
            writer.writerow([i, num])

    avg = sum(numbers) / len(numbers)
    print(f"Generated {count} numbers. Average = {avg:.2f}")
