name = input("What's your name? ").strip().title()
parts = name.split()

if parts:  # make sure it isn't empty
    full_name = " ".join(parts)
    print(f"Hello, {full_name}!")
else:
    print("Hello there!")