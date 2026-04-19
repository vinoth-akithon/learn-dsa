"""
"""



def optimal_approach(arr: list[int], t: int) -> list[list[int]]:
    """
        - Fixing one element and applying two sum with auxiliary set.
        - Complexity Analysis:
            - Time -> O(nlogn + n^3) ~= O(n^3)
            - Space -> O(4nCr) ~= O(1) due to resultant array
    """
    n = len(arr)
    arr.sort()
    quadruplets = []

    for i in range(n-3):
        if i > 0 and arr[i-1] == arr[i]:
            continue

        for j in range(i+1, n-2):
            if j > i+1 and arr[j-1] == arr[j]:
                continue
            nt = t - (arr[i] + arr[j])
            l = j+1
            r = n-1
            while (l < r):
                if l > j+1 and arr[l-1] == arr[l]:
                    l += 1
                    continue
                sum = arr[l] + arr[r]
                if sum == nt:
                    quadruplets.append([arr[i], arr[j], arr[l], arr[r]])
                    l += 1
                    r -= 1
                elif sum < nt:
                    l += 1
                else:
                    r -= 1
    
    return quadruplets


if __name__ == "__main__":
    # arr = [1,0,-1,0,-2,2]; t=0
    arr = [4,3,3,4,4,2,1,2,1,1]; t=9
    print(optimal_approach(arr, t))