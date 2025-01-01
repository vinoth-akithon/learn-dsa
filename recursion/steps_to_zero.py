
def step_count(num: int, count=0) -> int:
    if num == 0:
        return count

    if num%2 == 0:
        return step_count(num//2, count+1)
    return step_count(num-1, count+1)


def step_count2(num: int) -> int:
    if num == 0:
        return 0

    if num%2 == 0:
        return 1 + step_count2(num//2)
    return 1 + step_count(num-1)


def step_count3(num: int) -> int:
    count = 0

    while num != 0:
        if num%2 == 0:
            num //= 2
        else:
            num -= 1
        count += 1
    return count



if __name__ == "__main__":
    print(step_count(14))
    print(step_count2(14))
    print(step_count3(14))
    print(step_count(2))