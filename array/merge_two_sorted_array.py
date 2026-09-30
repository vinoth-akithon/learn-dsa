"""
Merge the two sorted array
where, arr1_size = m + n (so, actual size is m-n )and arr2_size = n

"""


def brute_force_approach(arr1: list[int], arr2: list[int]) -> None:
    """
    - Using Merge implementation algo with auxiliary array for storing the result


    Complexity Analysis:
        Time -> O(m)
        Space -> O(m)
    """
    n = len(arr2)
    m = len(arr1) - n
    res = []

    l = r = 0
    while (l < m and r < n):
        if arr1[l] == arr2[r]:
            res.append(arr1[l])
            res.append(arr2[r])
            l += 1
            r += 1
        elif arr1[l] < arr2[r]:
            res.append(arr1[l])
            l += 1
        else:
            res.append(arr2[r])
            r += 1
    
    while (l < m):
        res.append(arr1[l])
        l += 1
    
    while (r < n):
        res.append(arr2[r])
        r += 1

    for i in range(len(res)):
        arr1[i] = res[i]


def better_approach(arr1: list[int], arr2: list[int]) -> None:
    """
    - Using Merge Implementation algo and shifting


    Complexity Analysis:
        Time -> O(m * n)
        Space -> O(1)
    """
    n = len(arr2)
    m = len(arr1) - n


    l = r = 0
    while (l < m + r and r < n):
        if arr1[l] < arr2[r]:
            l += 1
        else:
            # shifting all the elements one step to right for placing the right element
            for i in range(m+r, l, -1):
                arr1[i] = arr1[i -1]
            arr1[l] = arr2[r]
            r += 1
            l += 1

    while (r < n):
        arr1[l] = arr2[r]
        l += 1
        r += 1

def optimal_approach(arr1: list[int], arr2: list[int]) -> None:
    """
    - Using Reverse Merge Implementation


    Complexity Analysis:
        Time -> O(m) -> length of array 1
        Space -> O(1)
    """
    n = len(arr2)
    m = len(arr1) - n

    l = m-1
    r = n-1
    i = m+n-1

    while (l >= 0 and r >= 0):
        if arr1[l] == arr2[r]:
            arr1[i] = arr1[l]
            arr1[i-1] = arr2[r]
            i -= 2
            l -= 1
            r -= 1
        elif arr1[l] > arr2[r]:
            arr1[i] = arr1[l]
            i -= 1
            l -= 1
        else:
            arr1[i] = arr2[r]
            i -= 1
            r -= 1

    while (r >= 0):
        arr1[i] = arr2[r]
        i -= 1
        r -= 1



if __name__ == "__main__":
    arr1 = [-5, -2, 4, 5, 0, 0, 0]; arr2 = [-3, 1, 8]
    # arr1 = [1,2,3,0,0,0]; arr2 = [2,5,6]
    # arr1 = [0]; arr2 = [1]
    # print(brute_force_approach(arr1, arr2))
    better_approach(arr1, arr2)
    # optimal_approach(arr1, arr2)
    print(arr1)