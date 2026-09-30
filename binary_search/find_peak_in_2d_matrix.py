"""
Given an 2d matrix where we have to find the peak element

Peak element is the one whose adjacent (top, bottom, left, right) should be small. 

No adjacent elements are equal.

Return the indexes as array [i, j]
"""


def is_peak(mat: list[list[int]], r: int, c: int, t: int) -> bool:
    try:
        return mat[r][c] < t
    except IndexError:
        return True


def get_value(mat: list[list[int]], r: int, c: int) -> bool:
    M = len(mat)
    N = len(mat[0])

    if r < 0 or c < 0 or r > M-1 or c > N-1:
        return -1
    return mat[r][c]
                


def brute_force(mat: list[list[int]]) -> list[int]:
    """
        - Complexity Analysis:
            - Time -> O(M * N)
            - Space -> O(1)
    """
    M = len(mat)
    N = len(mat[0])

    for r in range(M):
        for c in range(N):
            if is_peak(mat, r-1, c, mat[r][c]) and is_peak(mat, r+1, c, mat[r][c]) and is_peak(mat, r, c-1, mat[r][c]) and is_peak(mat, r, c+1, mat[r][c]):
                return [r,c]
    return [-1,-1]


def better_approach(mat: list[list[int]]) -> list[int]:
    """
        - Complexity Analysis:
            - Time -> O(M * N)
            - Space -> O(1)
    """
    M = len(mat)
    N = len(mat[0])

    for r in range(M):
        for c in range(N):
            if get_value(mat, r-1, c) < mat[r][c] and get_value(mat, r+1, c) < mat[r][c] and get_value(mat, r, c-1) < mat[r][c]  and get_value(mat, r, c+1) < mat[r][c]:
                return [r,c]
    return [-1,-1]



def optimal_approach(mat: list[list[int]]) -> int:
    """
        - Complexity Analysis:
            - Time -> O(M * log N)
            - Space -> O(1)
    """
    M = len(mat)
    N = len(mat[0])

    s = 0
    e = N-1

    while (s <= e):
        m = s + (e-s)//2
        max_value = 0
        max_value_idx = mat[0][m]

        for i in range(M):
            if mat[i][m] > max_value:
                max_value = mat[i][m]
                max_value_idx = i

        left = (m == 0 or mat[max_value_idx][m-1] < mat[max_value_idx][m])
        right  = (m == N-1 or mat[max_value_idx][m+1] < mat[max_value_idx][m]) 
        
        if left and right:
            return [max_value_idx, m]
        
        elif left and not right:
            s = m + 1
        else:
            e = m - 1

    return [-1, -1]

if __name__ == "__main__":
    # mat = [[10,20,15],[21,30,14],[7,16,32]]
    # mat = [[5, 10, 8], [4, 25, 7], [3, 9, 6]]
    mat = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]
    # mat = [[1,4],[3,2]]
    print(brute_force(mat))
    print(better_approach(mat))
    print(optimal_approach(mat))