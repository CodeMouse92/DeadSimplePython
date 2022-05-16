temps = [87, 76, 79]
highs = temps
print(temps is highs)  # prints True
temps += [81]
print(temps is highs)  # prints True
print(highs)           # prints [87, 76, 79, 81]
print(temps)           # prints [87, 76, 79, 81]
