num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
opp = input("Choose the operation (+, -, *, /): ")

match opp:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 == 0:
            print("can not divide by zero.")
        else:
            result = num1 / num2
print("The result is " + str(result))