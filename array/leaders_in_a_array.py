"""
- An element in the array called leader when all the elements next to it (till end) should be less than that element.
"""

def naive_approach(arr: list[int]) -> int:
    """
        - Using nested loop and Linear search.
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    n = len(arr)
    cnt = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] >= arr[i]:
                break
        else:
            cnt += 1

    return cnt


def optimal_approach(arr: list[int]) -> int:
    """
        - Using linear search from reverse.
        - Keep one variable for maxElement seen so far.
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    cnt = 0
    max_elem = float("-inf")
    
    for i in range(n-1, -1, -1):
        if arr[i] >= max_elem:
            cnt += 1
            max_elem = arr[i]

    return cnt



if __name__ == "__main__":
    arr = [4, 7, 1, 0] # 3 leaders 7,1,0
    # arr = [10, 22, 12, 3, 0, 6]
    # print(naive_approach(arr))
    print(optimal_approach(arr))
