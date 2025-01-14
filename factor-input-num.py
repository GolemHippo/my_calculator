#define function
def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
   return x / y

#menu select operation    
print("\n==== Menu =====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")


while True:
    try:
        choice = int(input("Enter your choice (1-5): "))
        if choice < 1 or choice > 5:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue
        elif choice == 5:
            print("Exiting...")
            break
    
        try:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number : "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            

        if choice == 1:
            #num1 = float(input("Enter first number : "))
        #num2 = float(input("Enter second number : "))
            print(num1 , "+",  num2, "=", add(num1, num2))
       
        elif choice == 2:
        #num1 = float(input("Enter first number : "))
        #num2 = float(input("Enter second number : "))
            print(num1 , "-",  num2, "=", substract(num1, num2))

        elif choice == 3:
        #num1 = float(input("Enter first number : "))
        #num2 = float(input("Enter second number : "))
            print(num1 , "*",  num2, "=", multiply(num1, num2))

        elif choice == 4:
        #num1 = float(input("Enter first number : "))
        #num2 = float(input("Enter second number : "))
            if num2 == 0:
                print("Error! Division by zero")
            else:
                print(num1 , "/",  num2, "=", divide(num1, num2))

    except ValueError:
        print("Invalid input. Please enter a number.")
        
    

    
        



