import time

import wasmtime.loader

import lib


def prime(n):
    # type: (int) -> int
    """Calculates the nth prime number."""
    if n == 0:
        return 2

    primes = [3]
    recent = 3
    count = 1

    while count < n:
        recent += 2
        is_prime = True

        for item in primes:
            if recent % item == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(recent)
            count += 1

    return primes[n - 1]


def pi():
    # type: () -> float
    """Calculates pi, as per https://github.com/JuliaLang/Microbenchmarks"""
    sum = 0.0

    for j in range(1, 501):
        sum = 0.0

        for k in range(1, 10001):
            sum += 1.0 / (k * k)

    return sum


def fibonacci(n):
    # type: (int) -> int
    """Calculates the nth Fibonacci number, as per https://github.com/JuliaLang/Microbenchmarks"""
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def benchmark(expression, iterations, variant):
    # type: (str, int, str) -> None
    """Run benchmark on expression eval."""
    start = time.time()

    for i in range(iterations):
        result = eval(expression)

    average = (time.time() - start) / iterations
    print("average time (out of {}) {}: {:3f}s".format(iterations, variant, average))


if __name__ == "__main__":
    print("Calculating 10,000th prime number")
    assert prime(10000) == 104743
    assert lib.prime(10000) == 104743
    benchmark("prime(10000)", 3, "Python")
    benchmark("lib.prime(10000)", 3, "Rust")

    print("\nCalculating pi")
    assert abs(pi() - 1.644834071848065) < 1e-6
    assert abs(lib.pi() - 1.644834071848065) < 1e-6
    benchmark("pi()", 3, "Python")
    benchmark("lib.pi()", 3, "Rust")

    print("\nCalculating 25th Fibonacci number")
    assert fibonacci(25) == 75025
    assert lib.fibonacci(25) == 75025
    benchmark("fibonacci(25)", 3, "Python")
    benchmark("lib.fibonacci(25)", 3, "Rust")
