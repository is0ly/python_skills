def factorial(n):
    if n == 1:
        return n
    factorial_n_minus_1 = factorial(n-1)
    return n * factorial_n_minus_1


print(factorial(21))
