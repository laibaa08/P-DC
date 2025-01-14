def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /, %): ")
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid Operation"
    
    return f"The result is: {result}"

if __name__ == "__main__":
    print(calculator())
