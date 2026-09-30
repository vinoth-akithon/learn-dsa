"""

"""



def brute_force(arr: list[int], m: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n * Sum(arr)-Max(arr))
            - Space -> O(1)
    
    """
    n = len(arr)
    
    if m > n:
        return -1
    
    min_page = max(arr)
    if m == n:
        return min_page

    max_page = sum(arr)
    if m == 1:
        return max_page

    for p in range(min_page, max_page+1):
        users = 1
        pages = 0

        for i in range(n):
            new_pages = pages + arr[i]
            if new_pages > p:
                users += 1
                pages = arr[i]
            else:
                pages += arr[i]

        if users <= m:
            return p
        
    return -1


def optimal_approach(arr: list[int], m: int) -> int:
    """
        - Using Binary Search
        - Complexity Analysis:
            - Time -> O(n * log(Sum(arr) - Max(arr)))
            - Space -> O(1)
    """
    n = len(arr)
    if n < m:
        return -1

    min_page = max(arr)
    if n == m:
        return min_page
    
    max_page = sum(arr)
    if m == 1:
        return max_page
    
    ans = -1
    s = min_page
    e = max_page

    while (s <= e):
        p = s + (e-s)//2

        user = 1
        pre_pages = 0

        for i in range(n):
            new_pages = pre_pages + arr[i]
            if new_pages > p:
                user += 1
                pre_pages = arr[i]
            else:
                pre_pages += arr[i]

        if user > m: # Less pages
            s = p+1            
        else: # More pages
            ans = p
            e = p -1

    return ans
    

        

if __name__ == "__main__":
    arr = [12, 34, 67, 90]; m = 2
    # arr = [25, 46, 28, 49, 24]; m=4
    # arr = [15,10, 19, 10 ,5 ,18, 7]; m=5
    # arr = [22, 23, 67]; m=1
    print(brute_force(arr, m))
    print(optimal_approach(arr, m))




"""

pages = 100

if less users -> More pages
if more users -> less pages


"""