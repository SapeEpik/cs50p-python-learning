# Fun calculator

# Ask for two numbers and an operation
x = float(input("What's x? "))
y = float(input("What's y? "))
op = input("Operation (+, -, *, /): ")

# If the user chose "+", print the sum.
if op == "+":
    result = x + y
    print(f"The result is {result:,.0f}" if result.is_integer() else f"The result is {result:,.2f}")

# If the user chose "-", print the difference.
elif op == "-":
    result = x - y
    print(f"The result is {result:,.0f}" if result.is_integer() else f"The result is {result:,.2f}")

# If "*", print the product.
elif op == "*":
    result = x * y
    print(f"The result is {result:,.0f}" if result.is_integer() else f"The result is {result:,.2f}")

# If "/", first check that y isn’t 0.
# If it’s safe, do the division.
# Otherwise, show a friendly error.
elif op == "/":
    if y != 0:
        result = x / y
        print(f"The result is {result:,.0f}" if result.is_integer() else f"The result is {result:,.2f}")
    else:
        print("Cannot divide by zero!")
else:
    print("Unknown operation.")