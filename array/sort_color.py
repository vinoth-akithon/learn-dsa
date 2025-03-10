"""
    Sort Colors (Dutch National Flag)
    Link: https://leetcode.com/problems/sort-colors/description/
"""


def sort_color(arr: list[int]) -> None:
    """
        - Also Called 
    """
    n = len(arr)
    l = 0
    r = n-1
    i = 0
    while (i <= r):
        if arr[i] == 0:
            arr[i], arr[l] = arr[l], arr[i]
            l += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[r] = arr[r], arr[i]
            r -= 1
    



if __name__ == "__main__":
    arr = [0, 0, 2, 1, 0]
    sort_color(arr)
    print(arr)