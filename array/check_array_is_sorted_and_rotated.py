"""

[3,4,5,1,2]


- Iterate the array and check the sorted, if it's failed at some point right rotate the array by (n-1-i)
- To do so, 
- Keep first array for holding values from arr[(n-1-i)+1:]
- And keep second array for holding values form arr[:(n-1-i)+1]
- Rearrange the original array by using first array and second array elements.
- Then iterate the elements and check sorted or not by comparing adjacent elements.
"""


def naive_approach(arr: list[int]) -> bool:
    """
        - Complexity Analysis:
            - Time -> O(n (first pass for rotation check) + n (second pass for creating auxiliary arrays) + n (for right rotate the original array) + n (for checking the sorted or not)) ~= O(n)
            - Space -> O(n) ~= Due to Auxiliary arrays
    """
    
    n = len(arr)
    if n < 2:
        return True
    
    first_arr = []
    second_arr = []
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            first_arr = arr[i+1:]
            second_arr = arr[:i+1]
            break

    if first_arr:
        for i in range(len(first_arr)):
            arr[i] = first_arr[i]

        for i in range(len(second_arr)):
            arr[len(first_arr) + i] = second_arr[i] 

        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return False
    
    return True


def better_approach(arr: list[int]) -> bool:
    """
        - Complexity Analysis:
            - Time -> O(n (first pass for rotation check) + n (second pass for creating auxiliary array) + n (for right rotate the original array) + n (for checking the sorted or not)) ~= O(n)
            - Space -> O(r) ~= No. of rotated elements
    """
    
    n = len(arr)
    if n < 2:
        return True
    
    first_arr = []
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            first_arr = arr[i+1:]
            break
    else:
        return True

    if first_arr:
        for j in range(i, -1, -1):
            arr[len(first_arr) + j] = arr[j]

        for i in range(len(first_arr)):
            arr[i] = first_arr[i]


        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return False
    
    return True

def arr_reverse(arr: list[int], s: int, e: int) -> None:
    while (s < e):
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1


def better_approach2(arr: list[int]) -> bool:
    """
        Complexity Analysis:
            - Time -> O(n (rotation checking) + n (reversing the array) + n (for reversing the rotated array) + n (sorting property check))
            - Space -> O(1)
    
    """
    n = len(arr)
    if n < 2:
        return True
    
    i = 0
    while (i < n-1):
        if arr[i] > arr[i+1]:
            break
        i +=1
    else:
        return True
    
    right_rotate = n-1-i
    arr_reverse(arr, 0, n-1)
    arr_reverse(arr, 0, right_rotate-1)
    arr_reverse(arr, right_rotate, n-1)

    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True
    

def optimal_approach(arr: list[int]) -> bool:
    """
        Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    cnt = 0

    for i in range(n):
        if arr[i] > arr[(i+1) % n]:
            cnt += 1

    return cnt <= 1



if __name__ == "__main__":
    arr = [3,4,5,1,2]
    arr = [2,1,3,4]
    # arr = [1,2,3]
    print(naive_approach(arr))
    print(better_approach(arr))
    print(better_approach2(arr))
    print(optimal_approach(arr))


# n - 1 - i = 5 - 1 - 2 = 2 

# 5-2 = 3
# 5-1 = 4
# 5-0 = 5

# 2 + 2 = 4
# 1 + 2 = 3
# 0 + 2 = 2