def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
                "+": add,
                "-": subtract,
                "*": multiply,
                "/": divide                
}

print("Operations:")
for key, value in operations.items() :
    print (key)

def calculator():
  num1= float(input("What's the first number?: "))
  continue_flag = True

  while continue_flag:
    operation_operator = input("Pick an operation: ")
    num2 = float(input("What's the second number?: "))
    calc = operations[operation_operator]
    answer = calc(num1, num2)

    print(f"{num1} {operation_operator} {num2} = {answer}")

    if input(f"Continue calculating? with {answer}?\n [y/n]\n") == "y":
      num1 = answer
    else:
      restart_flag = True
      while restart_flag:
        restart = input(f"Would you like to restart? [y/n]\n")
        if restart == "n":
          restart_flag = False
  
        else:
          num1= float(input("What's the first number?: "))
          for operator in operations:
            continue_flag = True

            while continue_flag:
              operation_operator = input("Pick an operation: ")
              num2 = float(input("What's the second number?: "))
              calc = operations[operation_operator]
              answer = calc(num1, num2)

              print(f"{num1} {operation_operator} {num2} = {answer}")
    
      else:
        continue_flag = False
        print("Goodbye.")
    

calculator()
