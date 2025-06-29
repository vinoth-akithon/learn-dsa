import string
def first_unique_char_in_str(s: int):
    buckets = [
        *[[c, 0, -1] for c in string.ascii_lowercase]
    ]

    for i, c in enumerate(s):
        ordinal_value = ord(c)
        bucket = ordinal_value - 97
        buckets[bucket][1] += 1
        if buckets[bucket][2] == -1:
           buckets[bucket][2] = i 

    for c in s:
        ordinal_value = ord(c)
        bucket = ordinal_value - 97
        if buckets[bucket][1] == 1:
            return buckets[bucket][2]
    return -1

if __name__ == "__main__":
    s = "aabb"
    # s = "loveleetcode"
    # s = "leetcode"
    print(first_unique_char_in_str(s))