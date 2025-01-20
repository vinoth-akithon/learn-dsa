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
