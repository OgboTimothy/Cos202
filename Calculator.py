print("CALCULATOR")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

match operator:
    case "+":
        print("Answer =", num1 + num2)

    case "-":
        print("Answer =", num1 - num2)

    case "*":
        print("Answer =", num1 * num2)

    case "/":
        if num2 != 0:
            print("Answer =", num1 / num2)
        else:
            print("Error! Cannot divide by zero.")

    case _:
        print("Invalid operator!")
