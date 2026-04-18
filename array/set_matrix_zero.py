"""
Set Matrix cell to Zero if either of it's row or column contains zero.

"""

def naive_approach(arr: list[list[int]]) -> list[list[int]]:
    """
        - Using nested loop and linear search approach.
        - Iterate the matrix and check if any of the cell is zero.
        - If so, mark it's entire row and column to -1.
        - After process the entire matrix, iterate the matrix to replace -1 to 0.

        - Complexity Analysis:
            - Time -> O(m * n * (m + n))
            - Space -> O(1)    
    """
    m = len(arr)
    n = len(arr[0])

    for r in range(m):
        for c in range(n):
            if arr[r][c] == 0:
                for i in range(n):
                    if arr[r][i] != 0:
                        arr[r][i] = "x"
                for j in range(m):
                    if arr[j][c] != 0:
                        arr[j][c] = "x"

    for r in range(m):
        for c in range(n):
            if arr[r][c] == "x":
                arr[r][c] = 0
    return arr

def better_approach(arr: list[list[int]]) -> list[list[int]]:
    """
        - Using nested loop and linear search approach.
        - Also using Auxiliary set DS for storing row and cols.
        - Iterate the matrix and check if any of the cell is zero.
        - If so, add that col/row into the right set.
        - After processing the entire matrix, iterate the matrix to update cell to 0 if that row/col present in the set.

        - Complexity Analysis:
            - Time -> O(m * n)
            - Space -> O(m + n)    
    """
    m = len(arr)
    n = len(arr[0])
    zr = set()
    zc = set()

    for r in range(m):
        for c in range(n):
            if arr[r][c] == 0:
                zr.add(r)
                zc.add(c)

    # for r in range(m):
    #     if r in zr:
    #         for i in range(n):
    #             arr[r][i] = 0
    #     else:
    #         for c in range(n):
    #             if c in zc:
    #                 for j in range(m):
    #                     arr[j][c] = 0

    for r in range(m):
        for c in range(n):
            if r in zr or c in zc:
                arr[r][c] = 0

    return arr

def optimal_approach(arr: list[list[int]]) -> list[list[int]]:
    """
        - Using nested loop and linear search approach.
        - Instead of using Auxiliary set, we can set first row and col to zero if want track.
        - Iterate the matrix and check if any of the cell is zero.
        - If so, mark the corresponding col in the first row and corresponding row first col.
        - After processing the entire matrix, iterate the matrix from second row and second column and mark to zero.

        - Complexity Analysis:
            - Time -> O(m * n)
            - Space -> O(1)    
    """
    m = len(arr)
    n = len(arr[0])

    has_first_row_zero = False
    has_first_col_zero = False

    for r in range(m):
        for c in range(n):
            if arr[r][c] == 0:
                arr[r][0] = 0
                arr[0][c] = 0
                
                if not has_first_row_zero and r == 0:
                    has_first_row_zero = True
                if not has_first_col_zero and c == 0:
                    has_first_col_zero = True

    for r in range(1, m):
        for c in range(1, n):
            if arr[r][0] == 0 or arr[0][c] == 0:
                arr[r][c] = 0

    if has_first_row_zero:
        for c in range(n):
            arr[0][c] = 0

    if has_first_col_zero:
        for r in range(m):
            arr[r][0] = 0

    return arr



if __name__ == "__main__":
    # arr = [[1,0], [1,1]]
    # arr = [[1,1,1],[1,0,1],[1,1,1]]
    arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]] # [[0,0,0,0], [0, 4,5, 0], [0,3,1,0]]

    # print(naive_approach(arr))
    # print(better_approach(arr))
    print(optimal_approach(arr))
    