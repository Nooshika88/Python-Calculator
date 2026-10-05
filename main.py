print("welcome to calculator! type /open/ to start and/ exit/ to turn off.")
exit_open = input("enter 'open' or 'exit' : ")

while True:

    
    if exit_open == "exit":
        print("culculator turned off. you can restart by typing 'open' anything")
        exit_open = input(" ")


    elif exit_open == "open":

        while True:
            operation = input("Enter operation (+, -, *, /, %, **,  and √(square root) or 'exit' : )")

            if operation == "exit":
                print("culculator turned off. you can restart by typing 'open' anything")
                exit_open = input(" ")
                continue

            elif operation == "√":
                number = float(input("Enter a number for square root: "))
                result = "Error...." if (number < 0 ) else number ** 0.5
                print(f"√{number} = {result}")
            
            elif operation == "%":
                number1 = float(input("Enter the percentage: "))
                number2 = float(input("Enter the number: "))
                result = (number1 * number2) / 100
                print(f"{number1}% of {number2} = {result}")

            else:

                number1 = float(input("Enter first number: "))
                number2 = float(input("Enter scecond number: "))
                if operation == "+":
                    result = number1 + number2

                elif operation == "-":
                    result = number1 - number2

                elif operation == "*":
                    result = number1 * number2

                elif operation == "/":
                    result = number1 / number2

                elif operation == "^":
                    result = number1 ** number2
                
                else:
                    result = "invalid operation"
                print(f"{number1} {operation} {number2} = {result}")

    else:
            exit_open = input("Error!...just typing 'open' or 'exit' ")
            continue

        
