"""
- Given a array of size n where all the elements inside between 1 to n (i.e -> n = 5 , [1,2,3,4,5])
- But only one element is duplicate (that is the repeating element) and position should hold the value is the missing elements.
- We should return the array of size 2 like [repeating elem, missing elem]
"""


def brute_force(arr: list[int]) -> list[int]:
    """
        - Using Nested loop approach.

        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    n = len(arr)
    dup = None
    miss = None

    for i in range(1, n+1):
        cnt = 0
        for j in range(n):
            if arr[j] == i:
                cnt += 1
        if cnt == 2:
            dup = i
        elif cnt == 0:
            miss = i
    
    return [dup, miss]


def better_approach(arr: list[int]) -> list[int]:
    """
        - Using Auxiliary Hash map.

        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n-1)
    """
    n = len(arr)
    hash_map = {}

    for i in range(n):
        hash_map[arr[i]] = hash_map.get(arr[i], 0) + 1

    # print(hash_map)
    dup = None
    miss = None
    for i in range(1, n+1):
        val = hash_map.get(i, 0)
        if val == 0:
            miss = i
        elif val == 2:
            dup = i

    return [dup, miss]

def better_approach2(arr: list[int]) -> list[int]:
    """
        - Using cycle sort algorithm.
        - First we should sort the array using cycle sort.
        - Then we iterate the array for find the repeated and missing.

        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n) -> Due to auxiliary array
    """
    n = len(arr)
    temp_arr = arr.copy()

    i = 0
    while (i < n):
        if temp_arr[i] == i+1 or temp_arr[temp_arr[i]-1] == temp_arr[i]:
            i += 1
        else:
            temp_arr[temp_arr[i]-1], temp_arr[i] = temp_arr[i], temp_arr[temp_arr[i]-1]

    for j in range(n):
        if j+1 != temp_arr[j]:
            return [temp_arr[j], j+1]

if __name__ == "__main__":
    arr = [3, 5, 4, 3, 1]
    # print(brute_force(arr))
    print(better_approach(arr))
    print(better_approach2(arr))
