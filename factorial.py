
def factorial_using_loop(num: int) -> int:
    # 3 -> 3 * 2 * 1 -> 6
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    return factorial


def factorial_using_recursion(num: int) -> int:
    # base condition
    if num == 0:
        return 1
    
    return num * factorial_using_recursion(num - 1)

# print(factorial_using_loop(4))
print(factorial_using_recursion(4))

