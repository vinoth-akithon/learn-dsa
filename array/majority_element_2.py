"""

"""
import math


def brute_force_approach(arr: list[int]) -> list[int]:
    """
        - Using auxiliary hashmap for storing the frequency
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(d) -> no of non duplicate elements in the input array
    """

    n = len(arr)
    hash_map = {}

    me = n // 3 + 1

    for i in range(n):
        cnt = hash_map.get(arr[i], 0) + 1
        hash_map[arr[i]] = cnt

    res = []
    for k,v in hash_map.items():
        if v >= me:
            res.append(k)
            if len(res) == 2: # Because more than 2 majority elements are not possible.
                break
    
    return res


def better_approach(arr: list[int]) -> list[int]:
    """
        - Using Sorting and counting the consecutive elements
        - Complexity Analysis:
            - Time -> O(n log n)
            - Space -> O(1)
    """

    n = len(arr)
    
    arr.sort()

    pre = arr[0]
    cnt = 1
    res = set()
    me = n // 3 + 1

    for i in range(1, n):
        if pre == arr[i]:
            cnt += 1
        else:
            if cnt >= me:
                res.add(pre)
                if len(res) == 2:
                    break
            pre = arr[i]
            cnt = 1

    if cnt >= me:
        res.add(pre)
    
    return list(res)



def optimal_approach(arr: list[int]) -> list[int]:
    """
        - Using counters
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """

    n = len(arr)
    me = n // 3 + 1
    
    ele1 = ele2 = None
    cnt1 = cnt2 = 0

    for i in range(n):
        if cnt1 == 0 and arr[i] != ele2:
            ele1 = arr[i]
            cnt1 += 1
        elif cnt2 == 0 and arr[i] != ele1:
            ele2 = arr[i]
            cnt2 += 1
        elif arr[i] == ele1:
            cnt1 += 1
        elif arr[i] == ele2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    cnt1 = cnt2 = 0
    for i in range(n):
        if arr[i] == ele1:
            cnt1 += 1
        elif arr[i] == ele2:
            cnt2 += 1

    res = []
    for e, c in [(ele1, cnt1), (ele2, cnt2)]:
        if e and c >= me:
            res.append(e)

    return res






if __name__ == "__main__":
    # arr = [1, 2, 1, 1, 3, 2]   
    arr = [1, 2, 1, 1, 3, 2, 2]
    arr = [1]
    arr = [1,2]
    # print(brute_force_approach(arr))
    # print(better_approach(arr))
    print(optimal_approach(arr))

    
