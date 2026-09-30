"""

"""

from collections import Counter

def brute_force(arr: list[int]) -> int:
    """
        - Using hashmap as counter
        - Complexity Analysis:
            - Time -> O(n + d)
            - Space => O(d)
    """
    counter = Counter(arr)

    for k,v in counter.items():
        if v == 1:
            return k

def better_approach(arr: list[int]) -> int:
    """
        - Using hash set
        - Complexity Analysis:
            - Time -> O(n)
            - Space => O(d)
    """
    hash_set = set()

    for e in arr:
        if e not in hash_set:
            hash_set.add(e)
        else:
            hash_set.remove(e)

    return hash_set.pop()


def optimal_approach(arr: list[int]) -> int:
    """
        - Using XOR operator
        - Complexity Analysis:
            - Time -> O(n)
            - Space => O(1)
    """
    res = 0
    for e in arr:
        res ^= e

    return res

if __name__ == "__main__":
    arr = [2,2,1]
    print(brute_force(arr))
    print(better_approach(arr))
    print(optimal_approach(arr))


    
