"""
"""

def brute_force(mat: list[list[int]]) -> int:
    """
        Complexity Analysis:
            - Time -> O(M * N) + O(M*N log (M*N)) ~= O(M * N * log(M*N))
            - Space -> O(1)
    """
    M = len(mat)
    N = len(mat[0])

    auxiliary_arr = []
    for r in range(M):
        for c in range(N):
            auxiliary_arr.append(mat[r][c])
    
    auxiliary_arr.sort()
    return auxiliary_arr[(M*N)//2]


import bisect

def countLessEqual(row, mid):
    return bisect.bisect_right(row, mid)


def get_count1(mat: list[int], t: int):
    M = len(mat)
    N = len(mat[0])
    cnt = 0

    for r in range(M):
        s = 0
        e = N-1
        idx = -1

        while (s <= e):
            m = s + (e-s)//2
            
            if mat[r][m] <= t:
                idx = m
                s = m+1
            else:
                e = m-1
        cnt += idx+1
    
    return cnt

def get_count2(mat: list[list[int]], t: int):
    M = len(mat)
    cnt = 0
    for r in range(M):
        cnt += countLessEqual(mat[r], t)
    
    return cnt




def optimal_approach(mat: list[list[int]]) -> int:
    """
        - Complexity Analysis:
            - Time -> O(log(Max-min) * rows * log(cols)) 
            - Space -> O(1)
    """
    M = len(mat)
    N = len(mat[0])

    s = min([mat[r][0] for r in range(M)])
    e = max([mat[r][N-1] for r in range(M)])
    ans = None

    while (s <= e):
        m = s + (e-s)//2

        if get_count2(mat, m) >= (M*N)//2+1:
            ans = m
            e = m-1
        else:
            s = m+1

    return ans


if __name__ == "__main__":
    # mat = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
    # mat = [[2, 4, 9], [3, 6, 7], [4, 7, 10]]
    mat = [[3], [4], [8]]
    print(brute_force(mat))
    print(optimal_approach(mat))
