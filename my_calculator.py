#My Calculator

#List Setting
history_l=[]

#Input of Numbers and operator
def user_input():
    while True:
        try:
            first_number=float(input("Enter a number"))
            operation_sign=input("Enter the operation sign")
            second_number=float(input("Enter a number"))
        except ValueError:
            print("Enter a valid number")
        first_calculus=first_number, operation_sign, second_number
        return first_calculus
    
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

#Sorting Operators and formatting the int/float numbers
def calculus(first_calculus):
    first_number,operation_sign,second_number=first_calculus
    if operation_sign == '*':
        result=multiply(first_number,second_number)
    if operation_sign == '/':
        result=divide(first_number,second_number)
    if operation_sign == '+':
        result=add(first_number,second_number)
    if operation_sign == '-':
        result=substract(first_number,second_number)
    if operation_sign == '%':
        result=modulo(first_number,second_number)

    if first_number==int(first_number):
        first_number=int(first_number)
    if second_number==int(second_number):
        second_number=int(second_number)
    if result==int(result):
        result=int(result)

    calculus_result=first_number,' ',operation_sign,' ',second_number,' ','=',' ',round(result,4)
    return calculus_result

#Display of result
def display_result(calculus):
    print(('{}'*len(calculus)).format(*calculus))

#Memory Management
def display_history(history):
    history_l.append(history)
    return history_l

#Menu Loop
while True:
    choice=input('What do you want to do?\n"Calcul" or "History"')
    if choice=="Calcul":
        display_result(calculus(user_input()))
    if choice=="History":
        display_history(history_l)