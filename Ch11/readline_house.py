with open('78SomewhereRd.txt', 'r') as house:
    line1 = house.readline()
    line2 = house.readline()
    print(repr(line1))
    print(repr(line2))
