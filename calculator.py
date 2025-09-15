# Fun calculator

# Ask for two numbers and an operation
x = int(input("What's x? "))
y = int(input("What's y? "))
op = input("Operation (+, -, *, /): ")

# If the user chose "+", print the sum.
if op == "+":
    print(f"The result of {x} + {y} is {x + y}")

# If the user chose "-", print the difference.
elif op == "-":
    print(f"The result of {x} - {y} is {x - y}")

# If "*", print the product.
elif op == "*":
    print(f"The result of {x} * {y} is {x * y}")

# If "/", first check that y isn’t 0.
# If it’s safe, do the division.
# Otherwise, show a friendly error.
elif op == "/":
    if y != 0:
        print(f"The result of {x} / {y} is {x / y}")
    else:
        print("Cannot divide by zero!")
else:
    print("Unknown operation.")