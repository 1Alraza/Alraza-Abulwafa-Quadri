class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error! Division by zero."
        return x / y

while True:
    try:
        a = float(input("Enter first number: "))
        break
    except ValueError:
        print("Invalid number! Please enter a numeric value.")

while True:
    try:
        b = float(input("Enter second number: "))
        break
    except ValueError:
        print("Invalid number! Please enter a numeric value.")


valid_operations = ['+', '-', '*', '/']
operation = input("Enter operation (+, -, *, /): ")

while operation not in valid_operations:
    print("Invalid operation! Please enter one of +, -, *, /.")
    operation = input("Enter operation (+, -, *, /): ")

cal=Calculator()

if operation == '+':
    print(f"{a} + {b} = {cal.add(a,b)}") 
elif operation == '-':
    print(f"{a} - {b} = {cal.subtract(a,b)}")
elif operation == '*':
    print(f"{a} * {b} = {cal.multiply(a,b)}")
elif operation == '/':
    print(f"{a} / {b} = {cal.divide(a,b)}")