

def brute_force(n: int) -> None:
    arr = []
    for i in range(n + 1):
        if i < 2:
            print(i)
            arr.append(i)
        else:
            fib_i = arr[i-1] + arr[i-2]
            print(fib_i)
            arr.append(fib_i)



def using_recursion(n: int, arr: list[int]) -> None:
    """
        Complexity Analysis:
            Time -> O(n)
            Space -> O(n) -> due to recursion stack and fibonacci array 
    """
    # Base condition
    if n < len(arr):
        return arr[n]

    fib_n = using_recursion(n-1, arr) + using_recursion(n-2, arr)
    arr.append(fib_n)
    return fib_n



if __name__ == "__main__":
    n = 10
    arr = [0, 1]
    print(using_recursion(n, arr))
    print(arr)