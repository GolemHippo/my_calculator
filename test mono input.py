#initate the numbers and operators lists
numbers = []
operators = []

#input menu
while True:
    #ask the user for the operation
    og_input=input('Enter the operation like this : x + y - z \n:')

    #sort the values from the input to the proper list
    for word in og_input.split():
        try:
            numbers.append(float(word))
        except ValueError:
            operators.append(word)

    #check for error in operators
    for word in operators:
        if word != '*' and word != '+' and word != '/' and word != '-':
            print('error')
            break
    
    #check for operators priorities 
    for word in operators:
        if word == '*' or '/':
            priorities=word 
    
    #if conditions are met, call calculus functions in the correct order 

    print(numbers)
    print(operators)
    print(og_input)
    #need to reset the inital values


