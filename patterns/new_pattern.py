def print_pattern1(N: int):
    mid = (N//2)+1
    for i in range(1, N+1):
        for j in range(1, N+1):
            # if j==mid or (i-j == mid-1) or (i+j == mid+N): # for down arrow
            # if j==mid or (i+j == mid+1) or (j-i == mid-1): # for up arrow 
            # if (i == mid) or (i+j == mid+1) or (i-j == mid-1): # left arrow
            if (i == mid) or (j-i == mid-1) or (i+j == mid+N): # right arrow
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
def print_pattern2(N: int):
    for i in range(1, N+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
def print_pattern3(N: int):
    for i in range(1, N+1):
        print(" " * (N-i), end="")
        print("* " * i, end="")
        print()
def print_pattern4(N: int):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i>=j:
                print(i, end=" ")
            else:
                print("*", end=" ")
        print()
def print_pattern5(N: int):
    for i in range(N):
        for j in range(N):
            print(abs(i-j), end=" ")
        print()
def print_pattern6(N: int):
    for i in range(N):
        for j in range(N):
            print(abs(N-1-i-j), end=" ")
        print()
def print_pattern7(N: int):
    for i in range(N):
        for j in range(N):
            if i==j:
                print(i+1, end=" ")
            else:
                print("0", end=" ")
        print()
def print_pattern8(N: int):
    for i in range(N):
        for j in range(N):
            if i>=j:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()
def print_pattern9(N: int):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i <= N//2:
                print("0", end=" ")
            else:
                print("1", end=" ")
        print()
def print_pattern10(N: int):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if j <= N//2:
                print("0", end=" ")
            else:
                print("1", end=" ")
        print()
def print_pattern11(N: int):
    for i in range(N):
        for j in range(i, i+N):
            print((j%N)+1, end=" ")
        print()
def print_pattern12(N: int):
    for i in range(1, N+1):
        pointer = 1
        for j in range(i, N+i):
            if pointer < i:
                print("0", end=" ")
                pointer += 1
            else:
                print(j, end=" ")
        print()



if __name__ == "__main__":
    print_pattern12(5)