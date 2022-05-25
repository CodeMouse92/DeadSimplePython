import time
# sleepy = ['no pause', time.sleep(1), time.sleep(2)]
# ...three second pause...
# print(sleepy[0])  # prints 'no pause'

sleepy = (time.sleep(t) for t in range(0, 3))
print("Calling...")
next(sleepy)
print("Done!")

# Not lazy
sleepy = (time.sleep(t) for t in [1, 2, 3, 4, 5])
