from art import logo

# Welcome to the calculator app.  This simple app will prompt the user for two numbers and 
# a mathematical operation for the result and continue with subsequent calculations if wanted.

first_calculation = True
next_calculation = True

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2
    
def square_root(n1, n2):
    return n1 ** n2

    
#Operations dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": square_root
}

print(logo)
print("Welcome to the calculator app.")

while first_calculation:
# Prompt the user for inputs
    first_num = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation: ")
    second_num = float(input("What's the next number?: "))
# Compute the first calculation and display the result
    calculate_function = operations[operation_symbol]
    answer = calculate_function(first_num, second_num)
    print(f"{first_num} {operation_symbol} {second_num} = {answer}")
# Store the answer in the next_answer variable to get passed on to the next calculation if required
    next_answer = answer
# Prompt the user to continue with the next calculation, restart with a new calculation or exit the app
    continue_calculation = input(f"Type 'y' to continue calculating with {next_answer}, 'n' to start a new calculation or 'e' to exit: ").lower()
    if continue_calculation == 'y':
        next_calculation = True
        pass
    elif continue_calculation == 'n':
        next_calculation = False
        pass
    else:
        break

    while next_calculation:
# Get inputs from the user to compute the next calculation, display the results and return the answer in a function"""        
            def next_calculation_function(next_answer):
                current_answer = next_answer
                next_symbol = input("Pick an operation: ")
                next_num = float(input("What's the next number?: "))
                calculate_function = operations[next_symbol]
                next_answer = calculate_function(next_answer, next_num)
                print(f"{current_answer} {next_symbol} {next_num} = {next_answer}")
                return next_answer
# Store the value of the returned answer in the same next_answer variable in order to iterate through subsequent chain calculations if necessary
            next_answer = next_calculation_function(next_answer)
# Prompt the user to continue with the chain calculation, restart all over or exit the app
            continue_calculation = input(f"Type 'y' to continue calculating with {next_answer}, 'n' to start a new calculation or 'e' to exit: ").lower()
            if continue_calculation == 'y':
                pass
            elif continue_calculation == 'n':
                break
            else:
                next_calculation = False
                first_calculation = False
