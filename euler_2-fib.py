"""

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.

"""

"""
sum = 0

def Fib(n: object) -> object:
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fib(n-1)+Fib(n-2)

for number in range(0, 10):
    print()
    sum = Fib(number)
    print(sum)

"""

def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)


for index, fibonacci_number in zip(range(10), fib()):
     print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))




def rec_fib(n):
    '''inefficient recursive function as defined, returns Fibonacci number'''
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n

"""
for i in range(40):
    print(i, rec_fib(i))
"""

for i in range(40):
    if (i % 2 == 0) and (i < 400000):
        print(rec_fib(i))


# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
print(a)
a, b = b, a+b