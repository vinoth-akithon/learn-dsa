def valid_triangle_number(arr: list[int]):
    """
    - LC Link: https://leetcode.com/problems/valid-triangle-number/description/
    - Method -> Opposite Direction Two Pointers.
    - Same as `count of pair sum that greater than target(K)` and variation of 3Sum.
    - As per triangle inequivality theorem, any two side sum is always greater than third side.
    - Sort the given array.
    - For the triplet iterate the input until n-2.
        - Fix one largest element (right side) and apply pair calculation before that element.
        - Keep left pointer at start of the array and right pointer at the element before the fixed largest one.
        - Calculate the sum and compare it with the fixed one.
        - If the sum is greater than the fixed one, count the pairs by `right - left` and move the right pointer one step backward.
        - else move the left pointer one step forward.
    """
    arr.sort()
    c = 0
    n = len(arr)
    for k in range(n-1, 1, -1):
        l, r = 0, k-1
        K = arr[k]
        while (l < r):
            s = arr[l] + arr[r]
            if s > K:
                c += r - l
                r -= 1
            else:
                l += 1
    return c



if __name__ == "__main__":
    # arr = [2,2,3,4]
    arr = [4,2,3,4]
    print(valid_triangle_number(arr))