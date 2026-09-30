"""


"""


def brute_force(arr: list[int], k: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n * (Sum(arr)-Max(arr)))
            - Space -> O(1)
    """
    n = len(arr)
    min_arr = max(arr)
    if k == n:
        return min_arr
    max_arr = sum(arr)
    if k > n:
        return max_arr

    for p in range(min_arr, max_arr+1):
        cnt = 1
        pre_sum = 0
        for i in range(n):
            curr_sum = pre_sum + arr[i]
            if curr_sum > p:
                cnt += 1
                pre_sum = arr[i]
            else:
                pre_sum = curr_sum
        if cnt <= k:
            return p 


def optimal_approach(arr: list[int], k: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n * (Sum(arr)-Max(arr)))
            - Space -> O(1)
    """
    n = len(arr)
    min_arr = max(arr)
    if k == n:
        return min_arr
    max_arr = sum(arr)
    if k > n:
        return max_arr
    
    s = min_arr
    e = max_arr
    ans = 0
    while (s <= e):
        p = s + (e-s)//2

        cnt = 1
        pre_sum = 0
        for i in range(n):
            curr_sum = pre_sum + arr[i]
            if curr_sum > p:
                cnt += 1
                pre_sum = arr[i]
            else:
                pre_sum = curr_sum
        
        if cnt > k: # means p is lower value
            s = p +1
        else: # means p is high
            ans = p
            e = p-1

    return ans


if __name__ == "__main__":
    # arr = [1,2,3,4,5]; k = 3
    # arr = [3,5,1]; k = 3
    # arr = [7,2,5,10,8]; k = 2
    arr = [5,5,5,5];k = 3
    print(brute_force(arr, k))
    print(optimal_approach(arr, k))




"""
1. arr = [1,2,3,4,5]; k=3

largest subarray = Sum(arr)
minimum largest subarray = Max(arr)

if k == 1:
    ans = Sum(arr)
if k == n:
    ans = Max(arr)
if k > n:
    ans = -1


lar = 5
[1,2], [3], [4], [5]

lar = 6
[1,2,3], [4], [5]




2. arr = [3,5,1]; k = 3

lar = 5
[3], [5], [1] -> 5



arr = [7,2,5,10,8], k = 2

lar = 10
[7, 2], [5], [10], [8] 

lar = 11
[7, 2], [5], [10], [8]

lar = 12
[7, 2], [5], [10] [8]

lar = 13
[7, 2, 5] , [10], [8] 

lar = 14
[7, 2, 5] , [10], [8]

lar = 15
[7, 2, 5] , [10], [8] 

lar = 16
[7, 2, 5], [10], [8]

lar = 17
[7,2,5], [10], [8]

lar = 18
[7,2,5], [10, 8] -> 18



4. [1,2,3,4,5], k = 2

lar = 5
[1,2], [3] [4], [5]

lar = 6
[1,2,3], [4] ,[5]

lar = 7
[1,2,3], [4], [5]

lar = 8
[1,2,3], [4] , [5]

lar = 9
[1,2,3], [4,5] -> 9


arr = [5,5,5,5], k = 3

lar = 5
[5], [5], [5], [5]

lar = 10
[5, 5], [5, 5]

"""