import collections

def number_of_arithmetic_slices(arr: list[int]) -> int:
    n = len(arr)
    if n < 3:
        return 0
    
    result = 0
    s = 0
    counter = collections.Counter()
    for e in range(1, n):
        diff = arr[e] - arr[e-1]
        counter[diff] += 1

        # Shrinking 
        if e > 2:
            diff = arr[s+1] - arr[s]
            counter[diff] -= 1
            if counter[diff] == 0:
                del counter[diff]
            s += 1

        if e >= 2 and max(counter.values()) == 2:
            result += n-e

    return result
            

if __name__ == "__main__":
    # arr = [1,2,3,4]
    # arr = [1,3,5,7,9]
    # arr = [7,7,7,7]
    # arr = [3,-1,-5,-9]
    arr = [1,2,3,8,9,10]
    print(number_of_arithmetic_slices(arr))