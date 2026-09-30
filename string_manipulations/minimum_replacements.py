"""
Given string `s` and periodic length `k`, we have to calculate the minimum replacement required to
obtain a resultant string which is palindrome and k periodic strings.

ex:
    - aab bcb bcb -> bcb bcb bcb -> so the total replacement would be 2.
    - ab aa ba -> aa aa aa -> so the total replacement would be 2.


- Idea:
    - k periodic strings made only by concatenating several palindromic string having length k.
    - all the characters at the position i, k-i-1, i+k, 2k-i-1, 1+2k, 3k-i-1 should be same.
"""

from collections import defaultdict


def optimal_approach(s: int, k: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(26) ~= O(1)
    """
    n = len(s)
    total_replacements = 0

    for i in range((k+1)//2):
        hash_map = defaultdict(int)

        for j in range(i, n, k):
            hash_map[s[j]] += 1

        # handling edge case 
        if i%2 != 0 and i == k//2:
            pass
        else:
            for j in range(n-1, -1, -k):
                hash_map[s[j]] += 1

        curr_max = max(hash_map.values())
        visited = (n//k) * 2 if i%2==0 else n//k
        total_replacements += (visited - curr_max)

    return total_replacements


if __name__ == "__main__":
    # s =  "abaaba"; k = 2
    s = "aabbcbbcb"; k = 3
    print(optimal_approach(s, k))