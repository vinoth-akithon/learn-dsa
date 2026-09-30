"""

"""


def sum_of_first_n_number(n: int):
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n) -> Due to recursive stack
    """
    # Base condition
    if n < 2:
        return n
    return n + sum_of_first_n_number(n-1)


if __name__ == "__main__":
    n = 5
    print(sum_of_first_n_number(n))