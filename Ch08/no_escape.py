def greet():
    name = input("What's your name? ")
    print(f"Hello, {name}.")


while True:
    try:
        greet()
        break
    except Exception:
        print("Error caught")
