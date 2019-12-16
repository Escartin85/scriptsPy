from time import perf_counter
from timeit import timeit

items = {
    'a': 1,
    'b': 2,
}

default = -1

# Sum 1....n with a for loop
def upto_for(num):
    total = 0
    for i in range(num):
        total += i
    return total

# Sum 1...n with built-in sum and range
def upto_sum(num):
    return sum(range(num))

# Use try/catch to get a key with defualt
def use_catch(key):
    try:
        return items[key]
    except KeyError:
        return default

# Use dict.get to get a key with default
def use_get(key):
    return items.get(key, default)


if __name__ == "__main__":
    n = 1_000_000

    start = perf_counter()
    upto_for(n)
    duration = perf_counter() - start
    print("upto_for", duration)

    start = perf_counter()
    upto_sum(n)
    duration = perf_counter() - start
    print("upto_sum", duration)

    # Key is in the dictionary
    print('catch', timeit('use_catch("a")', 'from __main__ import use_catch'))
    print('get', timeit('use_get("a")', 'from __main__ import use_get'))

    # Key is missing from the dictionary
    print('catch', timeit('use_catch("x")', 'from __main__ import use_catch'))
    print('get', timeit('use_get("x")', 'from __main__ import use_get'))
