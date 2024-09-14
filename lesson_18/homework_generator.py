def even_numbers(n):    # Generator for a sequence of even numbers from 0 to N.
    for i in range(0, n + 1, 2):
        yield i


def fibonacci(n):   # Fibonacci sequence generator up to a certain number ( N ).
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
