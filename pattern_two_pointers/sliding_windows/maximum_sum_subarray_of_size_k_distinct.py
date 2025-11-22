import collections


def maximum_sum(arr: list[int], k: int) -> int:
    n = len(arr)
    if n < k:
        return 0
    
    max_sum = 0
    current_sum = 0
    count_map = collections.Counter()
    
    for e in range(n):
        current_sum += arr[e]
        count_map[arr[e]] += 1

        if e >= k:
            left_element = arr[e-k]
            current_sum = current_sum - left_element
            count_map[left_element] -= 1
            if count_map[left_element] == 0:
                del count_map[left_element]

        if e >= k-1 and len(count_map) == k:
            max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
    # arr = [1,5,4,2,9,9,9]; k = 3
    arr = [4,4,4]; k = 3
    print(maximum_sum(arr, k)) 