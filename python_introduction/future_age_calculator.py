try:
    current_age = int(input('How old are you? '))
    future_age = current_age + 25
    print(f'In 2050, you will be {future_age} years old.')
except ValueError:
    print('You need to input a valid number.')
