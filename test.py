# You have to follow the following steps to find the sqrt of an integer N.

# Consider L = 1, R = N, and cnt = 0

# STEP 1: MID = (floor)(L+R)/2 and cnt += 1

# STEP 2: if ((MID * MID) == N), then go to STEP 5 else go to STEP 3.

# STEP 3: if ((MID * MID) < N), then L = MID+1 and go to STEP 1 else STEP 4.

# STEP 4: if ((MID * MID) > N), then R = MID - 1 and go to STEP 1.

# STEP 5: PRINT MID.


def square_root(N):
    L = 1
    R = N
    cnt = 0


def print_reverse_triangle_pattern(size: int) -> None:
    print_reverse_triangle_pattern_helper(size, 0)


def print_reverse_triangle_pattern_helper(r: int, c: int) -> None:
    # Base condition
    if r == 0:
        return 
    
    if c < r:
        print_reverse_triangle_pattern_helper(r, c+1)
        print("*", end = " ")
    else:
        print_reverse_triangle_pattern_helper(r-1, 0)
        print()



def triplet_sum_equal_to_target(arr: list[int], t: int) -> list[list[int]]:
    res = []
    arr.sort()
    n = len(arr)
    for i in range(n-2):
        if i > 0 and (arr[i] == arr[i-1]):
            continue
        X = arr[i]
        pair_target = t - X
        l = i+1
        r = n-1
        while (l < r):
            s = arr[l] + arr[r]
            if s == pair_target:
                res.append([X, arr[l], arr[r]])
                pre = arr[l]
                l += 1
                r -= 1
                while (l < r) and (arr[l] == pre):
                    l += 1
            elif s < pair_target:
                l += 1
            else:
                r -= 1
    return res


# arr = [1,2,5,4,3]; target = 6
# arr = [-1,0,1,2,-1,-4]; target = 0
# arr = [0,1,1]; target = 0
# arr = [0,0,0]; target = 0
arr = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]; target = 0
# print(triplet_sum_equal_to_target(arr, target))


def triplets_closest_to_target(arr: list[int], t: int) -> int:
    n = len(arr)
    arr.sort()
    closest_distance = float("inf")
    for i in range(n-2):
        l = i+1
        r = n-1
        while (l < r):
            triplet_sum = arr[i] + arr[l] + arr[r]
            if triplet_sum == t:
                return triplet_sum
            elif triplet_sum < t:
                l += 1
            else:
                r -= 1
            current_distance = triplet_sum - t
            if abs(current_distance) < abs(closest_distance):
                closest_distance = current_distance
        
    return closest_distance + t

def triplets_closest_to_target2(arr: list[int], t: int) -> int:
    n = len(arr)
    arr.sort()
    closest_distance = float("inf")
    closest_sum = 0
    for i in range(n-2):
        l = i+1
        r = n-1
        while (l < r):
            triplet_sum = arr[i] + arr[l] + arr[r]
            if triplet_sum == t:
                return triplet_sum
            elif triplet_sum < t:
                l += 1
            else:
                r -= 1
            current_distance = abs(triplet_sum - t)
            if current_distance < closest_distance:
                closest_distance = current_distance
                closest_sum = triplet_sum
        
    return closest_sum





arr = [-1,2,1,-4]; t = 1
arr = [0,0,0]; t = 1
# arr = [10,20,30,40,50,60,70,80,90]; t = 1
print(triplets_closest_to_target(arr, t))
print(triplets_closest_to_target2(arr, t))
