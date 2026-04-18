"""

"""


def naive_approach(arr: list[list[int]]) -> list[list[int]]:
    """
        - Using nested loop approach and auxiliary set.
        - In the approach pick a row and transform that row into right column.
        - Example first row goes to last column and second row goes to second last column

        - Complexity Analysis:
            - Time -> O(n*2)
            - Space -> O(n*2)
    """
    n = len(arr)
    aux_matrix = []

    for _ in range(n):
        aux_matrix.append([0] * n) 

    for r in range(n):
        col_goes = n-r-1
        for c in range(n):
            aux_matrix[c][col_goes] = arr[r][c]

    for r in range(n):
        for c in range(n):
            arr[r][c] = aux_matrix[r][c]
    
    return arr

def better_approach(arr: list[list[int]]) -> list[list[int]]:
    """
        - Using nested loop approach and auxiliary set. (Nothing changes in complexity wise)
        - In the approach pick element move the element into right place directly using formula
            - arr(i, j) => arr(j, n-i-1)
        - Complexity Analysis:
            - Time -> O(n*2)
            - Space -> O(n*2)
    """
    n = len(arr)
    aux_matrix = []

    for _ in range(n):
        aux_matrix.append([0] * n) 

    for r in range(n):
        for c in range(n):
            aux_matrix[c][n-r-1] = arr[r][c]

    for r in range(n):
        for c in range(n):
            arr[r][c] = aux_matrix[r][c]
    
    return arr

def optimal_approach1(arr: list[list[int]]) -> list[list[int]]:
    """
        - Using Matrix properties. 
        - Transpose the given array and reverse all the rows one by one.
        - Complexity Analysis:
            - Time -> O(n*2)
            - Space -> O(n)
    """
    n = len(arr)
    already_swapped = set()

    for r in range(n):
        for c in range(n):
            if (r, c) not in already_swapped:
                arr[r][c], arr[c][r]  = arr[c][r], arr[r][c]
                already_swapped.add((c, r))

    for r in range(n):
        arr[r].reverse()
    
    return arr

def optimal_approach2(arr: list[list[int]]) -> list[list[int]]:
    """
        - Using Matrix properties. 
        - Transpose the given array and reverse all the rows one by one.
        - To avoid the duplicate swapping, we use matrix diagonal property.
        - Complexity Analysis:
            - Time -> O(n*2)
            - Space -> O(1)
    """
    n = len(arr)

    for r in range(n):
        for c in range(r+1, n):
            arr[r][c], arr[c][r]  = arr[c][r], arr[r][c]

    for r in range(n):
        arr[r].reverse()
    
    return arr






if __name__ == "__main__":
    arr = [[1,2], [3,4]] # [[3, 1], [4, 2]]
    # arr = [[1,2,3],[4,5,6],[7,8,9]]
    # print(naive_approach(arr))
    # print(better_approach(arr))
    # print(optimal_approach1(arr))
    print(optimal_approach2(arr))