"""

"""
def get_pos_pow(x: int, n: int, i: int, ans) -> int:
    # Base condition
    if i > n:
        return ans
    
    ans *= x
    return get_pos_pow(x, n, i+1, ans)

def get_neg_pow(x: int, n: int, i: int, ans: int) -> int:
    # Base condition
    if i == 0:
        return ans

    ans /= x
    return get_neg_pow(x, n, i-1, ans)
    

def brute_force(x: int, n: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n) -> Due to recursion space
    """
    return get_neg_pow(x, abs(n), abs(n), 1) if n < 0 else get_pos_pow(x, n, 1, 1)


def better_approach(x: int, n: int) -> int:
    """
            - Complexity Analysis:
                - Time -> O(n)
                - Space -> O(n) -> Due to recursion space
    """
    if n < 0:
        return 1/get_pos_pow(x, abs(n), 1, 1)
    else:
        return get_pos_pow(x, n, 1, 1)


def pow_x_to_n(x: int, n: int) -> int:
    """
    
    """
    # Base condition
    if n == 0:
        return 1

    if n % 2 == 0:
        return pow_x_to_n(x*x, n//2)
    else:
        return x * pow_x_to_n(x, n-1)


def optimal_approach(x: int, n: int):
    """
        - Complexity Analysis:
            - Time -> O(log n)
            - Space -> O(log n)
    """
    if n < 0:
        n = -n
        return 1/pow_x_to_n(x, n)
    else:
        return pow_x_to_n(x, n)



if __name__ == "__main__":
    # x = 3; n = 4
    x = 2; n = -2
    print(brute_force(x, n))
    print(better_approach(x, n))
    print(optimal_approach(x, n))
