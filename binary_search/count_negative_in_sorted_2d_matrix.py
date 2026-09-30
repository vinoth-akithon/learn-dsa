"""
Given Input matrix, each row is sorted in non-increasing order (means descending order)
"""


def brute_force(mat: list[list[int]]) -> int:
    """
        - Checking all the possibilities (If we found the first negative on a row then move to next row)

        - Complexity Analysis:
            - Time -> O(M * N)
            - Space -> O(1)
    """

    M = len(mat)
    N = len(mat[0])
    cnt = 0

    for r in range(M):
        for c in range(N):
            if mat[r][c] < 0:
                cnt += N - c
                break
    return cnt



def optimal_approach(mat: list[list[int]]) -> int:
    """
        - Find the first negative element in each row and compute the total negative numbers corresponding to that row.
        - Finally cumulate all negative numbers and return

        - Apply Binary search on each row for getting total negative for that row.

        - Complexity Analysis:
            - Time -> O(M * log (N)) 
            - Space -> O(1)
    
    """
    M = len(mat)
    N = len(mat[0])
    cnt = 0

    for r in range(M):
        start = N

        s = 0
        e = N-1
        while (s <= e):
            m = s + (e-s)//2

            if mat[r][m] < 0:
                start = m
                e = m-1
            else:
                s = m+1
        cnt += N-start
    
    return cnt


if __name__ == "__main__":
    mat = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    # mat = [[3,2],[1,0]] 

    print(brute_force(mat))
    print(optimal_approach(mat))
