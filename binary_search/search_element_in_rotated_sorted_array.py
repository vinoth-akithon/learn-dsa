"""
Given an rotated sorted array without duplicate elements. (Either half of the elements must be sorted)
"""


def brute_force(arr: list[int], k: int) -> int:
    """
        - Using Linear Search approach
        
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)

    for i in range(n):
        if arr[i] == k:
            return i
        
    return -1

def left_rotate(arr: list[int], p: int) -> list[int]:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """

    n = len(arr)
    left_arr = []
    right_arr = []

    for i in range(p):
        left_arr.append(arr[i%n])

    for i in range(p, n):
        right_arr.append(arr[i%n])

    # print(left_arr, right_arr)
    for i in range(n-p):
        arr[i] = right_arr[i]

    for j in range(p):
        arr[n-p+j] = left_arr[j]

    return arr

def undo_rotation_approach(arr: list[int], k : int) -> int:
    """
        - Using undoing left rotation and using a auxiliary DS for keeping index

        - Complexity Analysis:
            - Time -> O(n + log n) ~= O(n)
            - Space -> O(n)
    """
    """
        - Complexity Analysis:
            - Time -> O(n + n + (n + n) + log n) ~= O(n)
            - Space -> O(n + n) ~= O(n)
    """
    # Phase 1: Finding the breaking place
    n = len(arr)
    auxiliary_arr = [(val, idx) for idx, val in enumerate(arr)]
    i = 0
    while (i < n-1):
        if arr[i+1] < arr[i]:
            break
        i += 1
    
    p = i+1


    # Phase2: Undo the rotation to make complete sorted array
    left_rotate(auxiliary_arr, p) # Array becomes sorted array (but not rotated)


    # Phase3: Apply binary search to find the target
    s = 0
    e = n-1
    
    while (s <= e):
        m = s + (e-s)//2

        if auxiliary_arr[m][0] == t:
            return auxiliary_arr[m][1]
        elif auxiliary_arr[m][0] < t:
            s = m + 1
        else:
            e = m-1

    return -1

def optimal_approach(arr: list[int], t: int) -> int:
    """
        - Using binary search on the sorted portion (As we know, in the rotated sorted array, whole array is not sorted.)
        - If the array doesn't contain duplicate, either half of the array must be sorted

        Algorithm:
            - Rotated Array Property: In a sorted rotated array (without any duplicates), either half of the array is sorted arr[s...m] or arr[m...e] (inclusive m)
            - find the mid element and check against the target, if matched return it's index
            - check the left half is sorted
                - Check the target lies in the left half
                    - If so, shrink the array to left half
                    - else, shrink the array to right half
            - check the right half is sorted
                - check the target lies in the right half
                    - If so, shrink the array to right half
                    - else, shrink the array to left half

        - Complexity Analysis:
            - Time -> O(log n)
            - Space -> O(1)    
    """
    n = len(arr)
    s = 0
    e = n-1

    while (s<=e):
        m = s + (e-s)//2

        if arr[m] == t:
            return m

        elif arr[s] <= arr[m]:
            if arr[s] <= t < arr[m]:
                e = m-1
            else:
                s = m+1
        else:
            if arr[m] < t <= arr[e]:
                s = m+1
            else:
                e = m-1
    return -1



if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2]; k = 0
    # arr = [4, 5, 6, 7, 0, 1, 2]; k = 3
    # print(brute_force(arr, k))
    # print(undo_rotation_approach(arr, k))
    print(optimal_approach(arr, k))



    """
    [
        (4, 0),
        (5, 1),
        (6, 2),
        (7, 3),
        (0, 4),
        (1, 5),
        (2, 6)
    
    ]


    0 + (6-0)//2 -> 3
    mid = 7
    left arr = [4, 5, 6]
    right_arr = [0, 1, 2]

    sorted_arr = left_arr
    if arr[s] <= k <= arr[m-1]:
        new arr = left arr
    else:
        new arr = right arr

    left sorted
        - left (if arr[s] <= k <= arr[m-1])
        - right (if not arr[s] <=k <= arr[m-1])
    right sorted
        - left (if not arr[m+1] <= k <= arr[e])
        - right (if arr[m+1] <= k <= arr[e])

    """