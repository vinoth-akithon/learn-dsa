"""

"""


def naive_approach(arr: list[int]) -> int:
    """
        Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1) 
    """
    n = len(arr)
    max_con = 0

    for i in range(n):
        current_max_con = 0
        if arr[i] == 1:
            current_max_con += 1
            for j in range(i+1, n):
                if arr[j] == 0:
                    max_con = max(max_con, current_max_con)
                    break
                current_max_con += 1
            else: 
                max_con = max(max_con, current_max_con)
    return max_con


def optimal_approach(arr: list[int]) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    max_con = 0
    curr_max_con = 0

    for i in range(n):
        if arr[i] == 0:
            max_con = max(max_con, curr_max_con)
            curr_max_con = 0
        else:
            curr_max_con += 1

    max_con = max(max_con, curr_max_con)
    return max_con



if __name__ == "__main__":
    arr = [0,0,0]
    # print(naive_approach(arr))
    print(optimal_approach(arr))