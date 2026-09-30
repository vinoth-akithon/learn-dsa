"""
Given a binary matrix (having elements either 0 or 1) of size M x N. Find out a row having more number of ones than other rows.

If more than one rows having the same number of ones return the first matched row.

If no rows having at least one 1s, return -1
"""


def brute_force(mat: list[list[int]]) -> int:
    """
        - Complexity Analysis:
            - Time -> O(M * N)
            - Space -> O(1)
    """
    M = len(mat)
    N = len(mat[0])
    max_ones_idx = -1
    max_ones = 0

    for r in range(M):
        for c in range(N):
            if mat[r][c] == 1:
                curr_row_ones = N-c
                if curr_row_ones > max_ones:
                    max_ones = curr_row_ones
                    max_ones_idx = r
                break
    return max_ones_idx




def optimal_approach(mat: list[list[int]]) -> int:
    """
        - Optimizing using Boundary value pattern (First True)
        - Complexity Analysis:
            - Time - O(M * log N)
            - Space -> O(1)
    """
    M = len(arr)
    N = len(arr[0])
    max_ones_idx = -1
    max_ones = 0

    for r in range(M):
        s = 0
        e = N-1
        one_start_idx = N
        while (s <= e):
            m = s + (e-s)//2
            
            if arr[r][m] == 1:
                one_start_idx = m
                e = m - 1
            else:
                s = m + 1

        curr_row_ones = N - one_start_idx
        if curr_row_ones > max_ones:
            max_ones = curr_row_ones
            max_ones_idx = r

    return max_ones_idx



if __name__ == "__main__":
    arr = [
        [1,1,1],
        [0,0,1],
        [0,0,0]
    ]

    arr = [
        [0, 0],
        [0, 0]
    ]
    print(brute_force(arr))
    print(optimal_approach(arr))


