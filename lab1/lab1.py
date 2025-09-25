# - write a program that prints hello world
print("hello world")
# - application to take a number in binary form from the user, and print it as a decimal
# n_bin = input("Enter number in binary form: ")
# while n_bin not in '01':
while True: 
    try : 
        n_bin = input("Enter number in binary form: ")
        print(int(n_bin,2))
        break  
    except : 
        print("please, inter a valid number  : ")

# - write a function that takes a number as an argument and if the number
# 	divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 	divisible by both return "FizzBuzz"
def fizz(num: int) -> str :
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return ""
# - Ask the user to enter the radius of a circle print its calculated area and circumference
r = None
while True :
    try : 
        r = float(input("Enter the radius of a circle"))
        break
    except : 
        print("Please, enter a valid input")
area = 2 * r ** 2
circumference = 2 * 3.14 * r
print("area = " , area)
print(circumference)
# - Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data
name = input("Enter your name: ").strip()
while not name.isalpha():    
    name = input("Enter a valid name not empty or integer: ")
    if name.isalpha():
        email = input("Enter your email: ")
        break
if name.isalpha():
        email = input("Enter your email: ")  
# - Write a program that prints the number of times the substring 'iti' occurs in a string
s = input()
x = s.count('iti')
print(x)