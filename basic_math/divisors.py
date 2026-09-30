"""

"""
import math


def naive_approach(n: int) -> list[int]:
    """
        Time -> O(n)
        Space -> O(d) where d is number of divisors
    """
    out = []
    for i in range(1, n+1):
        if n % i == 0:
            out.append(i)
    
    return out


def optimal_approach(n: int) -> list[int]:
    """
        Approach: 
            - Square root symmetric property
            - If the d is divisor of n, n/d is also a divisor of n
            - Example:
                - 3 is a divisor of 36.
                - 36/3 = 12 is also a divisor of 36. 
        Complexity Analysis:
            - Time -> O(sqrt(n))
            - Space -> O(d) where d is number of divisors
    """
    out = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            out.append(i)
            if i != (n//i):
                out.append(n//i)
    return out

if __name__ == "__main__":
    # n = 36
    n = 16
    print(naive_approach(n))    
    print(optimal_approach(n))