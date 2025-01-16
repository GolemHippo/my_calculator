#initate the numbers and operators lists
numbers = []
operators = []
l_numbers = []
l_operators = []
history =[]

#define the operations functions
def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulo(x,y):
    return x % y


#define the sorting function for operators and numbers
def sort_input(og_input):
    for word in og_input.split():
        try:
            numbers.append(float(word))
        except ValueError:
            operators.append(word)

#check for errors in the operators list
def check_error():
    for word in operators:
        if word != '*' and word != '+' and word != '/' and word != '-' and word != '(' and word != ')':
            print('error')
            return False
        else:
            return True

def check_parentheses(operators, numbers):
    while '(' in operators:
        #find the index of the first parenthese
        p_index = operators.index('(')
        #find the index of the closing parenthese
        p_index2 = operators.index(')')
        #isolate the operation between the parentheses
        parenthese_operators = operators[p_index+1:p_index2]
        #isolate the numbers between the parentheses
        parenthese_numbers = numbers[p_index:p_index2]
        #check for multiply or divide operators
        multiply_divide(parenthese_numbers,parenthese_operators)
        add_substract(parenthese_numbers,parenthese_operators)
        #delete the parentheses from the lists
        del operators[p_index:p_index2+1]
        del numbers[p_index:p_index2]
        #replace the parentheses by the result
        numbers.insert(p_index,parenthese_numbers[0])

#advance the calculus
def update_calculus(operation,index,l_numbers,l_operators):
                #save the result in a variable
                result = operation(l_numbers[index],l_numbers[index+1])
                #replace the first number by the result
                l_numbers[index] = result
                #remove the operator from the list
                l_operators.pop(index)
                #remove the second number from the list
                l_numbers.pop(index+1)

#check for multiply or divide operators
def multiply_divide(l_numbers,l_operators):
     while '*' in l_operators or '/' in l_operators:
            #isolate and execute each operation in the list
            for index, operator in enumerate(l_operators):
                if operator == '*':
                    #set the parameters for the function
                    operation = multiply
                    #call the function
                    update_calculus(operation,index,l_numbers,l_operators)
                    break
                if operator == '/':
                    operation = divide
                    update_calculus(operation,index,l_numbers,l_operators)
                    break

#check for addition or substract operators
def add_substract(l_numbers,l_operators):
    while '+' in l_operators or '-' in l_operators:
        for index, operator in enumerate(l_operators):
            if operator == '+':
                operation = add
                update_calculus(operation,index,l_numbers,l_operators)
                break
            if operator == '-':
                operation = substract
                update_calculus(operation,index,l_numbers,l_operators)
                break

#history functions

#display history
def display_history(history):
    if not history :
        print("history is empty")
    else:
        print("History:")
        for i, operation in enumerate(history, 1):
            print(f"{i}. {operation}")

#delete history
def delete_history(history):
    history.clear()
    print("History deleted")

#delete a specific entry
def delete_history_operation(history):
    display_history(history)
    try:
        index = int(input("Enter the index of the operation to delete: "))
        if 0 <= index - 1 < len(history):
            del history[index - 1]
            print("History operation deleted")
        else:
            print("Invalid index. Please enter a number between 1 and", len(history))
    except ValueError:
        print("Invalid index. Please enter a number between 1 and", len(history))

#delete history options
def delete_history_options(history):
    print("Choose an option:")
    print("1. Delete all history")
    print("2. Delete a specific entry")
    try:
        choice = int(input("Enter your choice (1-2): "))
        if choice == 1:
            delete_history(history)
        elif choice == 2:
            delete_history_operation(history)
        
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 2.")

#operations menu
def menu(operators, numbers):
    while True:
        #ask the user for the operation
        og_input=input('Enter the operation with a space between each number and operator : x + y - z \nIf you want to exit calculation, enter "exit"\n:')
        #exit the loop if the user wants to
        if og_input == 'exit':
            break
        #sort the input
        sort_input(og_input)
        #check for errors before starting the calculus
        if check_error() == True:
            try:
                #check for parentheses
                check_parentheses(operators, numbers)
                #finish the calculus
                multiply_divide(numbers,operators)
                add_substract(numbers,operators)
                #print the result
                print(og_input,'=',numbers[0])
                #save the operation in the history
                history.append(og_input + ' = ' + str(numbers[0]))
            except ZeroDivisionError:
                print('Error, division by zero')
        else:
            print('Error, please try again')
        #clear memory
        numbers.clear()
        operators.clear()

#main menu function
def main():
    while True:
        print("Choose an option:")
        print("1. Perform a calculation")
        print("2. Display history")
        print("3. Delete history")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                menu(operators, numbers)
            elif choice == 2:
                display_history(history)
            elif choice == 3:
                delete_history_options(history)
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()