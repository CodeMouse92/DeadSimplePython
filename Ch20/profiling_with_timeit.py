from timeit import timeit

count = 10_000_000

def multiple_assign():
    x, y, z = 'foo', 'bar', 'baz'

time_multiple_assign = timeit(multiple_assign)

def single_assign():
    x = 'foo'
    y = 'bar'
    z = 'baz'

time_single_assign = timeit(single_assign)

print("Multiple assignment:", time_multiple_assign, sep='\t')
print("Individual assignment:", time_single_assign, sep='\t')
