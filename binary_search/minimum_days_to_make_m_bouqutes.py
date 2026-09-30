"""

"""

def brute_force(arr: list[int], m: int, k: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n * (Max(arr) - Min(arr)))
            - Space -> O(1)
    """
    n = len(arr)

    # we need m*k flowers to make m bouquets
    if n < (m * k):
        return -1

    max_day = max(arr)
    min_day = min(arr)

    for day in range(min_day, max_day+1):
        bouquets = 0
        bloom = 0
        for i in range(n):
            if arr[i] <= day:
                bloom += 1
                if bloom == k:
                    bouquets += 1
                    bloom = 0
            else:
                bloom = 0
    
    if bouquets >= m:
        return day
    else:
        return -1


def optimal_approach(arr: list[int], m: int, k: int) -> int:
    """
    - Using Binary Search
    - Complexity Analysis:
        - Time -> O(log n * (Max(arr) - Min(arr)))
        - Space -> O(1)
    """
    n = len(arr)

    # we need m*k flowers to make m bouquets
    if n < (m * k):
        return -1
    
    s = min(arr)
    e = max(arr)
    ans = -1

    while (s <= e):
        day = s + (e-s)//2
        bouquets = 0
        blooms = 0

        for i in range(n):
            if arr[i] <= day:
                blooms += 1
                if blooms == k:
                    bouquets += 1
                    blooms = 0
            else:
                blooms = 0
        
        if bouquets < m:
            s = day + 1
        else:
            ans = day
            e = day -1

    return ans

if __name__ == "__main__":
    # arr = [7, 7, 7, 7, 13, 11, 12, 7]; m = 2; k = 3
    # arr = [1, 10, 3, 10, 2]; m = 3; k = 2
    # arr = [1,10,3,10,2]; m = 3; k = 1
    arr = [1000000000, 1000000000]; m = 1; k=1
    # arr = [7,7,7,7,12,7,7]; m=2; k= 3
    print(brute_force(arr, m, k))
    print(optimal_approach(arr, m, k))



[7,8,9,10,11,12]
