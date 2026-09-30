"""


"""

def recursive_func(a: list[int], b: list[int], s: int, ms: int, c: int, i: int, j: int) -> int:
    # Base condition
    if s > ms:
        return c
    elif i > len(a) and j > len(b):
        return c

    curr_sum = a[i] + s
    cnt1 = recursive_func(a, b, curr_sum, ms, c+1, i+1, j)

    curr_sum = b[j] + s
    cnt2 = recursive_func(a, b, curr_sum, ms, c+1, i, j+1)

    return max(cnt1, cnt2)


def brute_force(a: list[int], b: list[int], ms: int):
    return recursive_func(a, b, 0, ms, 0, 0, 0) - 1



if __name__ == "__main__":
    a = [1, 6, 4, 2, 4]; b = [5, 8, 1, 2]; ms = 10
    print(brute_force(a, b, ms))