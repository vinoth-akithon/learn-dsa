def happy_number(n: int) -> bool:
    seen = set()
    while True:
        seen.add(n)
        s = 0
        while (n):
            s += (n%10)**2
            n //= 10
        if s == 1:
            return True
        elif s in seen:
            return False
        n = s


if __name__ == "__main__":
    # n = 19
    n = 2
    print(happy_number(n))