def main():
    #Get user input for two numbers and an operator
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the seconf number: "))
    operator = input("Enter the operator(+, -, *, /):")

    #Perform the operation based on the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1*num2
    elif operator == '/':
        if num2 == 0:
            print ("Error:Division by zero")

            return
        result = num1 / num2
    else:
        print ("invalid operator")
        return
    
    #print the result
    print(f"{num1} {operator} {num2} = {result}")


if __name__ == "__main__":
    main()