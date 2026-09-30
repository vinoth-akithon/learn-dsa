"""
"""


def check_armstrong(x: int) -> int:
    """
        - Complexity Analysis
            - Time -> O(log10 n) -> No of digits
            - Space -> O(1)
    """
    inp = x
    count = 0
    while (inp > 0):
        count += 1
        inp //= 10

    inp = x
    out = 0
    while (inp > 0):
        digit = inp % 10
        out += digit ** count
        inp //= 10
    return x == out

    

    

if __name__ == "__main__":
    # x = 153
    x = 371
    print(check_armstrong(x))