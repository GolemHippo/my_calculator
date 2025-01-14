#define function
def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
   return x / y

def display_history(history):
    if not history :
     print("history is empty")
    else:
        print("History:")
        for i, operation in enumerate(history, 1):
            print(f"{i}. {operation}")
            
#menu select operation    
print("\n==== Menu =====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Display_history")
print("6. Exit")


history =[]
while True:
    
    try:
        choice = int(input("Enter your choice (1-6): "))
        if choice < 1 or choice > 6:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue
        elif choice == 6:
            print("Exiting...")
            break
        elif choice == 5:
            #display_history(history)
            print("test")
        try:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number : "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            

        if choice == 1:
            print(num1 , "+",  num2, "=", add(num1, num2))
            history.append(f"{num1} + {num2} = {add(num1, num2)}")
            
       
        elif choice == 2:
            print(num1 , "-",  num2, "=", substract(num1, num2))
            history.append(f"{num1} - {num2} = {substract(num1, num2)}")
            

        elif choice == 3:
            print(num1 , "*",  num2, "=", multiply(num1, num2))
            history.append(f"{num1} * {num2} = {multiply(num1, num2)}")
            

        elif choice == 4:
            if num2 == 0:
                print("Error! Division by zero")
            else:
                print(num1 , "/",  num2, "=", divide(num1, num2))
                history.append(f"{num1} / {num2} = {divide(num1, num2)}")
                

        
    except ValueError:
        print("Invalid input. Please enter a number.")
        
    

    
        




