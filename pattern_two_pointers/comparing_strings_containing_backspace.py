def comparing_strings_containing_backspace(s: str, t: str) -> bool:
    sn = len(s)
    tn = len(t)

    l, r = sn-1, tn-1
    while (l >= 0 or r >= 0):
        lbc = 0
        rbc = 0
        while l >= 0:
            if s[l] == "#":
                lbc += 1
            elif lbc > 0:
                lbc -= 1
            l -= 1
        while r >= 0:
            if t[r] == "#":
                rbc += 1
            elif rbc > 0:
                rbc -= 1
            r -= 1
        if l >= 0 and r >= 0:
            if s[l] != t[r]:
                return False
        elif l >= 0 or r >= 0:
            return False
        l -= 1
        r -= 1
        
    return True

def backspaceCompare(s: str, t: str) -> bool:
    def next_valid_char_index(string, index):
        backspace = 0
        while index >= 0:
            if string[index] == '#':
                backspace += 1
            elif backspace > 0:
                backspace -= 1
            else:
                break
            index -= 1
        return index

    i, j = len(s) - 1, len(t) - 1

    while i >= 0 or j >= 0:
        i = next_valid_char_index(s, i)
        j = next_valid_char_index(t, j)

        # Compare characters
        if i >= 0 and j >= 0:
            if s[i] != t[j]:
                return False
        elif i >= 0 or j >= 0:
            # One is finished, the other isn't
            return False

        i -= 1
        j -= 1

    return True


if __name__ == "__main__":
    # s = "xy#z"; t = "xzz#"
    s = "ab##"; t = "c#d#"
    # s = "a#c"; t = "b"
    s = ""; t = ""
    # s = ""; t = "x"

    print(comparing_strings_containing_backspace(s, t))
    # print(backspaceCompare(s, t))