from collections import deque
customers = deque(['Daniel', 'Denis'])

customers.append('Simon')
print(customers)     # prints deque(['Daniel', 'Denis', 'Simon'])

customer = customers.popleft()
print(customer)      # prints 'Daniel'
print(customers)     # prints deque(['Denis', 'Simon'])

customers.appendleft('James')
print(customers)     # prints deque(['James', 'Denis', 'Simon'])

last_in_line = customers.pop()
print(last_in_line)  # prints 'Simon'

print(customers)     # prints deque(['James', 'Denis'])
