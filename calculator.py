print("simple calculator")

while True:

    number1 = int(input("enter first number: "))                
    number2 = int(input("enter second number: "))

    operation = input("choose operation (+, -, *, / or q to quit): ")

    if operation == "q":
        break

    if operation == "+":
        result = number1 + number2
        print("result:", result)

    elif operation == "-":
          result = number1 - number2
          print("result:", result)

    elif operation == "*":
         result = number1 * number2
         print("result:", result)

    elif operation == "/":
          result = number1 / number2
          print("result:", result)

    else:
        print("invalid operation")