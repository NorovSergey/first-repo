# Task 4
value = input('Enter a number: ')
try:
    x = int(value)
    if x % 2 != 0:
        print(f'Entered value {value} is an odd number')
    else:
        print(f'Entered value {value} is an even number')
except ValueError:
        print(f'Entered value {value} is a text with length ' + str(len(value)))