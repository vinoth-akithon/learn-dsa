"""

"""


def brute_force(arr: list[int], k: int) -> int:
    """
        Complexity Analysis:
            - Time -> O(n * (Sum(arr)-Max(arr))
            - Space -> O(1)
    """
    n = len(arr)
    min_h = max(arr)
    if k == n:
        return min_h
    max_h = sum(arr)
    if k == 1:
        return max_h

    for b in range(min_h, max_h):
        cnt = 1
        pre_h = 0
        for i in range(n):
            new_h = pre_h + arr[i]
            if new_h > b:
                cnt += 1
                pre_h = arr[i]
            else:
                pre_h += arr[i]

        if cnt <= k:
            return b
        

def optimal_approach(arr: list[int], k: int) -> int:
    """
        Complexity Analysis:
            - Time -> O(n * log(Sum(arr)-Max(arr))
            - Space -> O(1)
    """
    n = len(arr)
    min_h = max(arr)
    if k == n:
        return min_h
    max_h = sum(arr)
    if k == 1:
        return max_h
    
    s = min_h
    e = max_h
    ans = 0

    while (s <= e):
        b = s + (e-s)//2

        cnt = 1
        pre_h = 0
        for i in range(n):
            new_h = pre_h + arr[i]
            if new_h > b:
                cnt += 1
                pre_h = arr[i]
            else:
                pre_h += arr[i]

        if cnt <= k:
            ans = b
            e = b-1
        else:
            s = b + 1

    return ans
        

if __name__ == "__main__":
    # arr = [5,5,5,5]; k = 2
    arr = [10, 20, 30, 40]; k = 2
    
    print(brute_force(arr, k))
    print(optimal_approach(arr, k))
