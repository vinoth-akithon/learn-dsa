"""

"""


def brute_force(arr: list[int], d: int) -> int:
    """
        Complexity Analysis:
            Time -> O(n * Sum(arr) - Max(arr))
            Space -> O(1)
    """
    n = len(arr)
    lar = max(arr)
    total = sum(arr)

    for c in range(lar, total+1):
        days = 1
        curr_cap = 0

        for i in range(n):
            new_cap = curr_cap + arr[i]
            if new_cap > c:
                days += 1
                curr_cap = arr[i]
            else:
                curr_cap += arr[i]


            # This condition is handled at start by setting days =1
            # if i == n-1 and curr_cap > 0:
            #     days +=1
            
            if days > d:
                break
                
        if days <= d:
            return c
        

def optimal_approach(arr: list[int], d: int) -> int:
    """
        - Using Binary Search

        - Complexity Analysis:
            - Time -> O(log(Sum(arr) - Max(arr)) * n)
            - Space -> O(1)
    """
    n = len(arr)
    lar = max(arr)
    total = sum(arr)

    s = lar
    e = total
    ans = None

    while (s <= e):
        c = s + (e-s)//2

        days = 1
        curr_cap = 0
        for i in range(n):
            new_cap = curr_cap + arr[i]
            if new_cap > c:
                days += 1
                curr_cap = arr[i]
            else:
                curr_cap += arr[i]


            if days > d:
                break

        if days <= d:
            ans = c
            e = c -1
        else:
            s = c + 1

    return ans




if __name__ == "__main__":
    # arr = [5, 4, 5, 2, 3, 4, 5, 6]; d = 5
    arr = [1, 2, 3, 4, 5]; d = 2
    print(brute_force(arr, d))
    print(optimal_approach(arr, d))




"""
Dry run 1:

arr = [5, 4, 5, 2, 3, 4, 5, 6]; d = 5

lar = 6
total = 34

for c = 6,



"""