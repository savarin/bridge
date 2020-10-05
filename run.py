import time

import wasmtime.loader

import primes


def nth(n):
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


def benchmark(expression, iterations, variant):
    # type: (str, int, str) -> None
    """Run benchmark on expression eval."""
    start = time.time()

    for i in range(iterations):
        print("{} of {}: {}".format(i + 1, iterations, eval(expression)))

    print("average time {}: {:3f}s\n".format(variant, (time.time() - start) / iterations))


if __name__ == "__main__":
    benchmark("nth(10000)", 3, "Python")
    benchmark("primes.nth(10000)", 3, "Rust")
