"""
"""

import math

def brute_force(arr: list[int], h: int):
    """
        Complexity Analysis:
            - Time -> O(n max(arr))
            - Space -> O(1)

    """

    n = len(arr)
    largest = max(arr)

    for i in range(1, largest+1):
        count = 0
        for j in range(n):
            count += math.ceil(arr[j]/i)
            if count > h:
                break

        if count <= h:
            return i
        

def optimal_approach(arr: list[int], h: int):
    """
        Complexity Analysis:
            - Time -> O(n log (max(arr)))
            - Space -> O(1)

    """

    n = len(arr)
    e = max(arr)
    s = 1
    speed = float("inf")

    while (s <= e):
        curr_speed = s + (e-s)//2
        hour = 0
        for j in range(n):
            hour += math.ceil(arr[j]/curr_speed)

        if hour <= h:
            speed = curr_speed
            e = curr_speed-1
        else:
            s = curr_speed+1

    return speed
            
        

if __name__ == "__main__":
    arr = [7,15, 6,3]; h=8
    # arr = [25, 12, 8, 14, 19]; h = 5
    print(brute_force(arr, h))
    print(optimal_approach(arr, h))

