# Arithmatic functions
def add(a,b):
  return(a+b)
  
def subtract(a,b):
  return a-b
  
def multiply (a,b):
  return a*b

def divide(a,b):
  try:
    return a/b
  except Exception as e:
    print(e)
    
def power(a,b):
  return a**b
  
def remainder(a,b):
  return a%b
  
def history(a):
  for items in a:
    print(items)

def select_op(choice):
  if (choice == '#'):
    return -1
      
  elif (choice == '$'):
    return 0
      
  elif (choice == '?'):
    if (history_list == []):
      print("No past calculations to show")
      return 0
    elif (history_list != []):
      return history(history_list)
      
  elif (choice in ('+','-','*','/','^','%')):
    # first_input
    while (True):
      input1 = str(input("Enter first number: "))
      print(input1)
      if input1.endswith('#'):
        return -1
      if input1.endswith('$'):
        return 0
      try:
        num1 = float(input1)
        break
      except:
        print("Not a valid number,please enter again")
    
    # first_input    
    while (True):
      input2 = str(input("Enter second number: "))
      print(input2)
      if input2.endswith('#'):
        return -1
      if input2.endswith('$'):
        return 0
      try:
        num2 = float(input2)
        break
      except:
        print("Not a valid number,please enter again")
   
    # calculation
    result = 0.0
    last_calculation = ""    
    while (True):
      if choice == '+':
        result = add(num1,num2)
      elif choice == '-':
        result = subtract(num1,num2)
      elif choice == '*':
        result = multiply(num1,num2)
      elif choice == '/':
        result =  divide(num1,num2)
      elif choice == '^':
        result = power(num1,num2)
      elif choice == '%':
        result = remainder(num1,num2)
      break
  
    last_calculation =  "{0} {1} {2} = {3}".format(num1, choice, num2, result) 
    print(last_calculation )
    history_list.append(last_calculation)
    
  else:
      print("Unrecognized operation")
      
history_list = []
# MAIN LOOP
while (True):
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  print("8.History  : ? ")
  
  choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
  print(choice)
  if (select_op(choice) == -1):
    print("Done. Terminating")
    exit()