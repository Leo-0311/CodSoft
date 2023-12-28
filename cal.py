def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."
    
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Operations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = input("Enter operation (choose 1-4): ")
if operation == '1':
    result = add(a, b)
elif operation == '2':
    result = subtract(a, b)
elif operation == '3':
    result = multiply(a, b)
elif operation == '4':
    result = divide(a, b)
else:
    print("Invalid operation. Please choose a number between 1 and 4.")
    result = None
if result is not None:
    print("Result: {}".format(result))
