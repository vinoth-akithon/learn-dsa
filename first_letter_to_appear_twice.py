def first_letter_to_appear_twice(s: str) -> str:
    hash_set = set()
    for c in s:
        if c in hash_set:
            return c
        else:
            hash_set.add(c)

def first_letter_to_appear_twice2(s: str) -> str:
    count = [0] * 26
    for c in s:
        ordinal_value = ord(c)
        pos = ordinal_value - 97
        if count[pos]:
            return c
        else:
            count[pos] += 1

if __name__ == "__main__":
    s = "abccbaacz"
    s = "abcdd"
    # print(first_letter_to_appear_twice(s))
    print(first_letter_to_appear_twice2(s))