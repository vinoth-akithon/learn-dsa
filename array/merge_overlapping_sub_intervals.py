"""
Given an array of intervals.
Interval has start and end entity, where start <= end (i.e for [1, 2] -> [1, 2] and for [1,4] -> [1,2,3,4] and for [1, 1] -> [1]

"""


def optimal_approach(arr: list[list[int]]) -> list[list[int]]:
    """
        - Using nested loop approach
        - We have to sort the the interval array based on start of each interval
        - For every interval, we need to check all the future interval is overlap or not
        - If overlap, we to merge them by checking (future_interval[i] <= current_merged_interval) until non overlap
        - If non overlap found, we have to add the merged interval into resultant array and form the next merged interval.

        - Complexity Analysis:
            - Time -> O(n log n)
            - Space -> O(n)
    """

    n = len(arr)
    arr.sort(key=lambda i:i[0])
    res = []
    for i in range(n):
        interval = arr[i]
        if not res:
            res.append(interval)
        elif res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])

    return res

if __name__ == "__main__":
    # arr = [[1,3],[2,6],[2,6],[8,10],[15,18]] # [[1,6], [8, 10], [15, 18]]
    arr = [[1, 2], [3, 4]]
    print(optimal_approach(arr))