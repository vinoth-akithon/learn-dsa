"""


"""


def digit_product(n: int, ans: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(log10 n)
            - Space -> O(log10 n) -> due to recursion

    """
    # Base condition
    if n == 0:
        return ans
    
    return digit_product(n//10, ans = ans * (n%10))


def brute_force(n: int, t: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(log10 n * 10)
            - Space -> O(log10 n)
    """
    while True:
        if digit_product(n, 1) % t == 0:
            return n
        else:
            n += 1


if __name__ == "__main__":
    # n = 10; t = 2
    n = 15; t = 3

    # print(brute_force(n, t))
    print(digit_product(25, 1))