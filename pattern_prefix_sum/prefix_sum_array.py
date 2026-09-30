"""
Return the prefix sum array of the given array.

Each element in the prefix sum array is the sum of all the element in the original before it's index. 
prefix_sum[i] = arr[:i+1]

Complexity Analysis:
    - Time -> O(n)
    - Space -> O(n)

Notes:
    - In computer science, the `Prefix` is ending at `i` not end before `i`.
    - This is intentional. Range sum becomes one simple sunstration.
        - Sum(l, r) = prefix[r] - prefix[l-1]
"""


def prefix_sum(arr: list[int]) -> list[int]:
    n = len(arr)
    prefix_sum = [arr[0]]
    
    for i in range(1, n):
        prefix_sum.append(prefix_sum[i-1] + arr[i])

    return prefix_sum



if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(prefix_sum(arr))