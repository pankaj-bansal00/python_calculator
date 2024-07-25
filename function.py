"""This is the add function"""             
def add(x,y):
    return x+y
"""this is the suctract function"""
def subtract(x,y):
    return x-y
"""this is the multiply fucntion"""
def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

while True:
    #take the input from user#
    num1 = int(input("enter the first number"))
    num2 = int(input("enter the second number"))
    
    #choose the operation from the user
    operator = int(input("""Enter the operation
                         1.add
                         2.sub
                         3.multi
                         4.divide
                         5.quit""")) 
    if operator == 5:
            print ("quit") 
            break   

    """conditions"""
    if operator == 1:
        result = add(num1,num2)
    elif operator == 2:
        result = subtract(num1,num2)
    elif operator == 3:
        result = multiply(num1,num2)
    elif operator == 4:
        result = divide(num1,num2)
    else:
        print("invalid")
    print(result)

