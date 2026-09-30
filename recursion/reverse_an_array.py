"""
reverse(in_arr, c) = reverse([10,20,30], 0) -> Append 20, so out_arr = [30, 20, 10]
                                    |
                                    reverse([10, 20, 30], 1) -> Append 20, so out_arr = [30, 20]
                                                |
                                                reverse([10, 20, 30], 2) -> Append 30, so out_arr = [30]
                                                            |
                                                            reverse([10,20, 30], 3) -> returns []
                                                                        
"""



def reverse_an_array(arr: list[int], c: int) -> list[int]:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n) -> Due to recursive stack
    """
    # Base Condition
    if c == len(arr):
        return []
    out_arr = reverse_an_array(arr, c+1)
    out_arr.append(arr[c])
    return out_arr



if __name__ == "__main__":
    in_arr = [10,20,30]
    print(reverse_an_array(in_arr, 0))