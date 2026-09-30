"""
Given an array of integers, returns the count of reverse pairs.

Reverse pair: i < j and arr[i] > 2 arr[j]

"""


def brute_force(arr: list[int]) -> int:
    """
        - Using Nested loop approach

        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    n = len(arr)
    cnt = 0

    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] > 2 * arr[j]:
                cnt += 1
    
    return cnt

def merge_v2(arr: list[int], s: int, e: int) -> list[int]:
    """

    """
    m = (e-s)//2 + s
    temp = []

    cnt = 0
    r = m+1
    for i in range(s, m+1):
        while r <= e and arr[i] > 2*arr[r]:
            r += 1
        cnt += r - (m+1)
    
    l = s
    r = m+1
    while (l <= m and r <= e):
        if arr[l] <= arr[r]:
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[r])
            r  += 1

    while (l <= m):
        temp.append(arr[l])
        l += 1

    while (r <= e):
        temp.append(arr[r])
        r  += 1

    for i in range(len(temp)):
        arr[s] = temp[i]
        s += 1

    return cnt

def optimal_approach(arr: list[int], s: int, e: int):
    """
        - Using Merge sort algo.

        - Complexity Analysis:
            - Time -> O(2 * n log n) -> O(n) for merging + O(n) for counting so O(2n log n)
            - Space -> O(n) -> temp array used in merging
    
    """
    cnt = 0
    # Base Condition
    if s >= e:
        return cnt
    
    m = (e-s)//2 + s
    
    cnt += optimal_approach(arr, s, m)
    cnt += optimal_approach(arr, m+1, e)

    cnt += merge_v2(arr, s, e)
    return cnt


if __name__ == "__main__":
    # arr = [1,3,2,3,1]
    # arr = [3,2,1,4]
    # arr = [2,4,3,5,1] # [2, 3], [3, 1], [5, 1]
    arr = [5,4,3,2,1] # [5, 2] , [5, 1], [4,1], [3, 1]
    # print(brute_force(arr))

    print(optimal_approach(arr, 0, len(arr)-1))