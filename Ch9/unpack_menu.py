menu = {'drip': 1.95, 'cappuccino': 2.95, 'americano': 2.49}

a, b, c = menu.items()
print(a)  # prints ('drip', 1.95)
print(b)  # prints ('cappuccino', 2.95)
print(c)  # prints ('americano', 2.49)

(a_name, a_price), (b_name, b_price), *_ = menu.items()
print(a_name)   # prints 'drip'
print(a_price)  # prints 1.95
print(b_name)   # prints 'cappuccino'
print(b_price)  # prints 2.95
