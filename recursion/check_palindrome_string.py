"""
Palindrome means, if reversed string becomes ideal to the original string.

check_palindrome_string(0, len(s)-1)
    | if matched
    check_palindrome_string(1, len(s)-2)
        | if matched
        check_palindrome_string(2, len(s)-3) -> return True (l >= r)

"""


def check_palindrome_string(s: str, l: int, r: int):
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n) -> Due to recursive stack
    """
    # Base condition
    if l >= r:
        return True
    
    if s[l] != s[r]:
        return False
    return check_palindrome_string(s, l+1, r-1)


if __name__ == "__main__":
    s = "a"
    print(check_palindrome_string(s, 0, len(s)-1))