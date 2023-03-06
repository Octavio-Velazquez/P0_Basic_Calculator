
def addition(number_1, number_2):
    """This functions sums two numbers."""
    result = number_1 + number_2
    #print(f"{number_1} + {number_2} = {result}")
    return result

def subtraction(number_1, number_2):
    """This functions rest two numbers."""
    result = number_1 - number_2
    # print(f"{number_1} - {number_2} = {result}")
    return result

def multiplication(number_1, number_2):
    """This functions multiply two numbers."""
    result = number_1 * number_2
    # print(f"{number_1} * {number_2} = {result}")
    return result

def division(number_1, number_2):
    """This functions divides two numbers."""
    try:
        result = number_1 / number_2
        # print(f"{number_1} / {number_2} = {result}")
        return result
    except ZeroDivisionError:
        print("You can not divide by zero.")