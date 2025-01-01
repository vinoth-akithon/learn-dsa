def print_numbers_1_to_n(n: int):
    if n == 0:
        return
    print_numbers_1_to_n(n-1)
    print(n)


def print_numbers_n_to_1(n: int) -> None:
    if n == 0:
        return
    print(n)
    print_numbers_n_to_1(n-1)

if __name__ == "__main__":
    print_numbers_1_to_n(5)
    print("--")
    print_numbers_n_to_1(5)