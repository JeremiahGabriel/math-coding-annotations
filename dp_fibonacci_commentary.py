def fibonacci(n):
    # Calculates the nth Fibonacci number using bottom-up dynamic programming.

    if n <= 1:
        return n

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


# Example
n = 10
print("Fibonacci number at position", n, "is", fibonacci(n))  # Output: 55
