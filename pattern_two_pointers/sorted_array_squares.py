

def sorted_array_squares1(arr: list[int]):
    """
        - LT Link -> https://leetcode.com/problems/squares-of-a-sorted-array/
        - Method: Naive Approach
        - We can iterate and sqaure each element in the array.
        - Finally sort the resultant array.
        -----------------------
        - Complexity Analysis:
        -----------------------
            - Time -> O(n + nlogn) ~= O(nlogn)
            - Space -> O(n) or O(1) depends upon sorting algo
    """
    for i in range(len(arr)):
        arr[i] = arr[i]**2
    arr.sort()
    return arr

def sorted_array_squares2(arr: list[int]):
    """
        - LT Link -> https://leetcode.com/problems/squares-of-a-sorted-array/
        - Method: Two Pointers Approach (Opposite direction poiners)
        - Initialize the left, right pointers and resultant array of size as input array size and filled with zeros.
        - Loop through until the left pointer croses the right pointer
            - Square each pointer values and compare.
            - If the left pointer value is greater than right one update the resultant array with sqaure of the value of left pointer and move left pointer and resultant array pointer one step forward.
            - Else update the resultant array with sqaure of the value of right pointer and move right pointer one step backward and resulant pointer one step forward.
        -----------------------
        - Complexity Analysis:
        -----------------------
        - Time -> O(n)
        - Space -> O(n) (for the resultant array)
    """
    n = len(arr)
    l, r = 0, n-1
    res, rp = [0]*n, n-1
    while (l <= r):
        ls = arr[l]**2
        rs = arr[r]**2
        if ls > rs:
            res[rp] = ls
            l += 1
        else:
            res[rp] = rs
            r -= 1
        rp -= 1
    return res


if __name__ == "__main__":
    arr = [-5,-2,4,5,6]
    # print(sorted_array_squares1(arr))
    print(sorted_array_squares2(arr))