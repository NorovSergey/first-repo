# Task 2
value = input('Enter a number: ')
try:
    x = int(value)
    if x % 2 == 0:
        print(f"The number {x} is even")
    else:
        print(f"The number {x} is odd")
except ValueError:
    print(f"The value {value} is not a number")