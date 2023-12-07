# using the python lambda fuction create a fibonacci series from 1 to 50 elements


from functools import reduce

fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
print(fib(50))
