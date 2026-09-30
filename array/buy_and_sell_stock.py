"""
"""


def naive_approach(arr: list[int]) -> int:
    """
        - Using Nested Loop and Linear Search
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    n = len(arr)
    max_profit = 0
    
    for i in range(n-1):
        b = arr[i]
        for j in range(i, n):
            p = arr[j] - b
            max_profit = max(max_profit, p)

    return max_profit


def better_approach(arr: list[int]) -> int:
    """
        - Using Min and Linear search
        - Complexity Analysis:
            - Time -> O(2n) ~= O(n)
            - Space -> O(1)
        - It won't work for some cases.
    """
    n = len(arr)
    b = arr[0]
    bi = 0
    
    for i in range(n):
        if arr[i] < b:
            b = arr[i]
            bi = i

    max_profit = 0
    for j in range(bi+1, n):
        p = arr[j] - b
        max_profit = max(max_profit, p)
    
    return max_profit


def optimal_approach(arr: list[int]) -> int:
    """
        - Using Simulation
            - What's the lowest price we've seen so far?
            - What's the profit if we sold today?
            - Is it better than our best so far?
            - Is it the lower price than so far?
            
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    min_price = arr[0]
    max_profit = 0

    for i in range(1, n):
        profit = arr[i] - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, arr[i])
    
    return max_profit


if __name__ == "__main__":
    arr = [7,1,5,3,6,4]
    # arr = [7,6,4,3,1]
    print(naive_approach(arr))
    # print(better_approach(arr))
    print(optimal_approach(arr))