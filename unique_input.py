#initate the numbers and operators lists
numbers = []
operators = []
l_numbers = []
l_operators = []

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
            numbers.clear()
            operators.clear()
            break

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

#menu function
def menu(operators, numbers):
    while True:
        #ask the user for the operation
        og_input=input('Enter the operation with a space between each number and operator : x + y - z \n:')
        sort_input(og_input)
        check_error()
        #check for parentheses
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
        #finish the calculus
        multiply_divide(numbers,operators)
        add_substract(numbers,operators)
        #print the result
        print(og_input,'=',numbers[0])
        #clear memory
        numbers.clear()
        operators.clear()

if __name__ == '__main__':
    menu(operators, numbers)