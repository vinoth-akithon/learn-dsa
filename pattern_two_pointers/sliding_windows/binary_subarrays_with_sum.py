def binary_subarrays_sum(arr: list[int], k: int):
    n = len(arr)
    s = 0
    curr_sum = 0
    count = 0
    for e in range(n):
        curr_sum += arr[e]

        while curr_sum > k:
            curr_sum -= arr[s]
            s -= 1

        if curr_sum == k:
            count += 1
            
        # while curr_sum >= k:
        #     if curr_sum == k:
        #         count += 1
        #     else:
        #         curr_sum -= arr[s]
        #         s -= 1






if __name__ == "__main__":
    # arr = [0,1,0,1,1,1,0]; k = 2
    arr = [1,0,1,0,1,0]; k = 2
    print(binary_subarrays_sum(arr, k))