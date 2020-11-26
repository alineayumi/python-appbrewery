from art import logo

# Calculator
def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return (n1 / n2)

print(logo)

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  is_done = False
  num1 = float(input("What is the 1st number? "))
  for symbol in operations:
    print(symbol)

  while not is_done:
    operation_symbol = input("Pick an operation from the line above: ")

    num2 = float(input("What is the next number? "))
    result = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    is_done = (input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'n')
    if not is_done:
      num1 = result
    else:
      calculator()
calculator()
    
