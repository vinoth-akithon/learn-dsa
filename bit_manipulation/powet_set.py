"""
Power set is the array that contains all the subset of the given array including empty array
"""


def brute_force(arr: list) -> list[int]:
    """
    
    """
    n = len(arr)
    power_set = [[]]
    for i in range(n):
        sub_set = []
        for j in range(i, n):
            sub_set = sub_set.copy()
            sub_set.append(arr[j])
            power_set.append(sub_set)

    return power_set


if __name__ == "__main__":
    arr = [1,2,3]
    print(brute_force(arr))