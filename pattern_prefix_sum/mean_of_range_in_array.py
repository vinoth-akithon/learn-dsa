"""

"""



import math

def solution(arr: list[int], quries:list[tuple[int, int]]) -> int:
    """
    Complexity Analysis:
        - Time -> O(n * q)
        - Space -> O(1)
    
    :param arr: Description
    :type arr: list[int]
    :param quries: Description
    :type quries: list[tuple[int, int]]
    :return: Description
    :rtype: int
    """

    n = len(arr)

    prefix_sum = [arr[0]]
    for i in range(1, n):
        prefix_sum.append(arr[i] + prefix_sum[i-1])
    
    result = []
    for q in quries:
        # range_sum = arr[r] - arr[l-1]
        if q[0] == 1:
            range_sum = prefix_sum[q[1]-1]
        else:
            range_sum = prefix_sum[q[1]-1] - prefix_sum[q[0]-1-1]
        mean = range_sum/(q[1]-q[0]+1)
        result.append(math.floor(mean))
    
    
    return result

if __name__ == "__main__":
    # arr = [3, 7, 2, 8, 5]; q = [[1, 3], [2, 5]]
    arr = [10, 20, 30, 40, 50, 60]; q = [[4, 6]]
    print(solution(arr, q))