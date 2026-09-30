"""
Given a matrix where elements of each row and col are sorted in ascending order. 

But first element of the row doesn't always need to greater than last element of the previous row (if any)


[1   4   7   11
2   5   8   12
3   6   9   16
10 13  14  17]
"""


def brute_force(mat: list[list[int]], t: int) -> bool:
    """
        Complexity Analysis:
            - Time -> O(M * N)
            - Space -> O(1)
    """
    M = len(mat)
    N = len(mat[0])

    for r in range(M):
        for c in range(N):
            if mat[r][c] == t:
                return True
    
    return False


def better_approach(mat: list[list[int]], t: int) -> bool:
    """
        - Applying binary search on each row for finding the target

        - Complexity Analysis:
            - Time -> O(M log N)
            - Space -> O(1)    
    """
    M = len(mat)
    N = len(mat[0])

    for r in range(M):
        s = 0
        e = N-1

        while (s <= e):
            m = s + (e-s)//2

            if mat[r][m] == t:
                return True
            elif mat[r][m] < t:
                s = m+1
            else:
                e = m-1
            
    return False


def optimal_approach(mat: list[list[int]], t: int) -> bool:
    """
        Complexity Analysis:
            - Time -> O(M+N)
            - Space -> O(1)
    """
    M = len(mat)
    N = len(mat[0])

    row = 0
    col = N-1

    while (row < M and col >= 0):
        if mat[row][col] == t:
            return True
        elif mat[row][col] < t:
            row += 1
        else:
            col -=1

    return False


if __name__ == "__main__":
    # mat = [[1 ,  4 ,  7 ,  11], [2 ,  5 ,  8,   12], [3 ,  6 ,  9,   16], [10, 13 , 14,  17]]; t = 9
    # mat = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]; t = 5
    mat = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]; t = 20
    print(brute_force(mat, t))
    print(better_approach(mat, t))
    print(optimal_approach(mat, t))


