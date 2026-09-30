"""

"""


def brute_force(arr: list[int], k: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    pre = 0
    pre_diff = 0
    for i in range(n):
        curr = arr[i]
        curr_diff = pre_diff + (curr - pre -1)

        if k <= curr_diff:
            break
        else:
            pre = curr
            pre_diff = curr_diff

    return k - pre_diff + pre



def optimal_approach(arr: list[int], k: int) -> int:
    """
    Complexity Analysis:
        - Time -> O(log n)
        - Space -> O(1)
    """

    n = len(arr)
    
    s = 0
    e = n-1

    while (s <= e):
        m = s + (e-s)//2
        missing = arr[m] - (m+1)
        if missing < k:
            # right half
            s = m+1
        else:
            # Left half
            e = m-1

    return k + e + 1 # equivalent to k + s

if __name__ == "__main__":
    arr = [4,7,9,10]; k = 6
    # arr = {4,7,9,10}; k = 4

    print(brute_force(arr, k))
    print(optimal_approach(arr, k))



# pre = 4
# curr = 7
# pre_diff = 3
# curr_diff = 2
# k = 4

# k - pre_diff + pre
# 4 - 3 = 1 + 4 = 5


# 5 - 3 = 2 + 4 => 6

[1,2,3,5,6,8,11]
"""
Dry run:

arr = [4,7,9,10]; k = 2

pre = 0
diff = curr - pre
diff  = 4 - 0 -> 4 -> [1, 2, 3]


k < diff -> 2 <= 4 
    diff - k = 4 - 2 = 2


arr = [4,7,9,10]; k = 4
pre = 1
diff = 4 - 1 => 4 

k < diff -> 4 <= 3 (fails) [1,2,3]
    prev_diff = 3

pre = 4+1
curr = 7
diff = 7 - 4 -> 2 -> [5, 6]

k < diff -> 4 < (3 + 2)

pre 





"""