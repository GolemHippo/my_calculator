#define function
def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Error! Division by zero")
        return None
    return x / y
#history function   
def display_history(history):
    if not history :
        print("history is empty")
    else:
        print("History:")
        for i, operation in enumerate(history, 1):
            print(f"{i}. {operation}")

def delete_history(history):
    history.clear()
    print("History deleted")


def delete_history_operation(history):
    index = int(input("Enter the index of the operation to delete: "))
    if 0 <= index - 1 < len(history):
        del history[index - 1]
        print("History operation deleted")
    else:
        print("Invalid index. Please enter a number between 1 and", len(history))

def delete_history_options(history):
    print("Choose an option:")
    print("1. Delete all history")
    print("2. Delete a specific entry")
    choice = int(input("Enter your choice (1-2): "))
    if choice == 1:
        delete_history(history)
    elif choice == 2:
        delete_history_operation(history)
    
    else:
        print("Invalid choice. Please enter a number between 1 and 2.")
        
#menu select operation 
def menu():   
    print("\n==== Menu =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Display_history")
    print("6. Delete")
    print("7. Exit")


history =[]
while True:

    menu()
    try:
        choice = int(input("Enter your choice (1-7): "))
        if choice < 1 or choice > 7:
            print("Invalid choice. Please enter a number between 1 and 7.")
            continue

        elif choice == 7:
            print("Exiting...")
            break
        
        elif choice == 5:
            display_history(history)
            continue

        elif choice == 6:
            delete_history_options(history)
            continue
                
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))
        
        if choice == 1:
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
            history.append(f"{num1} + {num2} = {result}")

        elif choice == 2:
            result = substract(num1, num2)
            print(f"{num1} - {num2} = {result}")
            history.append(f"{num1} - {num2} = {result}")
            
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
            history.append(f"{num1} * {num2} = {result}")
            
        elif choice == 4:
            result = divide(num1, num2)
            if result is not None:
                print(f"{num1} / {num2} = {result}")
                history.append(f"{num1} / {num2} = {result}")
                
    except ValueError:
        print("Invalid input. Please enter a number.")