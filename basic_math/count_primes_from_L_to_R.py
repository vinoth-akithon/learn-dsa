"""

"""


def is_prime(n: int):
    """
        - Complexity Analysis:
            - Time -> O(sqrt(n))
            - Space -> O(1)
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def brute_force(arr: list[list[int, int]]) -> list[int]:
    """
        - Using prefix sum and prime check
        - Complexity Analysis:
            - Time -> O(Q (for getting max) + M*sqrt(M) (for formulating prime counts) + Q)
            - Space -> O(M)
    """
    max_ = max([e[1] for e in arr])
    # hash_map = {0: 0, 1: 0}
    hash_arr = [0] * (max_+1)

    for i in range(2, max_+1):
        if is_prime(i):
            hash_arr[i] = hash_arr[i-1] + 1
        else:
            hash_arr[i] = hash_arr[i-1]

    return [hash_arr[q[1]] - hash_arr[q[0]-1] for q in arr]




def optimal_approach(arr: list[list[int, int]]) -> list[int]:
    """
        - Sieve of Eratosthenes and Prefix Sum
        - Complexity Analysis:
            - Time -> O(Q + sqrt(M)*logM + M + Q) ~= O(sqrt(M)*logM)
            - Space -> O(M)
    
    """
    max_ = max(q[1] for q in arr)
    if max_ < 2:
        return [0] * len(arr)

    hash_arr = [True] * (max_+1)

    for i in range(2, int(max_**0.5)+1):
        if hash_arr[i]:
            for j in range(i*i, max_+1, i):
                hash_arr[j] = False

    hash_arr[0] = hash_arr[1] = False

    new_hash_arr = [0, 0, ]
    for i in range(2, max_+1):
       new_hash_arr.append(new_hash_arr[i-1] + hash_arr[i])

    result = []
    for q in arr:
        result.append(new_hash_arr[q[1]] - new_hash_arr[q[0]-1])

    return result

    # result = []
    # for q in arr:
    #     r = 0
    #     for i in range(q[1]+1):
    #         if hash_arr[i]:
    #             r += 1

    #     l = 0
    #     for i in range(q[0]):
    #         if hash_arr[i]:
    #             l += 1

    #     result.append(r-l)

    return result
    

if __name__ == "__main__":
    # arr = [[2,5]]
    arr = [ [1, 7], [3, 7] ]
    # print(brute_force(arr))
    print(optimal_approach(arr))

