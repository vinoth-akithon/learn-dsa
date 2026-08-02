"""

"""

def brute_force_approach(arr: list[list[int]]) -> list[list[int]]:
    """
        - Using Simulation approach

        - Complexity Analysis:
            - Time -> O(n log n)
            - Space -> O(2n)

    
    """
    n = len(arr)
    if n == 1:
        return arr
    
    res = []

    arr.sort(key=lambda i:i[0])

    for i in range(1, n):
        from_result = False
        if res:
            from_result = True
            pre = res[-1]
        else:
            pre = arr[i-1]
        
        if arr[i][0] > pre[1]:
            if len(res) == 0:
                res.append(pre)
                res.append(arr[i])
            else:
                res.append(arr[i])

        else:
            f = min(pre[0], arr[i][1])
            s = max(pre[1], arr[i][1])
            if from_result:
                res[-1] = [f, s]
            else:
                res.append([f, s])

    return res


if __name__ == "__main__":
    # arr = [[1,3],[2,6],[8,10],[15,18]]
    # arr = [[1,4],[4,5]]
    # arr = [[4,7],[1,4]]
    arr = [[1,4],[5,6]]
    # arr = [[1,3]]
    # arr = [[1,4],[0,2],[3,5]]
    print(brute_force_approach(arr))