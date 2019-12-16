# function solution return a object
def even_integers_function(num):
    result = []
    for i in range(num):
        if i % 2 == 0:
            result.append(i)
    return result

# generator solution return a generator
def even_integers_generator(num):
    for i in range(num):
        if i % 2 == 0:
            yield i

print(even_integers_function(10))
print(even_integers_generator(10))
print(list(even_integers_generator(10)))

# list comprehension
#newlist = [item.upper() for item in collection]
# generator expression
#(item.upper() for item in collection)

# function solution return a object LIKE a EXPRESSION
print("## function solution return a object LIKE a EXPRESSION")
even_integers = (n for n in range(10) if n%2==0)
print(even_integers)
print(list(even_integers))

# generator solution return a generator LIKE a EXPRESSION
numbers = [7,22,4.5,99.7,'3','5']   # list of mixed format numbers

# convert numbers to integers using expression
print("## convert numbers to integers using expression")
integers = (int(n) for n in numbers)
print(integers)
print(list(integers))

# User generator object
print("## User generator object")
integers = even_integers_generator(10)
print(integers)
# print(integers.next())
# print(integers.next())
for number in integers:
    print(number)

# Fibonacci sequence generator
def fibonacci_gen():
    trailing, lead = 0,1
    while True:
        yield lead
        trailing, lead = lead, trailing + lead
        if lead >= 150: break

fib = fibonacci_gen()
print(list(fib))
