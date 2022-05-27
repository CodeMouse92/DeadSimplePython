class CafeQueue:

    def __init__(self):
        self._queue = []
        self._orders = {}
        self._togo = {}

    def __iter__(self):
        return CafeQueueIterator(self)

    def add_customer(self, customer, *orders, to_go=True):
        self._queue.append(customer)
        self._orders[customer] = tuple(orders)
        self._togo[customer] = to_go

    def __len__(self):
        return len(self._queue)

    def __contains__(self, customer):
        return (customer in self._queue)


class CafeQueueIterator:

    def __init__(self, cafe_queue):
        self._cafe = cafe_queue
        self._position = 0

    def __next__(self):
        try:
            customer = self._cafe._queue[self._position]
        except IndexError:
            raise StopIteration

        orders = self._cafe._orders[customer]
        togo = self._cafe._orders[customer]
        self._position += 1

        return (customer, orders, togo)

    def __iter__(self):
        return self


queue = CafeQueue()
queue.add_customer('Newman', 'tea', 'tea', 'tea', 'tea', to_go=False)
queue.add_customer('James', 'medium roast drip, milk, 2 sugar substitutes')
queue.add_customer('Glen', 'americano, no sugar, heavy cream')
queue.add_customer('Jason', 'pumpkin spice latte', to_go=False)

print(len(queue))       # prints 4
print('Glen' in queue)  # prints True
print('Kyle' in queue)  # prints False


def brew(order):
    print(f"(Making {order}...)")
    return order


for customer, orders, to_go in queue:
    for order in orders: brew(order)
    if to_go:
        print(f"Order for {customer}!")
    else:
        print(f"(Takes order to {customer})")
