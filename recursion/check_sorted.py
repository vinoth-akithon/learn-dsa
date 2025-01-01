def check_sorted(arr: list[int]) -> bool:
    return check_sorted_helper(arr, 0)

def check_sorted_helper(arr: list[int], pointer: int) -> bool:
    # Base condition
    if pointer >= len(arr) -1:
        return True

    return arr[pointer] <= arr[pointer + 1] and check_sorted_helper(arr, pointer+1)


if __name__ == "__main__":
    print(check_sorted([1,2,3]))
    print(check_sorted([1,3, 2]))
    print(check_sorted([1]))
    print(check_sorted([]))

