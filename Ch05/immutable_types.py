eggs = 12
carton = eggs
print(eggs is carton)  # prints True
eggs += 1
print(eggs is carton)  # prints False
print(eggs)            # prints 13
print(carton)          # prints 12
