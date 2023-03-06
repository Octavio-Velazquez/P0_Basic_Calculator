
from operations import addition
from operations import subtraction
from operations import multiplication
from operations import division

welcome = "\nWelcome to the calculator program."
welcome += "\nSelect the following options. "
print(welcome.upper())

menu = "\na. Addition \nb. Subtraction \nc. Multiplication \nd. Division \n\nWrite (quit) to exit the program."
print(menu)

while True:
    try:
        operation = input("\nChoose the operation: ")
        if operation.lower() == "quit":
            break

        n1 = float(input("First Number: "))
        n2 = float(input("Second Number: "))

        if operation == "a":
            print(addition(n1, n2))
        elif operation == "b":
            print(subtraction(n1, n2))
        elif operation == "c":
            print(multiplication(n1, n2))
        elif operation == "d":
            print(division(n1, n2))
        else:
            print("Error! Choose a correct operation.")

    except ValueError:
        print("Error! Just use digits.")

