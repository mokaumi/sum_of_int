# Prompt the user to input three integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Calculate the sum, product, and average
sum_values = num1 + num2 + num3
product_values = num1 * num2 * num3
average_value = sum_values / 3

# Display the results
print(f"Sum: {sum_values}")
print(f"Product: {product_values}")
print(f"Average: {average_value:.2f}")
print("Thank you for your input")
