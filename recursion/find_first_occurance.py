
def linear_search_forward(arr: list, target: int) -> int:
    return linear_search_forward_helper(arr, target, 0)


def linear_search_forward_helper(arr: list, target: int, pointer: int) -> int:
    if pointer == len(arr):
        return -1
    if arr[pointer] == target:
        return pointer
    return linear_search_forward_helper(arr, target, pointer+1)


if __name__ == "__main__":
    print(linear_search_forward([1,2,3,4,11,2], 2))