
def linear_search_backward(arr: list, target: int) -> int:
    return linear_search_backward_helper(arr, target, len(arr)-1)


def linear_search_backward_helper(arr: list, target: int, pointer: int) -> int:
    if pointer == -1:
        return -1
    if arr[pointer] == target:
        return pointer
    return linear_search_backward_helper(arr, target, pointer-1)


if __name__ == "__main__":
    print(linear_search_backward([1,2,3,4,11,2], 2))