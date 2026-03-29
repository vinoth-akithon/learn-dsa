"""


"""

def naive_approach(arr: list[int]) -> None:
    """
        - Complexity Analysis:
            - Time -> O(n^2)
    """
    n = len(arr)
    visited = [False] * n
    
    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        count = 1
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                visited[j] = True
                count += 1
        print(f"{arr[i]} -> {count}")


def optimal_approach(arr: list[int]) -> dict[int, int]:
    """
    Complexity Analysis:
        - Time -> O(n)
        - Space -> O(U) -> No. of unique elements
    """
    hashmap = {}
    for e in arr:
        if e in hashmap:
            hashmap[e] += 1
        else:
            hashmap[e] = 1
    
    for k, v in hashmap.items():
        print(f"{k} -> {v}")


if __name__ == "__main__":
    arr = [10,20,10,30,20,10]
    naive_approach(arr)
    print()
    optimal_approach(arr)