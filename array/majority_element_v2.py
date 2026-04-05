"""

"""


def naive_approach(arr: list[int]) -> int:
    """
        - Using Nested Loop and Linear Search
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    n = len(arr)
    freq = int(n/2) + 1

    for i in range(n):
        e = arr[i]
        count = 1
        for j in range(i, n):
            if arr[j] == e:
                count += 1

            if count >= freq:
                return e
    return -1


def better_approach1(arr: list[int]) -> int:
    """
        - Using Nested Loop and Linear Search with Set
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(n/2) -> Due to set
    """
    n = len(arr)
    freq = int(n/2) + 1
    seen = set()

    for i in range(n):
        e = arr[i]
        if e not in seen:
            count = 1
            for j in range(i, n):
                if arr[j] == e:
                    count += 1

                if count >= freq:
                    return e
            seen.add(e)
    return -1


def better_approach2(arr: list[int]) -> int:
    """
        - Using hash map
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n/2) -> Due to hashmap
    """
    n = len(arr)
    freq = int(n/2) + 1
    hashmap = {}

    for i in range(n):
        e = arr[i]
        ef = hashmap.get(e, 0)
        ef += 1

        if ef >= freq:
            return e
        
        hashmap[e] = ef

    return -1

def optimal_approach(arr: list[int]) -> int:
    """
        - Using math
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    me = arr[0]
    mef = 1

    for i in range(n):
        if arr[i] == me:
            mef += 1
        elif mef == 1:
            me = arr[i]
        else:
            mef -= 1

    return me




if __name__ == "__main__":
    arr = [7, 0, 0, 1, 7, 7, 2, 7, 7] 
    arr = [1, 1, 1, 2, 1, 2]
    print(naive_approach(arr))
    print(better_approach1(arr))
    print(better_approach2(arr))
    print(optimal_approach(arr))

