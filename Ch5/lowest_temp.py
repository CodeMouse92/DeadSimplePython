def find_lowest(temperatures):
    # temperatures.sort()
    # print(temperatures[0])
    sorted_temps = sorted(temperatures)  # sorted returns a new list
    print(sorted_temps[0])


temps = [85, 76, 79, 72, 81]
find_lowest(temps)
print(temps)
