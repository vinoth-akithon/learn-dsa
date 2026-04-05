"""

"""

def naive_approach(arr: list[int]) -> int:
    """
        - Using Nested loop approach
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    n = len(arr)
    max_sum = float("-inf")

    for i in range(n):
        cur_sum = 0
        for j in range(i, n):
            cur_sum += arr[j]
            if cur_sum > max_sum:
                max_sum = max(max_sum, cur_sum)
    
    return max_sum


def optimal_approach(arr: list[int]) -> int:
    """
        - Using Kadane's Algorithm
            - At each index, decide 
                - Should we extend the previous sub-array
                - Restart with current element
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    max_sum = float("-inf")
    curr_sum = 0

    for i in range(n):
        curr_sum = max(curr_sum + arr[i], arr[i])
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

if __name__ == "__main__":
    arr = [2, 3, 5, -2, 7, -4] 
    # arr = [-2, -3, -7, -2, -10, -4]
    print(naive_approach(arr))
    print(optimal_approach(arr))
