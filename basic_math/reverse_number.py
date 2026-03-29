"""
Reverse the digits of a number.

- in -> 12345 out -> 54321
- in -> 1200 out -> 21
"""

import math

def reverse_number(n: int) -> int:
    """
    Complexity Analysis:
        - Time -> O(log10 n)
        - Space -> O(1)
    """
    if n == 0:
        return 0
    
    out = 0
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    print(n)
    while (n > 0):
        digit = n % 10
        
        out = (10 * out) + digit
        n //= 10

    if int(math.log2(out)+1) >= 32:
        return 0
    return -out if is_negative else out



if __name__ == "__main__":
    # n = 12345
    # n = -1200
    # n = 0
    n = 1563847412
    print(reverse_number(n))