from secret_agent import SecretAgent
mouse = SecretAgent("Mouse")
armadillo = SecretAgent("Armadillo")
fox = SecretAgent("Fox")

# SecretAgent._codeword = "Parseman"
# print(armadillo._codeword)  # prints "Parmesan"
# print(mouse._codeword)      # prints "Parsesan"

# mouse._codeword = "Cheese"
# print(mouse._codeword)      # prints "Cheese"
# print(armadillo._codeword)  # prints "Parmesan"

mouse.remember(("42.864025, -72.568511"))

SecretAgent.inform("The goose honks at midnight.")
print(mouse._codeword)      # prints "The goose honks at midnight."

fox.inform("The duck quacks at midnight.")
print(mouse._codeword)      # prints "The duck quacks at midnight."
