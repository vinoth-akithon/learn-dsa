def print_n_1_using_forward_recursion(n: int) -> None:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n) -> Due to recursive stack
    """
    # Base condition
    if n == 0:
        return 
    print(n)
    print_n_1_using_forward_recursion(n-1)


def print_n_1_using_backtracking(n: int, c: int) -> None:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n) -> Due to recursive stack
    """
    # Base Condition
    if c > n:
        return 
    print_n_1_using_backtracking(n, c+1)
    print(c)

if __name__ == "__main__":
    n = 3
    c = 1
    print_n_1_using_forward_recursion(n)
    print()
    print_n_1_using_backtracking(n, c)