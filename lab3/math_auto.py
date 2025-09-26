import math
from decorators import log_time

@log_time
def run_task():
    while True:
        numbers_input = input("Enter numbers (comma-separated): ").strip()
        try:
            numbers = [float(num.strip()) for num in numbers_input.split(",") if num.strip()]
            if not numbers:
                1/0
            break
        except Exception:
            print("Invalid input. Please enter valid numbers separated by commas.")

    with open("math_report.txt", "w") as f:
        for num in numbers:
            floor_val = math.floor(num)
            ceil_val = math.ceil(num)
            sqrt_val = math.sqrt(num) if num >= 0 else "NaN"
            circle_area = math.pi * (num ** 2)
            f.write(
                f"  Number: {num}\n"
                f"  Floor: {floor_val}\n"
                f"  Ceil: {ceil_val}\n"
                f"  Square Root: {sqrt_val}\n"
                f"  Circle Area: {circle_area}\n\n"
            )

    print("'math_report.txt' created successfully.\n--- File Content ---")
    with open("math_report.txt", "r") as f:
        print(f.read())
