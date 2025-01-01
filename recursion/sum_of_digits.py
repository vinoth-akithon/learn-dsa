def sum_of_digits_iterative(num: int) -> int:
    sum = 0
    while (num > 0):
        sum += num % 10
        num //= 10
    return sum


def sum_of_digits_recursive(num: int) -> int:
    """
        - Number of digits can be calculated using this formula:
            - log(n) + 1
        - Time complexity here is O(logn) + 1 ~= O(logn)
    """
    if num <= 9:
        return num
    return (num%10) + sum_of_digits_recursive(num//10)


if __name__ == "__main__":
    print(sum_of_digits_iterative(9))
    print(sum_of_digits_recursive(9))
