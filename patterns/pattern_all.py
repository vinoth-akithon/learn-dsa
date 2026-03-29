# print("Hello World")

arr = [10,20,30,40]

# for i in range(len(arr)):
#     print(arr[i])

# i = 0
# while i < len(arr):
#     print(arr[i])
#     i += 1


def func(a: int =0):
    print(id(a))

# num = 29080000000
# print(id(num))
# func(num)


def pattern1(count: int, times: int) ->None:
    """
        Time -> O(n^2)
        Space -> O(1)
    """
    for _ in range(times):
        for _ in range(count):
            print("*", end="")
        print()

# pattern1(5,5)

def pattern2(count: int) ->None:
    """
        Time -> O(n * (n+1)/2)
        Space -> O(1)
    """
    for i in range(count):
        for _ in range(0, i+1):
            print("*", end="")
        print()

# pattern2(5)


def pattern3(count: int) ->None:
    """
        Time -> O(n * (n+1)/2)
        Space -> O(1)
    """
    for i in range(1, count+1):
        for j in range(1, i+1):
            print(j, end="")
        print()

# pattern3(5)


def pattern4(count: int) ->None:
    """
        Time -> O(n * (n+1)/2)
        Space -> O(1)
    """
    for i in range(1, count+1):
        for _ in range(1, i+1):
            print(i, end="")
        print()

# pattern4(5)

def pattern5(count: int) ->None:
    """
        Time -> O(n * (n+1)/2)
        Space -> O(1)
    """
    for i in range(count, 0, -1):
        for _ in range(0, i):
            print("*", end="")
        print()

# pattern5(5)


def pattern6(count: int) ->None:
    """
        Time -> O(n * (n+1)/2)
        Space -> O(1)
    """
    for i in range(count, 0, -1):
        for j in range(1, i+1):
            print(j, end="")
        print()

# pattern6(5)

def pattern7(count: int) ->None:
    """
        Time -> O(n^2)
        Space -> O(1)
    """
    x = 1
    while (x <= count):
        spaces = count - x
        for i in range(spaces//2):
            print(" ", end="")
        for _ in range(x):
            print("*", end="")
        for _ in range(spaces//2):
            print(" ", end="")
        print()
        x += 2

# pattern7(7)

def pattern8(count: int) ->None:
    """
        Time -> O(n^2)
        Space -> O(1)
    """
    x = count
    while (x >= 1):
        spaces = count - x
        for i in range(spaces//2):
            print(" ", end="")
        for _ in range(x):
            print("*", end="")
        for _ in range(spaces//2):
            print(" ", end="")
        print()
        x -= 2

# pattern8(7)

def pattern9(count: int) ->None:
    """
        Time -> O(n^2)
        Space -> O(1)
    """
    pattern7(count)
    pattern8(count)

# pattern9(9)

def pattern10(count: int) ->None:
    """
        Time -> O(n^2)
        Space -> O(1)
    """
    pattern2(count)
    for i in range(count-1, 0, -1):
        for _ in range(0, i):
            print("*", end="")
        print()

# pattern10(5)

def pattern11(count: int) ->None:
    """
        Time -> O(n^2)
        Space -> O(1)
    """
    for i in range(count):
        for j in range(0, i+1):
            if (i % 2 == 0) and( j % 2 == 0):
                print(1, end="")
            elif (i % 2 != 0) and( j % 2 != 0):
                print(1, end="")
            else:
                print(0, end="")
        print()

# pattern11(5)

def pattern12(count: int) ->None:
    """
        Time -> O(n^2)
        Space -> O(1)
    """
    for i in range(1, count+1):
        for j in range(1, i+1):
            print(j, end="")

        space = count - i 
        for _ in range(space * 2):
            print(" ", end="")

        for j in range(i, 0, -1):
            print(j, end="")
        print()
        


# pattern12(5)

def pattern13(count: int) ->None:
    """
        Time -> O(n^2)
        Space -> O(1)
    """
    counter = 1
    for i in range(count):
        for _ in range(i+1):
            print(counter, end=" ")
            counter += 1
        print()
    

# pattern13(5)

def pattern14(count: int) ->None:
    """
        Time -> O(n^2)
        Space -> O(1)
    """
    for i in range(count):
        counter = 65
        for j in range(i+1):
            print(chr(counter + j), end=" ")
        print()
    

# pattern14(5)


def pattern15(count: int) ->None:
    """
        Time -> O(n^2)
        Space -> O(1)
    """
    for i in range(count, 0, -1):
        counter = 65
        for j in range(0, i):
            print(chr(counter + j), end=" ")
        print()
    

# pattern15(5)


def pattern16(count: int) ->None:
    """
        Time -> O(n^2)
        Space -> O(1)
    """
    START = 65
    for i in range(count):
        counter = START + i
        for _ in range(i+1):
            print(chr(counter), end="")
        print()

# pattern16(5)


def pattern17(row: int) ->None:
    """
        Time -> O(n^2)
        Space -> O(1)
    """
    for i in range(row):
        for _ in range(row - i - 1):
            print(" ", end="")
    
        for j in range(i+1):
            print(chr(ord("A") + j), end="")
        
        for j in range(i-1, -1, -1):
            print(chr(ord("A") + j), end="")

        for _ in range(row - i - 1):
            print(" ", end="")
        print()

# pattern17(3)


def pattern18(row: int) ->None:
    """
        Time -> O(n^2)
        Space -> O(1)
    """
    for i in range(row):
        for j in range(row-i-1, row):
            print(chr(ord("A") + j), end="")
        print()

# pattern18(5)

def pattern19(row: int) ->None:
    """
        Time -> O(n^2)
        Space -> O(1)
    """
    for i in range(row):
        print("*" * (row -i), end="")
        print(" " * i, end="")

        print(" " * i, end="")
        print("*" * (row -i))
    for i in range(1, row+1): 
        print("*" * (i), end="")
        print(" " * (row - i), end="")

        print(" " * (row - i), end="")
        print("*" * i)

# pattern19(5)


def pattern20(row: int) ->None:
    """
        Time -> O(n^2)
        Space -> O(1)
    """
    for i in range(1, row+1):
        print(i * "*", end="")
        print(2 * (row-i) * " ", end="")
        print(i * "*", end="\n")

    for i in range(row-1, 0, -1):
        print(i * "*", end="")
        print(2 * (row-i) * " ", end="")
        print(i * "*", end="\n")

# pattern20(5)

def pattern21(row: int) ->None:
    """
        Time -> O(n^2)
        Space -> O(1)
    """
    for i in range(1, row+1):
        if i in [1, row]:
            print("*" * row)
        else:
            print("*", end="")
            print(" " * (row-2), end="")
            print("*", end="\n")

# pattern21(5)

def pattern22(row: int) ->None:
    """
        Concentric Square Pattern (means, square inside a square, here share the center)
        Time -> O(n^2)
        Space -> O(1)
    """
    for i in range(2*row-1):
        for j in range(2*row-1):
            top = i
            bottom = (2*row - 2) - i
            left = j
            right = (2*row - 2) - j

            min_distance = min([top, bottom, left, right])
            print(row  - min_distance, end="")
        print()
pattern22(3)