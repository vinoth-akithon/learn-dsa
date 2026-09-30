"""
"""


def brute_force(arr: list[int]) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n/2 +1)
    """
    processed = set()
    res = 0

    for e in arr:
        if e not in processed:
            res += e
            processed.add(e)
        else:
            res -= e

    return res


def better_approach1(arr: list[int]) -> int:
    """
        - Using XOR operator
            - a ^ a -> 0
            - a ^ 0 -> a
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    res = 0
    for e in arr:
        res ^= e
    
    return res


def better_approach2(arr: list[int]) -> int:
    """
        - Comparing next neighbor and making the decision immediately.
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    f = 0

    while (f < n-1):
        if arr[f] == arr[f+1]:
            f += 2
        else:
            return arr[f]

    return arr[n-1]

def better_approach3(arr: list[int]) -> int:
    """
        - Comparing neighbors both the sides and handling edge cases separately
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    
    """
    n = len(arr)

    if n == 1:
        return arr[0]

    for i in range(n):
        if i == 0 and arr[i] != arr[i+1]:
            return arr[i]
        elif i == n-1 and arr[i] != arr[i-1]:
            return arr[n-1]
        elif arr[i] != arr[i-1] and arr[i] != arr[i+1]:
            return arr[i]
        

def optimal_approach(arr: list[int]) -> int:
    """
        - possible pair (if all the elements are pairs)
            - start at even index 
            - end at odd index
        - mixing of an unique element cause these rules break
        - We need to identify where this rule break, and cut off half of array
        - we are asking at some random idx, where is my next element (either start or end)
            - If I am at start, XOR gives end
            - If I am at end, XOR gives start

        - Complexity Analysis:
            - Time -> O(log n)
            - Space -> O(1)
    """
    n = len(arr)
    s = 0
    e = n-1

    while (s <= e):
        m = s + (e - s)//2

        if s == m == e:
            return arr[m]
        
        elif arr[m] == arr[m ^ 1]:
            s = m+1
        else:
            e = m


if __name__ == "__main__":
    # arr = [1,1,2,2,3,3,4,5,5,6,6]
    arr = [1,1,2]
    arr = [1,1,3,5,5]
    arr = [2]
    print(brute_force(arr))
    print(better_approach1(arr))
    print(better_approach2(arr))
    print(better_approach2(arr))
    print(optimal_approach(arr))


    """
    arr[m] -> 3
    arr[m ^ 1] -> arr[5 ^ 1] -> arr[4] -> 3
    

   
    """




