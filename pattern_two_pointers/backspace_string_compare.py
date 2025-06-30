def backspace_string_compare(s: str, t: str) -> bool:
    l, r = len(s)-1, len(t)-1
    while (l >= 0 or r >= 0):
        li = 0
        while (l >= 0):
            if s[l] == "#":
                li += 1
                l -= 1
            elif li > 0:
                li -= 1
                l -= 1
            else:
                break
        
        ri = 0
        while (r >= 0):
            if t[r] == "#":
                ri += 1
                r -= 1
            elif ri > 0:
                ri -= 1
                r -= 1
            else:
                break
        
        if (l >= 0 and r >= 0):
            if s[l] != t[r]:
                return False
            else:
                l -= 1
                r -= 1
        elif (l >= 0 or r >= 0):
            return False
        
    return True

if __name__ == "__main__":
    s = "ab#c"; t = "ad#c"
    # s = "ab##"; t = "c#d#"
    # s = "a#c"; t = "b"
    print(backspace_string_compare(s, t))