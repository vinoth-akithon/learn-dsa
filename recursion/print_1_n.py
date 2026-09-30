def print_1_n_using_backtracing(n: int) -> None:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n) -> Due to recursive stack
    """
    # Base condition
    if n == 0:
        return
    print_1_n_using_backtracing(n-1)
    print(n)


def print_1_n_using_forward_recursion(n: int, c) -> None:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n) -> Due to recursive stack
    """
    # Base condition
    if c > n:
        return
    print(c)
    print_1_n_using_forward_recursion(n, c+1)


if __name__ == "__main__":
    n = 1
    c = 1
    print_1_n_using_backtracing(n)
    print()
    print_1_n_using_forward_recursion(n, c)