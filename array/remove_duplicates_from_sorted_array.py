from collections import defaultdict

def remove_duplicates1(arr: list[int]) -> int:
    """
        - Using hash map
        - Time -> O(n)
        - Space -> O(k)
    """
    n = len(arr)
    hash_table = defaultdict(int)
    for i in range(n):
        hash_table[arr[i]] += 1
    
    for idx, key in enumerate(hash_table):
        arr[idx] = key
    return len(hash_table)


def remove_duplicates(arr: list[int]) -> int:
    """
        Using Two poiners
        Time -> O(n)
        Space -> O(1)
    """
    n = len(arr)
    i = 0; j = 1
    while (j < n):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
        j += 1
    return i + 1


if __name__ == "__main__":
    # arr = [1,1,2]
    arr = [0,0,1,1,1,2,2,3,3,4]
    print(remove_duplicates1(arr))
    print(arr)