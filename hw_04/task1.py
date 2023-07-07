# Task 1
value = input('Entered value: ')
if value.isnumeric():
    print(f'The entered value {value} is a number')
elif value.isalpha():
    print(f'The entered value {value} is a text')
else:
    print(f'You wrote the wrong value {value}')