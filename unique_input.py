#initate the numbers and operators lists
numbers = []
operators = []

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
def update_calculus(parameter,index):
    #save the result in a variable
                result = parameter(numbers[index],numbers[index+1])
                #replace the first number by the result
                numbers[index] = result
                #remove the operator from the list
                operators.pop(index)
                #remove the second number from the list
                numbers.pop(index+1)

#input menu
def menu():
    while True:
        #ask the user for the operation
        og_input=input('Enter the operation like this : x + y - z \n:')
        sort_input(og_input)
        check_error()
        #check for multiply or divide operators
        while '*' in operators or '/' in operators:
            #isolate and execute each operator in the list
            for index, operator in enumerate(operators):
                if operator == '*':
                    #set the parameters for the function
                    parameter = multiply
                    #call the function
                    update_calculus(parameter,index)
                    break
                if operator == '/':
                    parameter = divide
                    update_calculus(parameter,index)
                    break
        #check for addition or substract operators
        while '+' in operators or '-' in operators:
            for index, operator in enumerate(operators):
                if operator == '+':
                    parameter = add
                    update_calculus(parameter,index)
                    break
                if operator == '-':
                    parameter = substract
                    update_calculus(parameter,index)
                    break
        print(og_input,'=',numbers[0])
        #clear memory
        numbers.clear()
        operators.clear()

if __name__ == '__main__':
    menu()