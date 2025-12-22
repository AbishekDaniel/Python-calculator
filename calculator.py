# Arithmetic functions
def add(a,b):
    return a + b
    
def subtract(a,b):
    return a - b
    
def multiply(a,b):
    return a * b
    
def divide(a,b):
    try:
        return a / b
    except:
        print("float division by zero")
        return None
    
    
def power(a,b):
    return a ^ b
    
def remainder(a,b):
    return a % b

# select_op function
def select_op(choice):
    if choice == "#":
        return -1
    
    elif choice == "$":
        print("Resetting...")
        return 0
      
    elif choice not in ("+","-","*","/","^","%","#","$"):
        print("Unrecognized operation")
        return 0
        
    #first input number    
    while True:
        input1 = input("Enter first number: ")
        print(input1)
        
        if input1.endswith("#"):
            return -1
            
        if input1.endswith("$"):
            return 0
            
        try:
            first_num = float(input1)
            break
        except:
            print("Not a valid number,please enter again")
    
    #second input number        
    while True:
        input2 = input("Enter second number: ")
        print(input2)
        
        if input2.endswith("#"):
            return -1
            
        if input2.endswith("$"):
            return 0
            
        try:
            second_num = float(input2)
            break
        except:
            print("Not a valid number,please enter again")
            
    #calculation
    if choice == "+":
        result = add(first_num, second_num)
        print(first_num,"+",second_num,"=",result )
        
    if choice == "-":
        result = substract(first_num, second_num)
        print(first_num,"-",second_num,"=",result )
        
    if choice == "*":
        result = multiply(first_num, second_num)
        print(first_num,"*",second_num,"=",result )
    
    if choice == "/":
        result = divide(first_num, second_num)
        print(first_num,"/",second_num,"=",result )
        
    if choice == "^":
        result = power(first_num, second_num)
        print(first_num,"^",second_num,"=",result )
        
    if choice == "%":
        result = reminder(first_num, second_num)
        print(first_num,"%",second_num,"=",result )
        return 0

# MAIN LOOP      
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)

    if select_op(choice) == -1:
        print("Done. Terminating")
        exit()