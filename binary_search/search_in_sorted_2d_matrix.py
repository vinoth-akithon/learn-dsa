"""
"""


def brute_force(mat: list[list[int]], t: int) -> bool:
    """
        - Check against all the elements by iterating rows and columns

        - Complexity Analysis:
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
        - Using Binary search on the right row

        - Complexity Analysis:
            - Time -> O(M * long(N))
            - Space -> O(1)
    """
    M = len(mat)
    N = len(mat[0])


    for r in range(M):
        if mat[r][0] <= t <= mat[r][N-1]:
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
        - Using Binary search on flatten 2D matrix (Imaginary 1D array)

        - Complexity Analysis:
            - Time -> O(log n)
            - Space -> O(1)
    """
    M = len(mat)
    N = len(mat[0])

    s = 0
    e = M*N -1

    while (s <= e):
        m = s + (e-s)//2

        r = m//N
        c = m%N
        if mat[r][c] == t:
            return True
        elif mat[r][c] < t:
            s = m+1
        else:
            e = m-1

    return False


def search_in_a_sorted_matrix(mat: list[list[int]], t: int) -> int:
    """
        - Exact match pattern
        - Think matrix like the flatten array

        - Complexity Analysis:
            - Time -> O(log n + log n) -> O(log n)
            - Space -> O(1)
    """
    if not mat and not mat[0]:
        return False

    r = len(mat)
    c = len(mat[0])

    sr = 0
    er = r-1

    while (sr < er):
        mr = sr + (er-sr)//2
        
        if mat[mr][0] == t:
            return True
        elif mat[mr][0] < t:
            if mat[mr][c-1] < t:
                sr = mr+1
            else:
                er = mr
        else:
            er = mr-1

    s = 0
    e = c-1

    while (s <= e):
        m = s + (e-s)//2

        if mat[sr][m] == t:
            return True
        elif mat[sr][m] < t:
            s = m + 1
        else:
            e = m-1

    return False




if __name__ == "__main__":
    mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]; t = 8
    mat = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ]; t = 78
    print(brute_force(mat, t))
    print(better_approach(mat, t))
    print(optimal_approach(mat, t))



"""

M x N -> 3 x 3 -> 9 elements total


[1,2,3,4,5,6,7,8,9]; t = 2
s = 0; e = 8
m = 4

row = m//N = 4//3 -> 1
col = m%N = 4%3 -> 1

so,s = 0 and e = 3

m = 2

row = 2//3 -> 0
col = 2%3 -> 2

so, s = 
"""