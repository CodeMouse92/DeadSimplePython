greeting = "Hello"
name = "Jason"
# message = greeting + ", " + name + "!"  # value is "Hello, Jason!"
message = "".join((greeting, ", ", name, "!"))  # value is "Hello, Jason!"
print(message)
