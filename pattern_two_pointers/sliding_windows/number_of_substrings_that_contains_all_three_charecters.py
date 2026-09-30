def brute_force(s: str) -> int:
    n = len(s)
    # substrings = []
    substrings_count = 0
    for i in range(n):
        hash_arr = [0] * 3
        for j in range(i, n):
            hash_arr[ord(s[j]) - 97] = 1
            if sum(hash_arr) == 3:
                # substrings.append(substring)
                substrings_count += n - j
                break
    return substrings_count

def optimal_approach(s: str) -> int:
    n = len(s)
    count = 0
    hash_arr = [-1] * 3
    for i in range(n):
        hash_arr[ord(s[i]) - 97] = i
        min_value = min(hash_arr)
        if min_value != -1:
            count += min_value + 1
    return count


if __name__ == "__main__":
    s = "abcabc"
    # s = "aaacb"
    print(brute_force(s))
    print(optimal_approach(s))