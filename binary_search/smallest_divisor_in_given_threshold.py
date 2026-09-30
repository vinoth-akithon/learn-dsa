"""
"""

import math

ceil = math.ceil

def brute_force(arr: list[int], t: int):
    """
        - Complexity Analysis:
            - Time -> O(n * Max(arr))
            - Space -> O(1)
    """
    lar = max(arr)
    
    for divisor in range(1, lar+1):
        sum = 0
        for e in arr:
            sum += ceil(e/divisor)
            if sum > t:
                break
        if sum <= t:
            return divisor
        

def optimal_approach(arr: list[int], t: int):
    """
    - Using Binary search

    - Complexity Analysis:
        - Time -> O(log n * Max(arr))
        - Space -> O(1)
    """
    n = len(arr)
    lar = max(arr)
    ans = None

    s = 1
    e = lar

    while (s <= e):
        divisor = s + (e-s)//2

        sum = 0
        for i in range(n):
            sum += ceil(arr[i]/divisor)
            if sum > t:
                break
        
        if sum > t:
            s = divisor + 1
        else:
            ans = divisor
            e = divisor - 1

    return ans


if __name__ == "__main__":
    # arr = [1,2,3,4,5]; t = 8
    # arr = [8,4,2,3]; t = 10
    arr = [44,22,33,11,1]; t = 5
    print(brute_force(arr, t))
    print(optimal_approach(arr, t))




# 1,2,3,4,5,6


# largest divisor -> small sum
# smallest divisor -> largest sum

"""

for arr = [8,4,2,3]; t = 10

max = 

for 4 -> [2,1,1,1] -> 5 <= 10
here sum is too small indicating divisor is large so, decreasing the divisor

for 2 -> [4, 2,1,2] -> 9 <= 10
here sum is low and indicating divisor is large, so, decreasing the divisor

for 1 -> [8,4,2,3] -> 17 > 10
here is sum is high and indicating divisor is small, so need to increase the divisor

"""

"""
for arr = [44,22,33,11,1]; t = 5

max = 44

for 22 -> [2, 1, 2, 1, 1] -> 7 > 5
here sum is large amd indicating divisor is low, increase the divisor

for 33 -> [2,1,1,1,1] -> 6 > 5
here sum is large amd indicating divisor is low, increase the divisor

for 38 -> [2,1,1,1,1] -> 6 > 5
here sum is large amd indicating divisor is low, increase the divisor

for 41 -> [2,1,1,1,1] -> 6 > 5
here sum is large amd indicating divisor is low, increase the divisor

for 43 -> [2,1,1,1,1] -> 6 > 5
here sum is large amd indicating divisor is low, increase the divisor

for 44 -> [1,1,1,1,1] -> 5 <= 5
here sum is small and indicating divisor is large, decrease the divisor

"""