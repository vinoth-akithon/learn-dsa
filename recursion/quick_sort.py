

def quick_sort(arr: list[int]) -> None:
    quick_sort_helper(arr, 0, len(arr)-1)

def quick_sort_helper(arr: list[int], l: int, h: int) -> None:
    if l >= h:
        return 
    
    s = l
    e = h
    m = s + (e-s)//2
    pivot = arr[m]

    while (s < e):
        while (arr[s] < pivot):
            s += 1
        while (arr[e] > pivot):
            e -= 1
    
        arr[s], arr[e] = arr[e], arr[s]

    quick_sort_helper(arr, l, e-1)
    quick_sort_helper(arr, s+1, h)


    



if __name__ == "__main__":
    # arr = [10, 50, 20, 30, 70]
    # arr = [50,40, 30, 20, 10]
    # arr = [50, 25, 92, 16, 76, 30, 43, 54, 19]
    # arr = []
    arr = [1]

    quick_sort(arr)
    print(arr)