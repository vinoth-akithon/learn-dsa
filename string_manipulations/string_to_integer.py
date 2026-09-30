"""

"""
INT_MIN = -2**31
INT_MAX = 2**31 -1

def get_integer(str_num: str) -> int:
    """
        1234 -> 4-1 => 3  (1 * 10^3) -> 1000
        234 -> 3-1 -> 2 (2 * 10^2) -> 200
        34 -> 2-1 -> 1 (3 * 10^1) -> 30
        4 -> 1-1 -> 0 (4 * 10^0) -> 4
    
    """
    # Base condition
    n = len(str_num)
    if n == 0:
        return 0

    res = get_integer(str_num[1:])
    res += int(str_num[0]) * (10 ** (n-1))
    return res

def get_integer_better(s: str, i: int, num: int, sign: int) -> int:
    """
    
    """
    n = len(s)
    # Base condition
    if i >= n or not s[i].isdigit():
        return num * sign

    num = num * 10 + int(s[i])
    if sign * num < INT_MIN: return INT_MIN
    if sign * num > INT_MAX: return INT_MAX

    return get_integer_better(s, i+1, num, sign)
    

def brute_force(s: str) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n (for taking digits) + n (for converting str to int))
            - Space -> O(n (for recursion) + n (copying the digit string))
    """
    n = len(s)
    i = 0

    # Removing leading whitespace
    while i < n and s[i] == " ":
        i += 1

    # If all are whitespace, early return
    if i == n:
        return 0

    is_positive = True
    if s[i] == "-":
        is_positive = False
        i += 1
    elif s[i] == "+":
        i += 1

    # If the first char is not digit, early return
    if not s[i].isdigit():
        return 0

    # Collecting consecutive digits
    j = i
    while j < n and s[j].isdigit():
        j += 1

    str_num = s[i:j]
    # print(f"number :{'' if is_positive else '-'}{str_num}")

    integer = get_integer(str_num)
    
    if is_positive and integer > 2147483647:
        return 2147483647
    elif not is_positive and integer > 2147483648:
        return -2147483648
    else:
        return integer if is_positive else integer * (-1)


def better_approach(s: str) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n (for taking digits) + n (for converting str to int))
            - Space -> O(n (for recursion))
    """
    n = len(s)
    i = 0
    

    # Removing leading whitespace
    while i < n and s[i] == " ":
        i += 1

    sign = 1
    if i < n and s[i] in ["-", "+"]:
        sign = 1 if s[i] == "+" else -1
        i += 1

    return get_integer_better(s, i, 0, sign)

if __name__ == "__main__":
    s = " -00012345abc"
    # s = "4193 with words"
    # print(brute_force(s))
    # print(get_integer("23"))
    print(better_approach(s))
    # print(get_integer_better("1234", 0))