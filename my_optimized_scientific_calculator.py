import json

# Initialize the numbers and operators lists
numbers = []
operators = []
history = []

# Define the operations functions
def add(x, y):
    return x + y

def substract(x, y):
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

# Load history from the JSON file
def load_history():
    try:
        with open("history.json", "r") as file:
            return json.load(file)["history"]
    except FileNotFoundError:
        return []

# Save history to the JSON file
def save_history():
    with open("history.json", "w") as file:
        json.dump({"history": history}, file, indent=4)

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
        if word not in ['*', '+', '/', '-', '(', ')']:
            print('Error: Invalid operator detected.')
            return False
    return True

# Advance the calculus
def update_calculus(operation, index, numbers, operators):
    # Save the result in a variable
    result = operation(numbers[index], numbers[index + 1])
    # If there was an error (e.g., division by zero)
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
    while '*' in operators or '/' in operators:
        # Isolate and execute each operation in the list
        for index, operator in enumerate(operators):
            if operator == '*':
                operation = multiply
                if not update_calculus(operation, index, numbers, operators):
                    # Exit on error (e.g., division by zero)
                    return False  
                break
            if operator == '/':
                operation = divide
                if not update_calculus(operation, index, numbers, operators):
                     # Exit on error (e.g., division by zero)
                    return False 
                break
    # No error occurred
    return True  


# Check for addition or substraction operators
def add_substract(numbers, operators):
    while '+' in operators or '-' in operators:
        for index, operator in enumerate(operators):
            if operator == '+':
                operation = add
                update_calculus(operation, index, numbers, operators)
                break
            if operator == '-':
                operation = substract
                update_calculus(operation, index, numbers, operators)

# Display history function
def display_history():
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
        history.clear()
        save_history()
        print("History deleted.")

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
    print("Choose an option:")
    print("1. Delete all history")
    print("2. Delete a specific entry")
    try:
        choice = int(input("Enter your choice (1-2): "))
        if choice == 1:
            delete_history()
        elif choice == 2:
            delete_history_operation()
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 2.")

# Menu function
def menu():
    while True:
        expression = input('Enter the operation (e.g., x + y - z), or type "exit" to quit:\n')
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
                add_substract(parenthese_numbers, parenthese_operators)
                del operators[p_index1:p_index2 + 1]
                del numbers[p_index1:p_index2]
                numbers.insert(p_index1, parenthese_numbers[0])

            # Perform the remaining calculations
            if not multiply_divide(numbers, operators):
                print("Calculation failed due to division by zero.")
                # Skip the current loop and ask for the next calculation
                continue  
            add_substract(numbers, operators)

            # Display the result
            if numbers:
                print(expression, '=', numbers[0])

                # Save the operation in the history
                history.append(f"{expression} = {numbers[0]}")
                save_history()

        else:
            print('Error, please try again.')

        # Clear memory
        numbers.clear()
        operators.clear()

# Main function to run the calculator program
def main():
    global history
    # Load history from the JSON file and assign it to the global variable   
    history = load_history()  
    while True:
        print("Choose an option:")
        print("1. Perform a calculation")
        print("2. Display history")
        print("3. Delete history")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                menu()
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

if __name__ == '__main__':
    main()
