import random

def sort_numbers():
    while True:
        try:
            arr = input("Enter five numbers to sort them (e.g. 1 2 2 3 5): ").split()
            if len(arr) != 5 or not all(x.isdigit() for x in arr):
                print("Please enter exactly five valid numbers separated by spaces.")
                continue
            arr = list(map(int, arr))
            print(f"Original: {arr}")
            print(f"Ascending: {sorted(arr)}")
            print(f"Descending: {sorted(arr, reverse=True)}")
            break
        except Exception:
            print("Unexpected error. Please try again.")

def generate_sequence(length: int, start: int):
    if length <= start:
        print("Length must be greater than start.")
        return
    for i in range(start, length):
        print(i, end=" ")
    print()

def sum_count_AVG():
    sumTotal = 0
    countTotal = 0
    while True:
        x = input("Enter number to calculate or 'done' to stop: ")
        if x.lower() == "done":
            avg = sumTotal // countTotal if countTotal else 0
            print(f"Sum = {sumTotal}")
            print(f"Count = {countTotal}")
            print(f"Avg = {avg}")
            break
        if not x.lstrip('-').isdigit():
            print("Please enter a valid integer or 'done' to stop.")
            continue
        x = int(x)
        sumTotal += x
        countTotal += 1

def display_list():
    while True:
        arr = input("Enter numbers to remove duplicates and sort (e.g. 1 2 2 3 5): ").split()
        if not arr or not all(x.isdigit() for x in arr):
            print("Please enter valid numbers separated by spaces.")
            continue
        arr = list(set(map(int, arr)))
        arr.sort()
        print(arr)
        break

def count_word():
    while True:
        sentence = input("Enter a sentence: ").strip()
        if not sentence:
            print("Please enter a non-empty sentence.")
            continue
        words = sentence.split()
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        print(list(d.items()))
        break

def gradebook():
    names = []
    scores = []
    for i in range(1, 6):
        while True:
            name = input(f"Enter student name {i}: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            break
        while True:
            score = input(f"Enter student score {i}: ")
            if not score.isdigit():
                print("Score must be a valid integer.")
                continue
            score = int(score)
            if score < 0 or score > 100:
                print("Score must be between 0 and 100.")
                continue
            break
        names.append(name)
        scores.append(score)
    print(f"Max = {max(scores)}")
    print(f"Min = {min(scores)}")
    print(f"Avg = {sum(scores) // len(scores)}")

def shopping_cart():
    d = {}
    def add_items(name: str, price: int):
        d[name] = price
        print(f"Item '{name}' added with price {price}.")
    def remove_item(name: str):
        if name in d:
            del d[name]
            print(f"Item '{name}' removed.")
        else:
            print(f"Item '{name}' not found.")
    def display():
        if d:
            print("Items in cart:")
            for name, price in d.items():
                print(f"{name}: {price}")
        else:
            print("Cart is empty.")
    while True:
        print("\nChoose number from the list below")
        print(" 1) Add item")
        print(" 2) Remove item")
        print(" 3) Display items")
        print(" 4) Chekout")
        x = input("Enter number of operation: ")
        if not x.isdigit() or int(x) not in [1,2,3,4]:
            print("Please enter a valid option (1-4).")
            continue
        x = int(x)
        if x == 1:
            name = input("Enter name of item: ").strip()
            if not name:
                print("Item name cannot be empty.")
                continue
            price = input("Enter price of item: ")
            if not price.isdigit() or int(price) < 0:
                print("Price must be a non-negative integer.")
                continue
            add_items(name, int(price))
        elif x == 2:
            name = input("Enter name of item to remove: ").strip()
            if not name:
                print("Item name cannot be empty.")
                continue
            remove_item(name)
        elif x == 3:
            display()
        elif x == 4:
            print(f"Total cost: {sum(d.values())}")
            break

def guessing_game():
    number = random.randint(1, 20)
    counter = 0
    print("Guess the number between 1 and 20.")
    while True:
        guess = input("Enter your guess: ")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)
        counter += 1
        if guess < 1 or guess > 20:
            print("Guess must be between 1 and 20.")
            continue
        if guess < number:
            print("Your guess was too low. Try again.")
        elif guess > number:
            print("Your guess was too high. Try again.")
        else:
            print(f"You got it in {counter} tries!")
            break

def main_menu():
    while True:
        print("\nChoose number from the list below:")
        print(" 1) Sort numbers")
        print(" 2) Generate sequence")
        print(" 3) Sum, Count, AVG of numbers")
        print(" 4) Remove duplicates and sort list")
        print(" 5) Count words in sentence")
        print(" 6) Gradebook")
        print(" 7) Shopping cart")
        print(" 8) Guessing game")
        print(" 9) Exit")
        choice = input("Enter number of operation: ")
        if not choice.isdigit() or int(choice) not in range(1, 10):
            print("Invalid choice, please select a valid option (1-9).")
            continue
        choice = int(choice)
        if choice == 1:
            sort_numbers()
        elif choice == 2:
            while True:
                seq_input = input("Enter the start and range of sequence (e.g. 1 50): ").split()
                if len(seq_input) != 2 or not all(x.isdigit() for x in seq_input):
                    print("Please enter two valid integers separated by space.")
                    continue
                start, length = map(int, seq_input)
                generate_sequence(length + start, start)
                break
        elif choice == 3:
            sum_count_AVG()
        elif choice == 4:
            display_list()
        elif choice == 5:
            count_word()
        elif choice == 6:
            gradebook()
        elif choice == 7:
            shopping_cart()
        elif choice == 8:
            guessing_game()
        elif choice == 9:
            print("Exiting program.")
            break

main_menu()