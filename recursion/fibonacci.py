def nth_fib_recursive(n: int) -> int:
    if n < 2:
        return n
    return nth_fib_recursive(n-1) + nth_fib_recursive(n-2) # recurrance relation


def nth_fib_iterative(n: int) -> int:
    if n < 2:
        return n
    fibonacci = [0, 1]
    while len(fibonacci) <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[-1]

if __name__ == "__main__":
    print(nth_fib_recursive(5))
    print(nth_fib_iterative(5))