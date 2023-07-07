# Task 1
value = input('Entered value: ')
if value.isnumeric():
    print(f'The enterd value {value} is a number')
elif value.isalpha():
    print(f'The enterd value {value} is a text')
else:
    print(f'You wrote the wrong value {value}')