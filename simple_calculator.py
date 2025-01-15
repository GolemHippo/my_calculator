def add(x,y):
    return x + y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        print("can't divide by zero")
    else:
        return x/y
    
def calculator():
    
    try:
        x = float(input("Enter the first number : "))
        y = float(input("Enter the second number : "))
    except ValueError:
        print("Error.please choose a number!")
        return

    
    operation = input("Enter the operation (+, -, *, /) : ")

    
    if operation == "+":
        result = add(x,y)
    elif operation == "-":
        result = subtract(x,y)
    elif operation == "*":
        result = multiply(x,y)
    elif operation == "/":
        result = divide(x,y)
    else:
        print("Error : not-existent operation.")
        

    
    print(f"Result : {result}")
    
    again=input("Do you want to calculate again? (yes/no) : ")
    if again == "yes":
        calculator()
    else:
        print("Goodbye!")
        
    

  
calculator()





