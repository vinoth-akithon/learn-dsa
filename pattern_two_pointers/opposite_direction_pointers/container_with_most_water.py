"""
    - Problem Link: https://leetcode.com/problems/container-with-most-water/description/
    - Intuition:
        - Using Opposite two pointers.
        - Keep a variable for tracking the max_area we computed so far. Initially 0.
        - Find the dominating height (small height which affect the container)
        - Compute the area by multipling the dominating height and width (distance bw two pointers)
        - Finally move a pointer in greedy way (move the dominating height pointer inward)
    - Complexity Analysis:
        - Time -> O(n)
        - Space -> O(1)

"""


def container_with_most_water(arr: list[int]) -> int:
    n = len(arr)
    l, r = 0, n-1
    max_area = 0

    while (l < r):
        h = l if arr[l] < arr[r] else r

        area = arr[h] * (r-l)
        max_area = max([max_area, area])

        if h == l:
            l += 1
        else:
            r -= 1
    return max_area


if __name__ == "__main__":
    arr = [1,8,6,2,5,4,8,3,7]
    # arr = [1,1]
    print(container_with_most_water(arr))