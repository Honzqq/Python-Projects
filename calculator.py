def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    if a == 0 or b == 0:
        return "Error: Cannot divide by zero"
    return a / b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter a mark for operation(+,-,*,/): ")

if operation == "+":
    print(f"Addition result is: {addition(a,b)}")
elif operation == "-":
    print(f"Subtraction result is: {subtraction(a,b)}")
elif operation == "*":
    print(f"Multiplication result is: {multiplication(a,b)}")
elif operation == "/":
    print(f"The result of the division is: {division(a,b)}")
else:
    print("Error: You must enter a sign")