# house = open("213AnywhereAve.txt")
# try:
#     print(house.read())
# finally:
#     house.close()

with open("213AnywhereAve.txt") as house:
    print(house.read())
