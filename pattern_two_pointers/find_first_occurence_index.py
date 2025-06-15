def first_first_occurence_index(left: str, right: str):
    l, r, ln, rn, i = 0, 0, len(left), len(right), -1
    while (l < ln):
        if left[l] == right[r]:
            if r == 0:
                i = l
            if r == rn-1:
                return i
            l += 1
            r += 1
        else:
            r = 0
            i = -1
            l += 1
    return i

if __name__ == "__main__":
    # left = "sadbutsad"; right = "sad"
    left = "leetleeto"; right = "leeto"
    print(first_first_occurence_index(left, right)) 