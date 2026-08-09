try:
    x = int(input("Enter a number: "))
    if x < 0:
        raise ValueError("Negative value entered")
    print(f"You entered: {x}")
except ValueError as ve:
    print(f"Error: {ve}")
finally:
    print("End of the program.")