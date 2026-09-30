"""
"""



def brute_force(arr: list[int], k: int) -> int:
    """
        - Complexity Analysis:
            - Time -> ( (n log n) + (n * (Max(arr)-Min(arr))) ) ~= O(n * Max(arr) - Min(arr))
            - Space -> O(1)
    """
    n = len(arr)
    stalls = sorted(arr)
    max_dis = max(stalls) - min(stalls)

    ans = 0
    for dis in range(1, max_dis+1):
        cnt = 1
        pre_stall = stalls[0]

        for i in range(1, n):
            if stalls[i] - pre_stall >= dis:
                cnt += 1
                pre_stall = stalls[i]
            
        if cnt >= k:
            ans = dis
        else:
            break

    return ans


def optimal_approach(arr: list[int], k: int) -> int:
    """
    - Applying binary search 
    - Complexity Analysis:
        - Time -> O( (n * log n) + (n * log(Max(arr)-Min(arr))) ) ~= O(n * log(Max(arr) - Min(arr)))
        - Space -> O(1)
    """

    n = len(arr)
    stalls = sorted(arr)
    max_dis = max(arr) - min(arr)

    s = 1
    e = max_dis
    ans = 0

    while (s <= e):
        dis = s + (e-s)//2

        cnt = 1
        pre_stall = stalls[0]
        for i in range(1, n):
            if stalls[i] - pre_stall >= dis:
                cnt += 1
                pre_stall = stalls[i]
        
        if cnt < k:
            e = dis -1
        else:
            s = dis + 1
            ans = dis

    return ans



if __name__ == "__main__":
    arr = [0,3,4,7,10,9]; k = 4
    arr = [4,2,1,3,6]; k = 2
    arr = [18, 8, 20, 7 ,9, 1, 14, 17, 11, 19, 6 ,15, 2, 13, 5]; k = 6
    print(brute_force(arr, k))
    print(optimal_approach(arr, k))



"""
arr = [1,2,3,4,6]; k = 2

dis = 3
cnt < k -> 2 (1,4) >= 2
ans = 3


arr = [4,6]; k = 2
dis = 4

"""



"""
arr = [0,3,4,7,10,9]; k = 4

nearest stall -> 0
farthest stall -> 10


i -> stall
arr[i] -> stall distance
[0,3,4,7,9,10]

max distance = farthest stall - first stall 
cnt = 1
at distance 1,

    curr_stall - pre_stall >= distance
        3 - 0 >= 1
        cnt => 2
        pre_stall = 3

        4 - 3 >= 1
        cnt => 3
        pre_stall = 4

        
    we can place 6 cows


at distance 2
    3 - 0 >= 2
    cnt => 2
    pre stall = 3


    we can place 4 cows


at distance 3
    we can place 4 cows


at distance 4
    we can place 3 cows





    
if distance bw stall short -> more cows we can place
if distance bw stall far -> less cows we can place
"""
