from collections import deque

customers = deque(['Kyle', 'Simon', 'James'])
customers.append('Daniel')

# first, second, third, _ = customers
# first, second, _, _ = customers
first, second, *rest = customers
print(first)   # prints 'Kyle'
print(second)  # prints 'Simon'
print(rest)    # prints ['James', 'Daniel']

first, *middle, last = customers
print(first)   # prints 'Kyle'
print(middle)  # prints '['Simon', 'James']
print(last)    # prints 'Daniel'

*_, second_to_last, last = customers
print(second_to_last)  # prints 'James'
print(last)            # prints 'Daniel'
