import collections

def total_fruits(arr: list[int]) -> int:
    n = len(arr)
    count_map = collections.Counter()
    max_window = 0
    s = 0

    for e in range(n):
        count_map[arr[e]] += 1

        while len(count_map) > 2:
            left_element = arr[s]
            count_map[left_element] -= 1
            if count_map[left_element] == 0:
                del count_map[left_element]
            s += 1

        current_window = e - s + 1
        max_window = max(current_window, max_window)

    return max_window


if __name__ == "__main__":
    # arr = [1,2,1]
    # arr = [0,1,2,2]
    arr = [1,2,3,2,2]
    print(total_fruits(arr))