"""
- All the number are appeared twice except 2 numbers

- XOR Properties
    - The two numbers have different bits at this position.
    - There is at least one bit where our two unique numbers differ.


- x & -x gives right most set bit
    - -x is the 2's complement of x
        2's complement is 1's compliment + adding of 1 to it

"""

from collections import Counter

def brute_force(arr: list[int]) -> list[int]:
    """
        - Using auxiliary data structure (Hashmap)
        - Complexity Analysis:
            - Time -> O(n + d) ~= O(n)
            - Space -> O(d)
    """
    hash_map = Counter(arr)

    res = []
    for k, v in hash_map.items():
        if v == 1:
            res.append(k)

    res.sort()
    return res


def better_approach(arr: list[int]) -> list[int]:
    """
        - Applying sorting
        - Complexity Analysis:
            - Time -> O(n log n + n) ~= O(n log n)
            - Space -> O(1)
    """
    arr.sort()

    n = len(arr)
    i = 0
    res = []
    while (len(res) != 2 and i < n-1):
        if arr[i] == arr[i+1]:
            i += 2
        else:
            res.append(arr[i])
            i += 1

    if len(res) == 1:
        res.append(arr[-1])

    res.sort()
    return res


def optimal_approach(arr: list[int]) -> list[int]:
    """
        - Iterate the array and get the xor of all the elements
        - find the right most set bit
        - Iterate the array and group element based on right most set bit
            - xor each group which adding element to the group
        - Finally each group as one element, that's the ans

        - Complexity Analysis:
            - Time -> O(n + n) ~= O(n)
            - Space -> O(1)
    """
    xor_all = 0
    for e in arr:
        xor_all ^= e

    right_set_bit = xor_all & -xor_all

    group1 = 0
    group2 = 0
    for e in arr:
        if e & right_set_bit:
            group1 ^= e
        else:
            group2 ^= e

    return [group1, group2] if group1 < group2 else [group2, group1]

if __name__ == "__main__":
    # arr = [1,2,1,3,5,2]
    arr = [-1, 0]
    print(brute_force(arr))
    print(better_approach(arr))
    print(optimal_approach(arr))

