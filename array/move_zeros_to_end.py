"""
Moves Zeros to the end of the array
"""


def naive_approach(arr: list[int]) -> list[int]:
    """
        - keep a temp array for holding all the non-zero elements.
        - Then iterate the temp array and fill into the original array
        
        - Complexity Analysis:
            - Time -> O(2n) ~= O(n)
            - Space -> O(n) - due to the temp array
    """
    n = len(arr)
    temp = []
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])
    
    for i in range(len(temp)):
        arr[i] = temp[i]
    
    for i in range(len(temp), n):
        arr[i] = 0

    return arr


def better_approach(arr: list[int]) -> list[int]:
    """
        - Using Two pointer (one pointer at the left and another pointer at right)
        - Whenever the left pointer points to zero, swap all the elements one step backward from left+1 to right.
        - if left pointer point to non-zero element, move left pointer one step forward.
        - If the right pointer already points to 0, then move the right pointer one step backward.
        - Do this process until left meets right.

        - Complexity Analysis:
            - Time -> O(n^2) -> due to swapping the entire array at some cases
            - Space -> O(n)
    """

    n = len(arr)
    l = 0
    r = n-1

    while (l < r):
        if arr[r] == 0:
            r -= 1
        elif arr[l] != 0:
            l +=1
        else:
            for i in range(l+1, r+1):
                arr[i-1] = arr[i]
            arr[r] = 0
            r -= 1
    return arr


def optimal_approach(arr: list[int]) -> list[int]:
    """
        - Using two pointers approach (like remove duplicates)
        - Keep a left pointer at first zero element.
        - iteration the array from next to the first zero element (right pointer) till the end.
        - If we find non zero element, swap elements pointing the pointers.
        - Then move the left pointer one step forward (as the right pointer increment automatically by the iterator)

        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    s = -1
    for i in range(n):
        if arr[i] == 0:
            s = i
            break
    else:
        return arr
    
    for i in range(s+1, n):
        if arr[i] != 0:
            arr[s], arr[i] = arr[i], arr[s]
            s += 1

    return arr

if __name__ == "__main__":
    arr = [0,0,1, 0]
    # arr = [0,0,0]
    # arr = [1,2,2]
    # print(naive_approach(arr))
    # print(better_approach(arr))
    print(optimal_approach(arr))
