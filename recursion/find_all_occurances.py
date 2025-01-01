
def find_all_occurances(arr: list[int], target: int) -> list[int]:
    resultArray = []
    find_all_occurances_helper(arr, target, 0, resultArray)
    return resultArray


def find_all_occurances_helper(arr: list, target: int, pointer: int, resultArray: list[int]) -> None:
    if pointer == len(arr):
        return
    if arr[pointer] == target:
        resultArray.append(pointer)
    find_all_occurances_helper(arr, target, pointer+1, resultArray)


def find_all_occurances2(arr: list[int], target: int) -> list[int]:
    return find_all_occurances_helper2(arr, target, 0)


def find_all_occurances_helper2(arr: list[int], target: int, pointer: int) -> list[int]:
    result = []
    if pointer == len(arr):
        return result

    if arr[pointer] == target:
        result.append(pointer)
        
    return result + find_all_occurances_helper2(arr, target, pointer+1)



if __name__ == "__main__":
    print(find_all_occurances([1,2,3,4,11,2], 2))
    print(find_all_occurances2([1,2,3,4,11,2], 2))
