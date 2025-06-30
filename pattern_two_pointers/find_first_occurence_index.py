def first_first_occurence_index(left: str, right: str):
    ln, rn = len(left), len(right)
    if rn == 0:
        return 0
    elif (ln < rn):
        return -1
    for i in range(ln - rn + 1):
        l = i
        r = 0
        while (left[l] == right[r]):
            if r == rn-1:
                return i
            l += 1
            r += 1
    return -1

if __name__ == "__main__":
    left = "sadbutsad"; right = "sad"
    # left = "leetleeto"; right = "leeto"
    # left = "leetcode"; right = "leeto"
    # left = "aaa"; right = "aaaa"
    print(first_first_occurence_index(left, right)) 
    