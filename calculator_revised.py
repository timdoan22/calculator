from art import logo

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

def calculator():
    num1 = float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    
    while should_continue:
        operation_symbol = input("Select the operation: ")
        num2 = float(input("Enter the next number: "))
        compute_answer = operations[operation_symbol]
        answer = compute_answer(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        question = input(f"Type 'y' to continue calculating with {answer}, 'n' to restart or 'e' to exit: ").lower()
        if question == 'y':
            num1 = answer
        elif question == 'n':
            should_continue = False
            calculator()
        else:
            break

calculator()
    
