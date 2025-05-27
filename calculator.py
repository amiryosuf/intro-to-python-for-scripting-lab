"Prompts the user to enter two numbers and an operator"
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

#Use if-elif-else statements to perform the operation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operator. Please use +, -, *, or /."
# Print the result
print(f"The result of {num1} {operator} {num2} is: {result}")
# This script performs a basic calculator operation based on user input.
# It prompts the user for two numbers and an operator, performs the operation,
# and prints the result. It handles division by zero and invalid operators gracefully.

Enter the first number: 1
Enter an operator (+, -, *, /): *
Enter the second number: 5
Result: 6.0