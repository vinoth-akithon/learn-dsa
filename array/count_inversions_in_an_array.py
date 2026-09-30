"""

Inversion pair means (arr[j] < arr[i] for i & j < n and i < j)

Recalling Combination problem:
    total combinations  nCr = n!/r!(n-r)!

    ex: n = 5, r = 2
    5! / (2! * (5-2)!) => 120/(2 * 6) => 10

"""


def brute_force(arr: list[int]) -> int: 
    """
        - Using nested loop approach to find all the possible pair and check inversion required or not

        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    n = len(arr)
    cnt = 0

    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                cnt += 1

    return cnt


def merge(left: list[int], right: list[int], cnt: int) -> list[int]:
    """

    """
    l = r = 0
    m = len(left)
    n = len(right)
    res = []
    
    while (l < m and r < n):
        if left[l] <= right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r  += 1
            cnt += m - l

    while (l < m):
        res.append(left[l])
        l += 1

    while (r < n):
        res.append(right[r])
        r  += 1

    return (res, cnt)


def merge_sort(arr: list[int]) -> list[int]:
    """
    
    """
    global cnt

    n = len(arr)
    # Base Condition
    if n <= 1:
        return (arr, 0)
    
    mid = n//2

    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    left_sorted_arr, left_cnt = merge_sort(left_arr)
    right_sorted_arr, right_cnt = merge_sort(right_arr)


    return merge(left_sorted_arr, right_sorted_arr, left_cnt+right_cnt)


def merge_v2(arr: list[int], s: int, e: int, cnt: int) -> list[int]:
    """

    """
    l = s
    m = (e-s)//2 + s
    r = m+1
    temp = []
    
    while (l <= m and r <= e):
        if arr[l] <= arr[r]:
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[r])
            r  += 1
            cnt += m - l + 1

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


def optimal_approach(arr: list[int], s: int, e: int, cnt: int) -> list[int]:
    """
       - Using merge sort algo. 
       - During the merging, count the the inversion bulkily if arr[l] > arr[r], so length of the left array taken into account of inversions.

       - Complexity Analysis:
            - Time -> O(n log n)
            - Space -> O(n) -> Temp array using while merging
    """
    # Base Condition
    if s >= e:
        return 0
    
    m = (e-s)//2 + s
    
    cnt1 = optimal_approach(arr, s, m, cnt)
    cnt2 = optimal_approach(arr, m+1, e, cnt)

    return merge_v2(arr, s, e, cnt1+cnt2)
    



if __name__ == "__main__":
    # arr = [3,2,1]
    arr = [1,2,3,4,5]
    arr = [5,3,2,1,4]
    arr = [10, 10, 10]
    # arr = [2 ,3 ,4 ,5, 6]
    # print(brute_force(arr))
    print(optimal_approach(arr, 0, len(arr)-1, 0))
    # merge_v2(arr, 0, len(arr)-1)
    print(arr)


    """
    [5,4,3,2,1]

        [5,4,3] -> 3 + 3 [2, 1]

            [5, 4] [3]  -> 2   [2] [1] -> 1

                [5] [4] -> 1


    [5,3,2,1,4] 
        [5, 3] 2 + 2 + 1    [2, 1, 4]
            [5] [3] -> 1    [2, 1] [4] -> 0
                                [2] [1] -> 1
                

    """