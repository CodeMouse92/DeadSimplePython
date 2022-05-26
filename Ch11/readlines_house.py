with open('78SomewhereRd.txt', 'r') as house:
    lines = house.readlines()
    for line in lines:
        print(line.strip())
