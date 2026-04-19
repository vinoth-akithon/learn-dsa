"""
"""

def get_all_pairs(arr: list[int], idx: int) -> list[tuple[int, int]]:
    """
    """
    n = len(arr)

    pairs = []
    for i in range(idx, n):
        for j in range(i+1, n):
            pairs.append((arr[i], arr[j]))

    return pairs

def get_unique_pairs_with_orders_matter(arr: list[int], idx: int) -> list[tuple[int, int]]:
    """
    """
    n = len(arr)

    pairs = set()
    for i in range(idx, n):
        for j in range(i+1, n):
            pairs.add((arr[i], arr[j]))

    return list(pairs)

def get_unique_pairs_without_orders_matter(arr: list[int], idx: int) -> list[tuple[int, int]]:
    """
    """
    n = len(arr)

    pairs = set()
    for i in range(idx, n):
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                pair = (arr[i], arr[j])
            else:
                pair = (arr[j], arr[i])
            pairs.add(pair)

    return list(pairs)

def get_unique_trippets_without_order_matters(arr: list[int]) -> list[tuple[int, int, int]]:
    """
    """
    n = len(arr)

    trippets = set()

    for i in range(n-2):
        for pair in get_unique_pairs_without_orders_matter(arr, i+1):
            trippets.add((arr[i], *pair))

    return list(trippets)

def brute_force_approach(arr: list[int], t: int) -> list[list[int]]:
    """
        - Finding all possible triplets and check triplet sum against the target.
        - If matched, add that triplet (sorted triplet for orders doesn't matter problem) into the set for uniqueness.

        - Complexity Analysis:
            - Time -> O(n^3)
            - Space -> O(3 * nCr) ~= O(1) -> Due to resultant array
    """
    n = len(arr)

    triplets = set()

    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                triplet = [arr[i], arr[j], arr[k]]
                if sum(triplet) == t:
                    triplets.add(tuple(sorted(triplet)))

    return [list(i) for i in triplets]


def better_approach(arr: list[int], t: int) -> list[list[int]]:
    """
        - Fixing one element and applying two sum with auxiliary set.
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(n + 3nCr)
    """
    n = len(arr)

    triplets = set()
    for i in range(n-2):
        hash_set = set()
        for j in range(i+1, n):
            third = - (arr[i] + arr[j])
            if third in hash_set:
                triplet = [arr[i], arr[j], third]
                triplet.sort()
                triplets.add(tuple(triplet))

            hash_set.add(arr[j])
    
    return [list(item) for item in triplets]


def optimal_approach(arr: list[int], t: int) -> list[list[int]]:
    """
        - Fixing one element and applying two sum with auxiliary set.
        - Complexity Analysis:
            - Time -> O(nlogn + n^2) ~= O(n^2)
            - Space -> O(3nCr) ~= O(1) due to resultant array
    """
    n = len(arr)
    arr.sort()
    triplets = []

    for i in range(n-2):
        if i > 0 and arr[i-1] == arr[i]:
            continue
        nt = t - arr[i]
        l = i+1
        r = n-1
        while (l < r):
            if l > i+1 and arr[l-1] == arr[l]:
                l += 1
                continue
            sum = arr[l] + arr[r]
            if sum == nt:
                triplets.append([arr[i], arr[l], arr[r]])
                l += 1
                r -= 1
            elif sum < nt:
                l += 1
            else:
                r -= 1
    
    return triplets

if __name__ == "__main__":
    # arr = [1, 2, 3, 1] # 
    arr = [-1,0,1,2,-1,-4]
    # arr = [-1,0,1,0]
    # print(get_all_pairs(arr, 0)) 
    # print(get_unique_pairs_with_orders_matter(arr, 0)) 
    # print(get_unique_pairs_without_orders_matter(arr, 0))

    # print(get_unique_trippets_without_order_matters(arr)) 
    print(brute_force_approach(arr, 0))
    print(better_approach(arr, 0))
    print(optimal_approach(arr, 0))


