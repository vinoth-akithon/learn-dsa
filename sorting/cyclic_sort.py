def cyclic_sort(arr: list[int]) -> None:
    # n = len(arr)
    # for i in range(n-1):
    #     c = arr[i]
    #     while c != i + 1:
    #         arr[i], arr[c-1] = arr[c-1], arr[i]
    #         c = arr[i]

    n = len(arr)
    for i in range(n-1):
        while arr[i] != i + 1:
            c = arr[i]-1
            arr[i], arr[c] =  arr[c], arr[i]
            # c = arr[i]


if __name__ == "__main__":
    arr = [3, 5, 2, 1, 4]
    cyclic_sort(arr)
    print(arr)