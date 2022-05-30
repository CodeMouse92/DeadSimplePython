import warnings

thumbs = "pricking"

if thumbs == "pricking":
    warnings.warn("Something wicked this way comes.", FutureWarning)

with open('locks.txt', 'w') as file:
    file.write("Whoever knocks")
