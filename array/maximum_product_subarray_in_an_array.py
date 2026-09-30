"""
Given an array of positive and negative integers.

Find the maximum product sub array and return the that product value. 
"""

def brute_force(arr: list[int]) -> int:
    """
        - Using nested loop approach for finding all the possible sub arrays and their product.

        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    n = len(arr)
    max_p = float("-inf")

    for i in range(n):
        p = arr[i] 
        if p > max_p: # handling the first element is also maximum product sub array
            max_p = p

        for j in range(i+1, n):
            p *= arr[j]
            if p > max_p:
                max_p = p

    return max_p 


def better_approach(arr: list[int]) -> int:
    """
        - Using Kadane's Algo.

        - Complexity Analysis:
    
    """
    n = len(arr)
    max_p = float("-inf")
    
    curr_p = 1
    for i in range(n):
        curr_p = max(curr_p*arr[i], arr[i])
        max_p = max(max_p, curr_p)
    
    return max_p



if __name__ == "__main__":
    # arr = [1,2,3,4,5,0]
    arr = [1,2,-3,0,-4,-5]
    print(brute_force(arr))
    print(better_approach(arr))