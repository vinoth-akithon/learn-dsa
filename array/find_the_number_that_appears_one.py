"""
"""


def naive_approach(arr: list[int]) -> int:
    """
        Using linear search nested loop approach
        Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    n = len(arr)
    for i in range(n):
        num = arr[i]
        for j in range(n):
            if j != i and arr[j] == num:
                break
        else:
            return num
        

def better_approach(arr: list[int]) -> int:
    """
        Using hash map as auxiliary data structure
        Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """

    n = len(arr)
    hash_map = {}

    for i in range(n):
        v = hash_map.get(arr[i], 0) + 1
        hash_map[arr[i]] = v
    
    for k, v in hash_map.items():
        if v == 1:
            return k


def optimal_approach(arr: list[int]) -> int:
    """
        - Using XOR operator. 
            X ^ X -> 0
            X ^ 0 -> X
        Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)

    result = arr[0]
    for i in range(1, n):
        result ^= arr[i] 
    
    return result



if __name__ == "__main__":
    arr = [1,1,2,2, 3]
    print(naive_approach(arr))
    print(better_approach(arr))
    print(optimal_approach(arr))