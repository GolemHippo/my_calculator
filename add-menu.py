#define function
def add(x, y):
    return x + y

#num1 = float(input("Enter first number : "))
#num2 = float(input("Enter second number : "))
#print(num1 , "+",  num2, "=", add(num1, num2))

def substract(x, y):
    return x - y

#num1 = float(input("Enter first number : "))
#num2 = float(input("Enter second number : "))
#print(num1 , "-",  num2, "=", substract(num1, num2))

def multiply(x, y):
    return x * y

#num1 = float(input("Enter first number : "))
#num2 = float(input("Enter second number : "))
#print(num1 , "*",  num2, "=", multiply(num1, num2))

def divide(x, y):
    #if y == 0:
        #return "Error! Division by zero"
    #else:
        return x / y
    
#num1 = float(input("Enter first number : "))
#num2 = float(input("Enter second number : "))
#print(num1 , "/",  num2, "=", divide(num1, num2))

print("\n==== Menu =====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")



while True:
    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))
        print(num1 , "+",  num2, "=", add(num1, num2))
       
    elif choice == 2:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))
        print(num1 , "-",  num2, "=", substract(num1, num2))

    elif choice == 3:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))
        print(num1 , "*",  num2, "=", multiply(num1, num2))

    elif choice == 4:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))
        if num2 == 0:
            print("Error! Division by zero")
        else:
            print(num1 , "/",  num2, "=", divide(num1, num2))

    elif choice == 5:
        print("Exiting...")
        break
        



