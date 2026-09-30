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
# print(triplets_closest_to_target(arr, t))
# print(triplets_closest_to_target2(arr, t))



def valid_triangle_number(arr: list[int]) -> int:
    arr.sort()
    count = 0
    n = len(arr)
    for i in range(n-1, 1, -1):
        c = arr[i]
        l = 0
        r = i-1
        while (l < r):
            s = arr[l] + arr[r]
            if s > c:
                count += r-l
                r -= 1
            else:
                l += 1
    return count


# print(valid_triangle_number([2,2,3,4]))
# print(valid_triangle_number([4,2,3,4]))


def longest_consecutive_sequence(arr: list[int]) -> int:
    arr = list(set(arr))
    arr.sort()
    max_con_seq_count, i, n = 0, 0, len(arr)
    while (i < n):
        j = i
        l = 1
        while (j < n-1 and arr[j+1] == arr[j]+1):
            l += 1
            j += 1
        i = j+1
        max_con_seq_count = max(max_con_seq_count, l)
    return max_con_seq_count


# arr = [10, 1, 4,  20, 21,22,]
# arr = [100,4,200,1,3,2]
# arr = [0,3,7,2,5,8,4,6,0,1]
arr = [1, 0, 1, 2]
# print(longest_consecutive_sequence(arr))


def longest_consecutive_sequence2(arr: list[int]) -> int:
    hash_set = set(arr)
    max_con_seq_count, n = 0, len(arr)
    for e in hash_set:
        if (e-1) not in hash_set:
            l = 1
            while (e + l) in hash_set:
                l += 1
            max_con_seq_count = max(max_con_seq_count, l)
    return max_con_seq_count

# arr = [10, 1, 4,  20, 21,22,]
# arr = [100,4,200,1,3,2]
# arr = [0,3,7,2,5,8,4,6,0,1]
# arr = [1,0,1,2]
# print(longest_consecutive_sequence2(arr))


def longest_consecutive_sequence3(arr: list[int]) -> int:
    arr = list(set(arr))
    arr.sort()
    max_con_seq_count, i, n = 0, 0, len(arr)
    while (i < n):
        l = 1
        while (i+l < n) and (arr[i+l] == arr[i]+l):
            l += 1
        i += l
        max_con_seq_count = max(max_con_seq_count, l)
    return max_con_seq_count


# arr = [10, 1, 4,  20, 21,22,]
# arr = [100,4,200,1,3,2]
# arr = [0,3,7,2,5,8,4,6,0,1]
arr = [1, 0, 1, 2]
# print(longest_consecutive_sequence3(arr))


def boats_to_save_people(arr: list[int], t: int):
    arr.sort()
    no_boats = 0
    n = len(arr)
    l, r = 0, n-1
    while (l <= r):
        s = arr[l] + arr[r]
        if s > t:
            r -= 1
        else:
            l += 1
            r -= 1
        no_boats += 1
    return no_boats


# arr = [3,2,2,1]; t = 3
# arr = [1,2]; t = 3
arr = [3, 5, 3, 4];t = 5
# print(boats_to_save_people(arr, t))



def find_k_closed_element(arr: list[int], k: int, x: int):
    la = []
    ra = []
    res = []
    for e in arr:
        if e < x:
            la.append(e)
        else:
            ra.append(e)

    l = len(la)-1
    r = 0

    while (len(res) < k and l >= 0 and r < len(ra)):
        s1 = abs(la[l] - x)
        s2 = abs(ra[r] - x)
        if s1 < s2:
            res.append(la[l])
            l -= 1
        elif s1 == s2 and la[l] < ra[r]:
            res.append(la[l])
            l -= 1
        else:
            res.append(ra[r])
            r += 1
    while (len(res) < k and l >= 0):
        res.append(la[l])
        l -= 1

    while (len(res) < k and r < len(ra)):
        res.append(ra[r])
        r += 1

    res.sort()
    return res

arr = [1,2,3,4,5]; k = 4; x = 3
# arr = [1,1,2,3,4,5]; k = 4; x = -1
# arr = [0,0,1,2,3,3,4,7,7,8]; k = 3; x = 5  
# print(find_k_closed_element(arr, k, x))



def majority_element(arr: list[int]) -> int:
    count = 0
    element = None
    for e in arr:
        if not count:
            count = 1
            element = e
        elif e == element:
            count += 1
        else:
            count -= 1
    return element


arr = [3,2,3]
arr = [2,2,1,1,1,2,2]
# print(majority_element(arr))


def bubble_sort(arr: list[int]) -> list[int]:
    """
        - Educational purpose sorting algo
        - Time -> O(n^2)
        - Space -> O(1)

        Algo:
            - Implementing loop with the n-1 times
            - compare adjacent elements and swap if it's in the wrong place.
    """
    n = len(arr)
    for i in range(n-1, 0, -1):
        sorted = True
        for j in range(i):
            if arr[j] > arr[j+1]:
                sorted = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if sorted:
            print(i)
            print("pass")
            break
    return arr


def selection_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n-1):
        curr_max_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[curr_max_idx]:
                curr_max_idx = j
        arr[i], arr[curr_max_idx] = arr[curr_max_idx], arr[i]
    return arr


arr =[3,1,5,2,8]
# arr = [1,2,3,4,5]
# print(bubble_sort(arr))
# print(selection_sort(arr))




def length_of_non_repeating_char(s: str):
    n = len(s)
    l = 0
    hash_table = {}
    max_window = 0
    for r in range(n):
        if s[r] in hash_table and hash_table[s[r]] >= l:
            l = hash_table[s[r]]+1
        hash_table[s[r]] = r
        curr_max_window = r-l+1
        max_window = max(max_window, curr_max_window)
    return max_window

# s = "abccabd"
s = "pwwkew"
# print(length_of_non_repeating_char(s))


def left_rotate(arr: list[int], p: int):
    """
        - Also called as clockwise rotation
        - Complexity Analysis:
            - Time -> O(2n) ~= O(n)
            - Space -> O(n)
    """
    n = len(arr)
    left_array = []
    right_array = []

    for i in range(p):
        left_array.append(arr[i%n])
    
    for i in range(p, n):
        right_array.append(arr[i%n])


    for i in range(n-p):
        arr[i] = right_array[i]

    for i in range(p):
        arr[n-p+i] = left_array[i]

    return arr


# arr = [1,2,3,4,5]; p = 2
# print(left_rotate(arr, p))

# [1,2]
# [3,4,5]

"""

left_arr = [1, 2]
right_arr = [3,4,5]

[1,2,3,4,5] -> [3,4,5,1,2]
we can say 
    -> left rotated 2 places (undo left rotation 2 places means right rotate 2 places)
    -> right rotated 3 places (undo right rotation 3 places means left rotate 3 places)
"""



def undo_rotation(arr: list[int]) -> list:
    """
    
    """
    n = len(arr)

    i = 0
    while (i < n-1):
        if arr[i+1] < arr[i]:
            break
        i += 1
    else:
        print("pass")
        return arr
    
    p = i+1
    return left_rotate(arr, p)


# arr = [1,2,3,4,5]; p = 1
# left_rotated_arr = left_rotate(arr, p)
# print(undo_rotation(left_rotated_arr))



def find_target(arr: list[int], t: int) -> int:
    """
    Using Binary search (assuming given arr is sorted)
    """

    n = len(arr)
    s = 0
    e = n-1

    while (s <= e):
        m = s + (e-s)//2

        if arr[m] == t:
            return m
        elif arr[m] < t:
            s = m+1
        else:
            e = m-1

    return -1


def floor_of_target(arr: list[int], t: int) -> int:
    """
    - Also called upper bound.
    - Using Binary Search approach (assuming given arr is sorted)
    """
    n = len(arr)
    
    s = 0
    e = n-1
    floor_index = None

    while (s <= e):
        m = s + (e-s)//2

        if arr[m] <= t:
            floor_index = m
            s = m+1
        else:
            e = m-1

    return arr[floor_index] if floor_index is not None else -1


def ceil_of_target(arr: list[int], t: int) -> int:
    """
    - Also called lower bound
    - Using Binary search
    """
    n = len(arr)
    s = 0
    e = n-1
    ceil_idx = None

    while (s <= e):
        m = s + (e-s)//2
        
        if arr[m] >= t:
            ceil_idx = m
            e = m - 1
        else:
            s = m + 1

    return arr[ceil_idx] if ceil_idx is not None else -1


def insert_position(arr: list[int], t: int) -> int:
    """
    - Also called lower bound (ceil)
    - Using Binary search
    """
    n = len(arr)
    s = 0
    e = n-1
    ceil_idx = None

    while (s <= e):
        m = s + (e-s)//2
        
        if arr[m] >= t:
            ceil_idx = m
            e = m - 1
        else:
            s = m + 1

    return ceil_idx if ceil_idx is not None else n

def count_occurrences(arr: list[int], t: int) -> int:
    """
    - Find the lower bound index
    - Find the Upper bound index
    - Calculate the index difference
    - Using Binary search
    """
    n = len(arr)
    s = 0
    e = n-1
    lower_bound_idx = None

    while (s <= e):
        m = s + (e-s)//2
        
        if arr[m] >= t:
            lower_bound_idx = m
            e = m - 1
        else:
            s = m + 1

    s = 0
    e = n-1
    upper_bound_idx = None

    while (s <= e):
        m = s + (e-s)//2
        if arr[m] <= t:
            upper_bound_idx = m
            s = m + 1
        else:
            e = m - 1
    
    return upper_bound_idx - lower_bound_idx + 1 if (upper_bound_idx and lower_bound_idx) else 0


# arr = [1,2,4,5,6,7,8,9]; t = 3
arr = [3, 4, 13, 13, 13, 20, 40]; t = 13
# print(find_target(arr, t))
# print(floor_of_target(arr, t))
# print(ceil_of_target(arr, t))
# print(insert_position(arr, t))
# print(count_occurrences(arr, t))

# 0 -> 5 if s = 2, e = 5, so m = (5-2)/2 + 2 => 3
# 0 -> if s = 1 e = 5, so m = (5-1)/2 + 1 => 3




def left_rotate(arr: list[int], p: int) -> list[int]:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """

    n = len(arr)
    left_arr = []
    right_arr = []

    for i in range(p):
        left_arr.append(arr[i%n])

    for i in range(p, n):
        right_arr.append(arr[i%n])

    # print(left_arr, right_arr)
    for i in range(n-p):
        arr[i] = right_arr[i]

    for j in range(p):
        arr[n-p+j] = left_arr[j]

    return arr


def undo_rotation(arr: list[int]) -> list[int]:
    """
        - Complexity Analysis:
            - Time -> O(n + n) ~= O(n)
            - Space -> O(n)
    """
    n = len(arr)

    i = 0
    while (i < n-1):
        if arr[i+1] < arr[i]:
            break
        i += 1

    p = i+1
    return left_rotate(arr, p)

def search_in_a_rotated_sorted_array(arr: list[int], t: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n + n + (n + n) + log n) ~= O(n)
            - Space -> O(n + n) ~= O(n)
    """
    # Phase 1: Finding the breaking place
    n = len(arr)
    auxiliary_arr = [(val, idx) for idx, val in enumerate(arr)]
    i = 0
    while (i < n-1):
        if arr[i+1] < arr[i]:
            break
        i += 1
    
    p = i+1


    # Phase2: Undo the rotation to make complete sorted array
    left_rotate(auxiliary_arr, p) # Array becomes sorted array (but not rotated)


    # Phase3: Apply binary search to find the target
    s = 0
    e = n-1
    
    while (s <= e):
        m = s + (e-s)//2

        if auxiliary_arr[m][0] == t:
            return auxiliary_arr[m][1]
        elif auxiliary_arr[m][0] < t:
            s = m + 1
        else:
            e = m-1

    return -1

def search_in_a_rotated_sorted_array2(arr: list[int], t: int) -> int:
    """
        - Rotated Array Property: In a sorted rotated array (without any duplicates), either half of the array is sorted arr[s...m] or arr[m...e] (inclusive m)
        - find the mid element and check against the target, if matched return it's index
        - check the left half is sorted
            - Check the target with in the left half
                - If so, shrink the array to left half
                - else, shrink the array to right half
        - check the right half is sorted
            - check the target lies in the right half
                - If so, shrink the array to right half
                - else, shrink the array to left half
    """
    n = len(arr)
    s = 0
    e = n-1

    while (s<=e):
        m = s + (e-s)//2

        if arr[m] == t:
            return True

        elif arr[s] <= arr[m]:
            if arr[s] <= t < arr[m]:
                e = m-1
            else:
                s = m+1
        else:
            if arr[m] < t <= arr[e]:
                s = m+1
            else:
                e = m-1
    return False

arr = [4,5,0,1,2,3]; t = 1
# arr = [0,0,0,1,0,0,0,0,0,0,0]; t = 1
# print(search_in_a_rotated_sorted_array(arr, t))


# arr = [4,5,0,1,2,3]; t = 2
# arr = [1]; t = 0
# print(search_in_a_rotated_sorted_array2(arr, t))


# [0,0,0,1,0,0,0,0,0,0,0] # left rotated by 8 position



def square_root_1(N: int) -> int:
    """
    Brute force approach (Checking all the lower possible numbers)

    Complexity Analysis:
        - Time -> O(n)
        - Space -> O(1)
    """

    if (N < 2):
        return N
    
    ans = 1
    for i in range(2, N):
        if (i * i > N):
            break
        else:
            ans = i

    return ans


def square_root_2(N: int) -> int:
    """
    Optimal Approach (Using Binary search start with medium range number)
    
    Complexity Analysis:
        - Time -> O(log n)
        - Space -> O(1)
    """
    
    if N < 2:
        return N

    ans = 1
    s = 2
    e = N

    while (s <= e):
        m = s + (e-s)//2

        if (m * m > N):
            e = m-1
        else:
            ans = m
            s = m + 1

    return ans


N = 36
# print(square_root_1(N))
# print(square_root_2(N))



def n_th_root_1(M: int, N: int) -> int:
    """
    Brute force approach (checking with smallest possible number)
    
    Complexity Analysis:
        - Time -> O(n)
        - Space -> O(1)
    """
    if N == 0:
        return M
    elif M < 2:
        return M

    for x in range(1, M+1):
        res = x ** N
        if res == M:
            return x 
        elif res > M:
            return -1



def n_th_root_2(M: int, N: int) -> int:
    """
    Optimal approach (start checking with mid range element)

    Complexity Analysis:
        Time -> O(log n)
        Space -> O(1)
    
    """
    if N == 0 or M < 2:
        return M

    s = 2
    e = M

    while (s <= e):
        x = s + (e-s)//2
        res = x ** N
        
        if res == M:
            return x
        elif res > M:
            e = x-1
        else:
            s = x + 1
    return -1

    


M = 27; N = 3
# N = 4; M = 69
# print(n_th_root_1(M, N))
# print(n_th_root_2(M, N))



def binary_search(arr: list[int], t: int) -> int:
    """
        - Exact match pattern
        - If found the target, return otherwise return -1
    """
    n = len(arr)
    s = 0
    e = n-1

    while (s <= e):
        m = s + (e-s)//2

        if arr[m] == t:
            return m
        elif arr[m] < t:
            s = m +1
        else:
            e = m -1

    return -1
        

# arr = [1,2,3,4,5,6,7]; t = 10
# print(binary_search(arr, t))


def count_occurrences(arr: list[int], t: int) -> int:
    """
    - Exact match pattern with variant
    - fist the first occurrence of the target and last occurrence of the target, their index differences are answer.
    """

    n = len(arr)

    # First Occurrence
    s = 0
    e = n-1
    first_occurrence = None

    while (s <= e):
        m = s + (e-s)//2

        if arr[m] == t:
            first_occurrence = m
            e = m - 1
        elif arr[m] < t:
            s = m+1
        else:
            e = m-1

    if not first_occurrence:
        return 0
    
    # last Occurrence
    s = 0
    e = n-1
    last_occurrence = None
    while (s <= e):
        m = s + (e-s)//2

        if arr[m] == t:
            last_occurrence = m
            s = m+1
        elif arr[m] < t:
            s = m+1
        else:
            e = m-1

    return last_occurrence - first_occurrence + 1


# arr = [1,2,2,2,3,3,4,5,6,7]; t = 4
# print(count_occurrences(arr, t))



def search_in_a_sorted_matrix(mat: list[list[int]], t: int) -> int:
    """
        - Exact match pattern
        - Think matrix like the flatten array

        - Complexity Analysis:
            - Time -> O(log n + log n) -> O(log n)
            - Space -> O(1)
    """
    if not mat and not mat[0]:
        return False

    r = len(mat)
    c = len(mat[0])

    sr = 0
    er = r-1

    while (sr < er):
        mr = sr + (er-sr)//2
        
        if mat[mr][0] == t:
            return True
        elif mat[mr][0] < t:
            if mat[mr][c-1] < t:
                sr = mr+1
            else:
                er = mr
        else:
            er = mr-1

    s = 0
    e = c-1

    while (s <= e):
        m = s + (e-s)//2

        if mat[sr][m] == t:
            return True
        elif mat[sr][m] < t:
            s = m + 1
        else:
            e = m-1

    return False


mat = [[1,2,3], [4,5,6], [7,8,9]]; t = 6
# print(search_in_a_sorted_matrix(mat, t))



def find_floor(arr: list[int], t: int) -> int:
    """
        - Floor means, largest element that is less than or equal to target
        - Using binary search
            - Search Space -> input array itself
            - Monotonicity -> non-decreasing order of elements
            - Elimination -> Half of the search space if we encounter the value which is greater than the target    
    """
    n = len(arr)

    s = 0
    e = n-1
    ans = None

    while (s <= e):
        m = s + (e-s)//2

        if arr[m] <= t:
            ans = arr[m]
            s = m+1
        else:
            e = m-1

    return ans


def find_floor2(arr: list[int], t: int) -> int:
    """
        - Upper bound problem
    """
    n = len(arr)
    s = 0
    e = n-1

    while (s < e):
        m = s + (e-s)//2

        if arr[m] < t:
            s = m+1
        else:
            e = m
    return arr[e]

arr = [1,2,3,4,5,6]; t = 5
# print(find_floor(arr, t))
# print(find_floor2(arr, t))



def count_negative_in_sorted_2d_matrix(mat: list[list[int]]) -> int:
    """
        - Find the first negative element in each row and compute the total negative numbers corresponding to that row.
        - Finally cumulate all negative numbers and return

        - Apply Binary search on each row for getting total negative for that row.

        - Complexity Analysis:
            - Time -> O(M * log (N)) 
            - Space -> O(1)
    
    """
    M = len(mat)
    N = len(mat[0])
    cnt = 0

    for r in range(M):
        start = N

        s = 0
        e = N-1
        while (s <= e):
            m = s + (e-s)//2

            if mat[r][m] < 0:
                start = m
                e = m-1
            else:
                s = m+1
        cnt += N-start
    
    return cnt

    

# mat = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
mat = [[3,2],[1,0]]
# print(count_negative_in_sorted_2d_matrix(mat))


def is_pages_feasible(pages, arr, u):
    """
    """
    users = 1
    curr_pages = arr[0]
    
    for i in range(1, len(arr)):
        if curr_pages + arr[i] > pages:
            users += 1
            curr_pages = arr[i]
        else:
            curr_pages += arr[i]

    return users <= u


def book_allocate(arr: list[int], u: int) -> int:
    """
        - Applying Binary search on Answer space (Pages)
        - Complexity Analysis:
            - Time -> O(n log n)
            - Space -> O(1)
    """
    min_pages = max(arr)
    max_pages = sum(arr)
    right_pages = max_pages

    while (min_pages <= max_pages):
        pages = min_pages + (max_pages - min_pages)//2

        if is_pages_feasible(pages, arr, u):
            right_pages = pages
            max_pages = pages - 1
        else:
            min_pages = pages + 1

    return right_pages


# arr = [12, 34, 67, 90]; u = 2
# arr = [25, 46, 28, 49, 24]; u = 4
# print(book_allocate(arr, u))


def is_cow_feasible(distance: int, arr: list[int], c: int) -> bool:
    cow_placed = 1
    last_distance = arr[0]

    for i in range(1, len(arr)):
        if arr[i] - last_distance >= distance:
            cow_placed += 1
            last_distance = arr[i]
        
    return cow_placed >= c
    


def aggressive_cows(arr: list[int], c: int) -> int:
    """
    
    """

    arr.sort()

    min_distance = 1
    max_distance = arr[-1] - arr[0]
    right_distance = min_distance

    while (min_distance <= max_distance):
        distance = min_distance + (max_distance - min_distance)//2

        if is_cow_feasible(distance, arr, c):
            right_distance = distance
            min_distance = distance + 1
        else:
            max_distance = distance - 1

    return right_distance


# arr = [0,3,4,7,10,9]; c = 4
arr = [4,2,1,3,6]; c = 2
# print(aggressive_cows(arr, c))



"""

I am vinothkumar
python FS Eng
having over 5 years of experience
currently working in SEA as an SDET, here primary domain is E commerce
previously I worked for 2 early stage startup including the admission department and health care department
I primary use python and nodejs for Backend component development
having good exposer in monolith and micro service architecture
Expertise in robust and scalable backend systems 
I focus TDD workflow, 
"""


class Person:
    count: int
    
    def __init__(self, id: int) -> None:
        self.id = id



def get_person_id(person: Person):
    person.id   


def brute_force( arr: list[list[int]]) -> list[list[int]]:
    merged_intervals = []
    n = len(arr)
    is_overlapped = False
    arr.sort()
    
    
    int1 = arr[0]
    for j in range(1, n):
        int2 = arr[j]
        if int1[1] >= int2[0] and int1[1] <= int2[1]:
            is_overlapped = True
            merged_intervals.append([int1[0], int2[1]])
                
        else:
            merged_intervals.append(int2)
    
    if is_overlapped:
        return brute_force(merged_intervals)
    else:
        merged_intervals[0] = int1
    return merged_intervals


# print(brute_force([[1,3],[2,6],[1,6],[8,10],[15,18]]))



def first_non_repeating_char_brute_force(s: str):
    """
        - Using Auxiliary DS (Hash Map as it preserves the insertion order) 
        - I am assuming at least one non duplicate char present in the input str
        
        - Complexity Analysis:
            - Time -> O(n + d) ~= O(n)
            - Space -> O(d) ~= O(26) ~= O(1)
    """
    hash_map = {}

    for c in s:
        if c in hash_map:
            hash_map[c] += 1
        else:
            hash_map[c] = 1

    for k,v in hash_map.items():
        if v == 1:
            return k

    return -1

def first_non_repeating_char_better_approach(s: str):
    """
        - Using Auxiliary DS (array of fixed size)
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(26) ~= O(1)
    """
    # arr = [0] * 26

    # for c in s:
    #     arr[ord(c)%26 - 19] += 1

    # for i in range(len(arr)):
    #     if arr[i] == 1:
    #         return chr(i + 97)

    arr = [[0, -1] for _ in range(26)]

    for i in range(len(s)):
        c = s[i]
        idx = ord(c)%26 - 19
        arr[idx][0] += 1
        if arr[idx][1] == -1:
            arr[idx][1] = i


def first_non_repeating_char_optimal_approach(s: str):
    """
        - Using Two pointer approach

        - Complexity Analysis:
            - Time -> O(n log n)
            - Space -> O(n)

    """
    s = "".join(sorted(s))
    n = len(s)
    l = 0
    r = 1

    while r < n:
        if s[r] == s[l]:
            r += 1
        else:
            diff = r-l
            if diff == 1:
                return s[l]
            l = r
            r += 1


s = "aaabbcddee"

# print(first_non_repeating_char_brute_force(s))
# print(first_non_repeating_char_better_approach(s))
# print(first_non_repeating_char_optimal_approach(s))



def number_of_substr_matches_the_pattern(s: str, p: str):
    """
        - Complexity Analysis:
            - Time -> O(n*m)
            - Space -> O(m)
    
    """
    n = len(s)
    m = len(p)
    cnt = 0

    if m > n:
        return cnt

    for i in range(n-m+1):
        if s[i:i+m] == p:
            cnt += 1
    
    return cnt


s = "ababbababa"; p = "aba"
# print(number_of_substr_matches_the_pattern(s, p))


"""
Regarding our L1 discussion for the Python Backend Developer role at Autnhive, here are the questions and solutions discussed for your records:

Interview Topics & Questions:

  - What is class and objects?
  - What is decorator?
  - What is generator?
  - What is encapsulation?
  - What is abstraction?
  - What is MRO?
  - What is LLM?
  - What is RAG?
  - LangChain vs. LangGraph
  - What is tokens?
  - RAG vs. Fine-tuning
  - How will you stop/reduce hallucinated response?
  - What is MCP server?

Technical Solutions:

1.  Python: Substring Count
    Find how many times a substring appears in a string.

text = "ababbababa"
pattern = "aba"
count = 0

for i in range(len(text) - len(pattern) + 1):
    if text[i:i + len(pattern)] == pattern:
        count += 1

print(count)

2.  Token Management Logic
    Selection to stay under 4,000 tokens based on priority scores:

  - chunk3 (1500 tokens, 0.95 score)
  - chunk1 (900 tokens, 0.91 score)
  - chunk2 (700 tokens, 0.88 score)
  - chunk5 (1200 tokens, 0.86 score)
  - Total: 3,100 tokens (Excludes chunk4 to maintain limit).

3.  First Non-Repeating Character
    Input: "aabbcddee"

def first_non_repeating(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for char in s:
        if counts[char] == 1:
            return char
    return None

Output: c

4.  Improving API Latency
    To improve performance, I would implement:

  - Caching: Using Redis for frequent queries.
  - Database Optimization: Indexing and query optimization in Postgres.
  - Asynchronous Processing: Utilizing Async/Await and FastAPI.
  - Infrastructure: Load balancing and Horizontal Scaling.
  - Data Transfer: Minimizing payload sizes via JSON optimization.
"""



def infix_to_postfix(s: str) -> str:
    """
        - exponential operator is the right associative, 
            - `a ^ b ^ c` => a ^ (b ^ c) but not (a ^ b) ^ c
    
    """
    precedence_map = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3 
    }


    res = ""
    stack = []

    for c in s:
        if c == " ":
            continue
        elif c.isalnum():
            res += c
        elif c == "(":
            stack.append(c)
        elif c == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != "("  and precedence_map[c] <= precedence_map[stack[-1]] and c != "^":
                res += stack.pop()
            stack.append(c)

    while stack:
        res += stack.pop()

    return res


s = "a + b * (c^d - e) ^ (f + g * h) - i "
# s = "(p + q) * (m - n)"
s = "a ^ b ^ c"
print(infix_to_postfix(s))

