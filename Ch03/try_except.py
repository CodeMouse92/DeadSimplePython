num_from_user = input("Enter a number: ")

try:
    num = int(num_from_user)
except ValueError:
    print("You didn't enter a valid number.")
    num = 0

print(f"Your number squared is {num**2}")
