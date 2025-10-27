def valid_palindrome(s: str) -> bool:
    n = len(s)
    l, r = 0, n-1

    while (l < r):
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1
    return True
        

if __name__ == "__main__":
    # s = "A man, a plan, a canal: Panama"
    s = "race a car"
    print(valid_palindrome(s))