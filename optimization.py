import json
import os

# Initialize globale variable
numbers = []
operators = []
history = []

# Define the arithmetic basic operations functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Error: Cannot divide by zero.")
        # Return None to indicate an error
        return None  
    return x / y

def modulo(x, y):
    return x % y

def power(x, y):
    if x == 0 and y < 0:
        print("Error: Cannot raise 0 to a negative power.")
        return None
    if x == 0 and y == 0:
        print("Error: 0 raised to the power of 0 is undefined.")
        return None
    return x ** y

def sqrt(x):
    if x < 0:
        print("Error: Cannot calculate the square root of a negative number.")
        # Return None to indicate an error
        return None  
    return x ** 0.5

#define the trigonometric function
"""polynomial function and Taylor"""
"""def cos(x):
    x = x % (2 * 3.141592653589793)
    if x > 3.141592653589793:
        x -= 3.141592653589793
    return 1 - (x ** 2) / 2 + (x ** 4) / 24 - (x ** 6) / 720    

def sin(x):
    x = x % (2 * 3.141592653589793)
    if x > 3.141592653589793:
        x -= 3.141592653589793
    return x - (x ** 3) / 6 + (x ** 5) / 120 - (x ** 7) / 5040

def tan(x):
    x = x % (2 * 3.141592653589793)
    if x > 3.141592653589793:
        x -= 3.141592653589793
    if x == 0:
        print("Error: Tan(0) is undefined.")
        return None
    return (sin(x) / cos(x))

# Define the exponential function
def exp(x):
    return 2.718281828459045 ** x """
# Load history from the JSON file
def load_history():
    try:
        with open("history.json", "r") as file:
            return json.load(file).get("History", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save history to the JSON file
def save_history():
    print("Debug: Saving history")
    try:
        with open("history.json", "w") as file:
            json.dump({"History": history}, file, indent=4)
        print("history saved")
    except Exception as e:
        print("Error: Failed to save history", e)
# Define the sorting function for operators and numbers
def sort_input(expression):
    numbers.clear()
    operators.clear()
    for word in expression.split():
        try:
            numbers.append(float(word))
        except ValueError:
            operators.append(word)

# Check for errors in the operators list
def check_error():
    for word in operators:
        if word not in ['*', '+', '/', '-', '(', ')','%',  '**', 'sqrt']:
            print('Error: Invalid operator detected.')
            return False
    return True

# Advance the calculus
def update_calculus(operation, index, numbers, operators):
    #The square root is a unitary operation , it requires only one operand
    if operation == 'sqrt':
        result = operation(numbers[index])
        # If there was an error , negative numbers
        if result is None:
            return False
        numbers[index] = result
        operators.pop(index)
        return True
    # Save the result in a variable
    result = operation(numbers[index], numbers[index + 1])
    # If there was an error , division by zero
    if result is None:  
        return False
    # Replace the first number by the result
    numbers[index] = result
    # Remove the operator from the list
    operators.pop(index)
    # Remove the second number from the list
    numbers.pop(index + 1)
    return True

# Check for multiply or divide operators
def multiply_divide(numbers, operators):
    while '*' in operators or '/' in operators or '**' in operators or 'sqrt' in operators:
        # Isolate and execute each operation in the list
        for index, operator in enumerate(operators):
            if operator == '*':
                operation = multiply
                if not update_calculus(operation, index, numbers, operators):
                    # Exit on error ( division by zero)
                    return False  
                break
            if operator == '/':
                operation = divide
                if not update_calculus(operation, index, numbers, operators):
                     # Exit on error ( division by zero)
                    return False 
                break
            if operator == '**':
                operation = power
                if not update_calculus(operation, index, numbers, operators):
                    # Exit on error ( division by zero)
                    return False
                break
            if operator =='sqrt':
                operation = sqrt
                if not update_calculus(operation, index, numbers, operators):
                    # Exit on error ( negative number)
                    return False
                break
    # No error occurred
    return True  


# Check for addition or substraction operators
def add_subtract(numbers, operators):
    while '+' in operators or '-' in operators or 'sqrt' in operators:
        for index, operator in enumerate(operators):
            if operator == '+':
                operation = add
                update_calculus(operation, index, numbers, operators)
                break
            if operator == '-':
                operation = subtract
                update_calculus(operation, index, numbers, operators)
                break
    return True
                
# Display history function
def display_history():
    print ("Debug:history ")
    if not history:
        print("History is empty.")
    else:
        print("History:")
        for i, operation in enumerate(history, 1):
            print(f"{i}. {operation}")

# Delete history
def delete_history():
    global history
    if not history:
        print("History is empty.")
    else:
        display_history()
        confirmation = input("Are you sure you want to delete the entire history? (y/n): ")
        if confirmation.lower() == "y":
            history.clear()
            save_history()
            print("History deleted successfully.")
        elif confirmation.lower() == "n":
            print("Deletion cancelled.")
        

# Delete history operation by index
def delete_history_operation():
    display_history()
    try:
        index = int(input("Enter the index of the operation to delete: "))
        if 0 <= index - 1 < len(history):
            del history[index - 1]
            save_history()
            print("History operation deleted.")
        else:
            print("Invalid index. Please enter a number between 1 and", len(history))
    except ValueError:
        print("Invalid index. Please enter a number between 1 and", len(history))

# Menu delete history
def delete_history_options():
    print(
    "\n======= Choose an option ======="
    "\n1. Delete all history"
    "\n2. Delete a specific entry"
    "\n3. Exit"
    )
    try:
        choice = int(input("Enter your choice (1-3): "))
        if choice == 1:
            delete_history()
        elif choice == 2:
            delete_history_operation()
        elif choice == 3:
            return
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 2.")

# Menu function
def perform_calculation():
    while True:
        expression = input('Enter the operation (x + y - z), or type "exit" to quit:\n')
        if expression == 'exit':
            break
        sort_input(expression)
        if check_error():
            # Check for parentheses
            while '(' in operators:
                p_index1 = operators.index('(')
                p_index2 = operators.index(')')
                parenthese_operators = operators[p_index1 + 1:p_index2]
                parenthese_numbers = numbers[p_index1:p_index2]
                multiply_divide(parenthese_numbers, parenthese_operators)
                add_subtract(parenthese_numbers, parenthese_operators)
                del operators[p_index1:p_index2 + 1]
                del numbers[p_index1:p_index2]
                numbers.insert(p_index1, parenthese_numbers[0])

            # Perform the remaining calculations
            if not multiply_divide(numbers, operators):
                print("Calculation failed due to error.")
                # Skip the current loop and ask for the next calculation
                continue 
            
            add_subtract(numbers, operators)

            result = numbers[0]
            if result.is_integer():  # Check if the result is an integer
                result = int(result)
            # Display the result
            if numbers:
                print(f"{expression} = {result}")

                # Save the operation in the history
                history.append(f"{expression} = {result}")
                print("Debug: history.append")
                save_history()

        else:
            print('Error, please try again.')

        # Clear memory
        numbers.clear()
        operators.clear()

#main menu function
def menu():
    print(
        "\n======== Menu =========="
        "\n1. Perform a calculation"
        "\n2. Display history"
        "\n3. Delete history"
        "\n4. Exit"
        )
#clear the termina screen 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
# Main function to run the calculator program
def main():
    global history
    # Load history from the JSON file and assign it to the global variable   
    history = load_history()
    print ("Debug: history loaded")
    while True:
        menu() 
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                clear_screen()
                perform_calculation()
            elif choice == 2:
                display_history()
            elif choice == 3:
                delete_history_options()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 4.")
        except KeyboardInterrupt:
            print("\nExiting the program...")
            break

if __name__ == '__main__':
    main()
