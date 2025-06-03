first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
choose_operator = input('Enter operation: ')

match choose_operator:
    case "+":
        print(first_number+second_number)
    case "-":
        print(first_number-second_number)
    case "/":
        if second_number == 0:
            print("Error: Can't divide by zero")
        else:
            print(first_number/second_number)
    case "*":
        print(first_number*second_number)
    case _:
        print("invalid operator.")
        