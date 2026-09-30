"""
Union of two sorted array (can be common between arrays and distinct elements in each array)

arr1 = [1,2,3,4] , arr2 = [3,4,5,6]
union(arr1, arr2) => [1,2,3,4,5,6]
"""


def naive_approach(arr1: list[int], arr2: list[int]) -> list[int]:
    """
        - Using Hash Set approach.
        - Iterate all the elements from each array and insert into set.
        - Finally convert set into array for sorting.
        - returning the sorted array.

        - Complexity Analysis:
            - Time -> O((m+n) log(m+n)) -> Due to sorting
            - Space -> O(d) -> No of non duplicate elements, due to auxiliary set data structure
    """

    hash_set = set()
    m = len(arr1)
    for i in range(m):
        hash_set.add(arr1[i])

    n = len(arr2)
    for i in range(n):
        hash_set.add(arr2[i])
    
    result = list(hash_set)
    result.sort()

    return result


def optimal_approach(arr1: list[int], arr2: list[int]) -> list[int]:
    """
        - Using Two pointers approach (merge sort algo)
        - Keep two pointers each points to start of the each array
        - Compare the left pointer is the less than the right and non duplicate, then insert the left pointer pointing element into the resultant array and move left pointer one step forward.
        - Else if the left pointer is greater than the right and non duplicate, then inset the right pointer pointing element into the resultant array and move right pointer one step forward.
        - If both pointers pointing the same value and non duplicate, then insert that element into the resultant element and move both pointers one step forward.
        - Do these step until any one of the array exhausted.
        - Handle the non exhausted array separately  by inserting into resultant array if non duplicate.

        - We can check the duplicate in the sorted array by comparing last element in the resultant array and current element.

        - Complexity Analysis:
            - Time -> O(m + n)
            - Space -> O(1)
    """
    l = r = 0
    m = len(arr1)
    n = len(arr2)
    result = []

    while (l < m) and (r < n):
        if arr1[l] < arr2[r]:
            if not result or result[-1] != arr1[l]:
                result.append(arr1[l])
            l += 1
        elif arr1[l] > arr2[r]:
            if not result or result[-1] != arr2[r]:
                result.append(arr2[r])
            r += 1
        else:
            if not result or result[-1] != arr1[l]:
                result.append(arr1[l])
            l += 1
            r += 1

    while (l < m):
        if not result or result[-1] != arr1[l]:
            result.append(arr1[l])
        l += 1
    
    while (r < n):
        if not result or result[-1] != arr2[r]:
            result.append(arr2[r])
        r += 1

    return result


if __name__ == "__main__":
    arr1 = [1,2,3,4]; arr2 = [3,4,5,6]
    # print(naive_approach(arr1, arr2))
    print(optimal_approach(arr1, arr2))