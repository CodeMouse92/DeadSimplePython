with open("213AnywhereAve.txt", 'r') as file:
    print(file.readable())  # prints 'True'
    print(file.writable())  # prints 'False'
    print(file.seekable())  # prints 'True'
