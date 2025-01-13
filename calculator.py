#define function
def add(x, y):
    return x + y

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
print(num1 , "+",  num2, "=", add(num1, num2))

def substract(x, y):
    return x - y

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
print(num1 , "-",  num2, "=", substract(num1, num2))

def multiply(x, y):
    return x * y

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
print(num1 , "*",  num2, "=", multiply(num1, num2))

def divide(x, y):
    if y == 0:
        return "Error! Division by zero"
    else:
        return x / y
    
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
print(num1 , "/",  num2, "=", divide(num1, num2))
