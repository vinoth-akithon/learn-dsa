"""

factorial(3) = 3 * factorial(2)
                        |
                    2 + factorial(1)
                            |
                            1 + factorial(0)
                                    |
                                    1
"""



def factorial_of_given_number(n: int):
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n) -> Due to recursive stack
    """
    # Base condition
    if n == 0:
        return 1
    
    return n * factorial_of_given_number(n-1)



if __name__ == "__main__":
    n = 3
    print(factorial_of_given_number(n))